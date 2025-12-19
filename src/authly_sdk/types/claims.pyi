from typing import NotRequired, TypedDict

class Claims(TypedDict):
    sub: str
    iss: str
    aud: str | list[str]
    exp: int
    iat: int
    sid: str
    permissions: dict[str, int]
    pver: NotRequired[int]
    scope: NotRequired[str]
