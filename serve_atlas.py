from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

import fire


ATLAS_APPS_DIR = Path("data/atlas/apps")


def serve(app: str = "title_jina-embeddings-v5-text-small", port: int = 8080):
    app_dir = ATLAS_APPS_DIR / app
    if not app_dir.exists():
        available = ", ".join(path.name for path in sorted(ATLAS_APPS_DIR.iterdir()))
        raise ValueError(f"Unknown Atlas app '{app}'. Available apps: {available}")

    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(
        *args,
        directory=str(app_dir),
        **kwargs,
    )
    server = ThreadingHTTPServer(("localhost", port), handler)
    print(f"Serving {app_dir} at http://localhost:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    fire.Fire(serve)
