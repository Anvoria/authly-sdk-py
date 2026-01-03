from ...client import AuthlyClient as AuthlyClient
from ...exceptions import (
    TokenExpiredError as TokenExpiredError,
    TokenInvalidError as TokenInvalidError,
)
from .schemas import AuthlyUser as AuthlyUser
from fastapi import Depends as Depends
from fastapi.security import (
    HTTPAuthorizationCredentials as HTTPAuthorizationCredentials,
    HTTPBearer as HTTPBearer,
)
from typing import Annotated

class AuthlyDep:
    def __init__(self, client: AuthlyClient) -> None: ...
    def __call__(
        self, creds: Annotated[HTTPAuthorizationCredentials, None]
    ) -> AuthlyUser: ...
