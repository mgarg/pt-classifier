import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st


LABEL_SOURCES = {
    "Labeled 10k template taxonomy": {
        "type": "labeled_products",
        "products": "data/labeled/sample.raw.10k.template_taxonomy.parquet",
        "cluster_column": "template_cluster",
    },
    "Template KMeans clusters": {
        "type": "label_samples",
        "labels": "data/cluster_labeling/template_clusters/template_cluster_labels.json",
        "samples": "data/cluster_labeling/template_clusters/template_cluster_labeling_samples.csv",
        "taxonomy": "data/taxonomy/template_product_taxonomy.json",
        "cluster_column": "template_cluster",
    },
    "Title KMeans clusters": {
        "type": "label_samples",
        "labels": "data/cluster_labeling/title_clusters/title_cluster_labels.json",
        "samples": "data/cluster_labeling/title_clusters/title_cluster_labeling_samples.csv",
        "taxonomy": "data/taxonomy/product_taxonomy.json",
        "cluster_column": "title_cluster",
    },
}


def resolve_project_path(relative_path: str) -> Path:
    for directory in [Path.cwd(), *Path.cwd().parents]:
        candidate = directory / relative_path
        if candidate.exists():
            return candidate
    raise FileNotFoundError(relative_path)


@st.cache_data
def load_json(relative_path: str):
    with resolve_project_path(relative_path).open() as file:
        return json.load(file)


@st.cache_data
def load_samples(relative_path: str) -> pd.DataFrame:
    return pd.read_csv(resolve_project_path(relative_path))


@st.cache_data
def load_labeled_products(relative_path: str) -> pd.DataFrame:
    return pd.read_parquet(resolve_project_path(relative_path))


def extract_image_url(value: object) -> str:
    if pd.isna(value):
        return ""

    text = str(value)
    match = re.search(r"https?://[^'\"\s,\)]+", text)
    if not match:
        return ""

    return match.group(0)


def sample_images_by_cluster(samples: pd.DataFrame) -> dict[int, list[str]]:
    images_by_cluster = {}
    for cluster_id, cluster_samples in samples.groupby("labeling_cluster_id"):
        urls = []
        for value in cluster_samples.get("images", []):
            url = extract_image_url(value)
            if url and url not in urls:
                urls.append(url)
            if len(urls) >= 6:
                break
        images_by_cluster[int(cluster_id)] = urls
    return images_by_cluster


def labels_to_dataframe(
    labels: list[dict],
    taxonomy: dict,
    cluster_column: str,
    images_by_cluster: dict[int, list[str]],
) -> pd.DataFrame:
    leaf_mapping = taxonomy.get("assignment", {}).get("leaf_mapping", {})
    rows = []
    for label in labels:
        cluster_id = label["cluster_id"]
        image_urls = images_by_cluster.get(cluster_id, [])
        rows.append(
            {
                "image": image_urls[0] if image_urls else "",
                "cluster_id": cluster_id,
                "taxonomy_node_id": leaf_mapping.get(str(cluster_id), ""),
                "label": label["label"],
                "parent_label": label["parent_label"],
                "confidence": label["confidence"],
                "description": label["description"],
                "include_keywords": ", ".join(label.get("include_keywords", [])),
                "exclude_keywords": ", ".join(label.get("exclude_keywords", [])),
                "cluster_column": cluster_column,
            }
        )
    return pd.DataFrame(rows).sort_values(["parent_label", "label"]).reset_index(drop=True)


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")

    parent_options = sorted(df["parent_label"].unique())
    selected_parents = st.sidebar.multiselect(
        "Parent category",
        parent_options,
        default=parent_options,
    )

    confidence_options = ["high", "medium", "low"]
    selected_confidence = st.sidebar.multiselect(
        "Confidence",
        confidence_options,
        default=confidence_options,
    )

    cluster_ids = sorted(df["cluster_id"].unique())
    selected_clusters = st.sidebar.multiselect(
        "Cluster ID",
        cluster_ids,
        default=cluster_ids,
    )

    query = st.sidebar.text_input(
        "Search labels / descriptions / keywords",
        placeholder="e.g. nail, hair, fragrance",
    ).strip()

    filtered = df[
        df["parent_label"].isin(selected_parents)
        & df["confidence"].isin(selected_confidence)
        & df["cluster_id"].isin(selected_clusters)
    ]

    if query:
        query_lower = query.lower()
        searchable = (
            filtered["label"]
            + " "
            + filtered["parent_label"]
            + " "
            + filtered["description"]
            + " "
            + filtered["include_keywords"]
            + " "
            + filtered["exclude_keywords"]
        ).str.lower()
        filtered = filtered[searchable.str.contains(query_lower, regex=False)]

    return filtered.reset_index(drop=True)


def render_metric_row(df: pd.DataFrame, filtered: pd.DataFrame) -> None:
    high_count = int((filtered["confidence"] == "high").sum())
    medium_count = int((filtered["confidence"] == "medium").sum())
    low_count = int((filtered["confidence"] == "low").sum())

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Visible labels", len(filtered), delta=f"of {len(df)}")
    col2.metric("High confidence", high_count)
    col3.metric("Medium confidence", medium_count)
    col4.metric("Low confidence", low_count)


def render_grid(filtered: pd.DataFrame) -> None:
    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        column_config={
            "image": st.column_config.ImageColumn("Image", width="small"),
            "cluster_id": st.column_config.NumberColumn("Cluster", width="small"),
            "taxonomy_node_id": st.column_config.TextColumn("Taxonomy node", width="medium"),
            "label": st.column_config.TextColumn("Label", width="medium"),
            "parent_label": st.column_config.TextColumn("Parent", width="medium"),
            "confidence": st.column_config.TextColumn("Confidence", width="small"),
            "description": st.column_config.TextColumn("Description", width="large"),
            "include_keywords": st.column_config.TextColumn("Include keywords", width="large"),
            "exclude_keywords": st.column_config.TextColumn("Exclude keywords", width="large"),
            "cluster_column": st.column_config.TextColumn("Source column", width="small"),
        },
    )


def render_details(filtered: pd.DataFrame, images_by_cluster: dict[int, list[str]]) -> None:
    if filtered.empty:
        st.info("No labels match the selected filters.")
        return

    st.subheader("Label Details")
    selected_cluster = st.selectbox(
        "Select a cluster",
        filtered["cluster_id"].tolist(),
        format_func=lambda cluster_id: f"Cluster {cluster_id}",
    )
    row = filtered[filtered["cluster_id"] == selected_cluster].iloc[0]

    st.markdown(f"### {row['label']}")
    st.caption(f"{row['parent_label']} · {row['taxonomy_node_id']} · {row['confidence']} confidence")
    st.write(row["description"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Include keywords**")
        st.write(row["include_keywords"])
    with col2:
        st.markdown("**Exclude keywords**")
        st.write(row["exclude_keywords"])

    image_urls = images_by_cluster.get(int(selected_cluster), [])
    if image_urls:
        st.markdown("**Representative images**")
        image_columns = st.columns(min(len(image_urls), 6))
        for column, image_url in zip(image_columns, image_urls):
            column.image(image_url, use_container_width=True)


def build_product_dataframe(samples: pd.DataFrame, labels_df: pd.DataFrame) -> pd.DataFrame:
    products = samples.copy()
    label_lookup = labels_df.set_index("cluster_id")[
        ["label", "parent_label", "confidence", "taxonomy_node_id", "description"]
    ]

    products = products.join(label_lookup, on="labeling_cluster_id", rsuffix="_label")
    products["image_url"] = products["images"].apply(extract_image_url)
    products["product_description"] = products["description"].fillna("").astype(str)
    products["title"] = products["title"].fillna("").astype(str)
    products["price"] = products["price"].fillna("").astype(str)
    return products


def normalize_labeled_products(products: pd.DataFrame, cluster_column: str) -> pd.DataFrame:
    products = products.copy()
    products["labeling_cluster_id"] = products[cluster_column]
    products["label"] = products["taxonomy_label"]
    products["parent_label"] = products["taxonomy_parent_label"]
    products["confidence"] = products["taxonomy_confidence"]
    products["taxonomy_node_id"] = products["taxonomy_node_id"]
    products["image_url"] = products["images"].apply(extract_image_url)
    products["product_description"] = products["description"].fillna("").astype(str)
    products["title"] = products["title"].fillna("").astype(str)
    products["price"] = products["price"].fillna("").astype(str)
    return products


def apply_product_filters(products: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    st.sidebar.header("Categories")

    category_options = sorted(products["parent_label"].dropna().unique())
    selected_categories = []
    for index, category in enumerate(category_options):
        if st.sidebar.checkbox(category, value=index == 0):
            selected_categories.append(category)

    if not selected_categories:
        return products.iloc[0:0].copy(), "Medium"

    st.sidebar.header("Confidence")
    confidence_options = ["high", "medium", "low"]
    selected_confidence = []
    for confidence in confidence_options:
        if st.sidebar.checkbox(confidence.title(), value=True, key=f"confidence-{confidence}"):
            selected_confidence.append(confidence)

    st.sidebar.header("Cards")
    card_size = st.sidebar.slider(
        "Card size",
        min_value=1,
        max_value=3,
        value=1,
        format="%d",
        help="1 = compact, 3 = large",
    )
    card_size_label = {1: "Compact", 2: "Medium", 3: "Large"}[card_size]

    filtered = products[
        products["parent_label"].isin(selected_categories)
        & products["confidence"].isin(selected_confidence)
    ]
    return filtered.reset_index(drop=True), card_size_label


def card_layout(card_size: str) -> dict[str, int]:
    if card_size == "Large":
        return {"height": 420, "image_width": 180, "columns": 3, "title_chars": 100}
    if card_size == "Medium":
        return {"height": 340, "image_width": 130, "columns": 4, "title_chars": 82}
    return {"height": 275, "image_width": 92, "columns": 5, "title_chars": 62}


def render_product_card(product: pd.Series, layout: dict[str, int]) -> None:
    title = product["title"]
    title_chars = layout["title_chars"]
    short_title = title if len(title) <= title_chars else title[: title_chars - 3] + "..."

    with st.container(border=True, height=layout["height"]):
        if product["image_url"]:
            st.image(product["image_url"], width=layout["image_width"])
        else:
            st.caption("No image")

        st.markdown(f"**{short_title}**")
        st.caption(
            f"{product['parent_label']} · {product['label']} · "
            f"cluster {int(product['labeling_cluster_id'])} · {product['confidence']}"
        )

        if product["price"] and product["price"].lower() != "nan":
            st.caption(f"Price: {product['price']}")

        with st.expander("Description"):
            if product["product_description"] and product["product_description"].lower() != "nan":
                st.write(product["product_description"])
            else:
                st.write("No product description available.")


def render_product_cards(products: pd.DataFrame) -> None:
    if products.empty:
        st.info("No products match the selected filters.")
        return

    layout = card_layout(st.session_state.get("card_size", "Compact"))
    columns = st.columns(layout["columns"])
    for index, (_, product) in enumerate(products.iterrows()):
        with columns[index % layout["columns"]]:
            render_product_card(product, layout)


def main() -> None:
    st.set_page_config(page_title="Taxonomy Label Viewer", layout="wide")
    st.title("Taxonomy Label Viewer")
    st.caption("Choose a taxonomy category on the left, then review matching products as cards.")

    source_name = st.sidebar.radio("Label source", list(LABEL_SOURCES))
    source = LABEL_SOURCES[source_name]

    if source["type"] == "labeled_products":
        products = normalize_labeled_products(
            load_labeled_products(source["products"]),
            source["cluster_column"],
        )
        df = products[
            [
                "labeling_cluster_id",
                "taxonomy_node_id",
                "label",
                "parent_label",
                "confidence",
                "taxonomy_description",
            ]
        ].drop_duplicates("labeling_cluster_id")
        df = df.rename(
            columns={
                "labeling_cluster_id": "cluster_id",
                "taxonomy_description": "description",
            }
        )
        df["image"] = ""
        df["include_keywords"] = ""
        df["exclude_keywords"] = ""
        df["cluster_column"] = source["cluster_column"]
    else:
        labels = load_json(source["labels"])
        samples = load_samples(source["samples"])
        taxonomy = load_json(source["taxonomy"])
        images_by_cluster = sample_images_by_cluster(samples)
        df = labels_to_dataframe(labels, taxonomy, source["cluster_column"], images_by_cluster)
        products = build_product_dataframe(samples, df)

    filtered_products, card_size = apply_product_filters(products)
    st.session_state["card_size"] = card_size

    col1, col2, col3 = st.columns(3)
    col1.metric("Visible products", len(filtered_products))
    col2.metric("Total products", len(products))
    col3.metric("Taxonomy labels", len(df))

    st.subheader("Product Cards")
    render_product_cards(filtered_products)

    with st.expander("Show label grid"):
        render_grid(df)


if __name__ == "__main__":
    main()
