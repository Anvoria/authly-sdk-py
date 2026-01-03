from pydantic import BaseModel, ConfigDict
from typing import ClassVar

class AuthlyUser(BaseModel):
    sub: str
    iss: str
    aud: str | list[str]
    exp: int
    iat: int
    sid: str
    permissions: dict[str, int]
    pver: int | None
    scope: str | None
    model_config: ClassVar[ConfigDict]
