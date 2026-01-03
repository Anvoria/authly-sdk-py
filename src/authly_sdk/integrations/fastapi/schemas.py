from typing import ClassVar
from pydantic import BaseModel, ConfigDict


class AuthlyUser(BaseModel):
    """
    Pydantic model representing an authenticated user.

    This model wraps the standard and custom claims returned by Authly,
    providing type-safe access via dot notation (e.g., `user.sub`, `user.permissions`).

    Attributes:
        sub (str): Subject identifier - the unique ID of the user.
        iss (str): Issuer identifier - the URL of the identity provider.
        aud (str | list[str]): Audience(s) for which the token is intended.
        exp (int): Expiration time (Unix timestamp).
        iat (int): Issued at time (Unix timestamp).
        sid (str): Session ID identifier.
        permissions (dict[str, int]): Dictionary of permissions granted to the user,
            where keys are resource names and values are permission levels.
        pver (int | None): Permission version. Defaults to None.
        scope (str | None): Space-separated list of scopes. Defaults to None.
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
