"""Entry point for ``python -m rfsn_v10.server``.

Runs the FastAPI inference server via uvicorn.
Environment variables:
    RFSN_HOST — bind host (default: 127.0.0.1)
    RFSN_PORT — bind port (default: 8000)
    RFSN_BACKEND — backend override (default: auto)
"""
from __future__ import annotations

from rfsn_v10.config import RFSNConfig

cfg = RFSNConfig.from_env()

from .app import create_app  # noqa: E402

app = create_app(cfg)

import uvicorn  # noqa: E402

uvicorn.run(app, host=cfg.server.host, port=cfg.server.port)
