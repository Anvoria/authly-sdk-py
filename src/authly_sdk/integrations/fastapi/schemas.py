from typing import ClassVar
from pydantic import BaseModel, ConfigDict


class AuthlyUser(BaseModel):
    """
    Pydantic model representing an authenticated user.
    """

    sub: str
    iss: str
    aud: str | list[str]
    exp: int
    iat: int
    sid: str
    permissions: dict[str, int]
    pver: int | None = None
    scope: str | None = None

    model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow")
