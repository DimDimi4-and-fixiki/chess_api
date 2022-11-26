import typing as t

from fastapi import FastAPI

from app import build_app


def main_app(*args: t.Any, **kwargs: t.Any) -> FastAPI:
    app = build_app()

    return app
