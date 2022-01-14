import typing as t
from functools import lru_cache
from pathlib import Path

from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    validator,
)


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
PROJECT_DIR = BASE_DIR.parent.parent


class Settings(BaseSettings):
    app_name: str = "Auth"
    api_v1_str: str = "/api/v1"

    https: bool = False

    secret_token: str = "GYctzupHZkyhhzGzcOXEGLfvIHmvStWuSqkqijmMTVUNIROohBTIHczEUwKRPCgo"  # /* cspell: disable-line */
    cookie_secure: t.Optional[bool] = None

    @validator("cookie_secure", always=True)
    def validate_cookie_secure(self, _, values: dict[str, t.Any]) -> bool:
        if values["https"] is True:
            return True
        return False

    backend_cors_origins: list[AnyHttpUrl] = [
        AnyHttpUrl(url="http://localhost:8080", scheme="http"),
        AnyHttpUrl(url="http://127.0.0.1:8000", scheme="http"),
    ]


@lru_cache
def get_settings() -> Settings:
    return Settings()
