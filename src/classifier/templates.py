def to_text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(to_text(item) for item in value if to_text(item))
    return str(value).strip()


def build_text(row):
    title = to_text(row.get("title", ""))
    desc = to_text(row.get("description", ""))
    features = to_text(row.get("features", ""))
    details = to_text(row.get("details", ""))

    return f"""Product: {title}
    Features: {features}
    Details: {details}
    Description: {desc}
    """
