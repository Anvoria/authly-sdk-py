from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ...client import AuthlyClient
from ...types import Claims
from ...exceptions import TokenExpiredError, TokenInvalidError


class AuthlyDep:
    """
    FastAPI dependency for Authly token verification.
    """

    _client: AuthlyClient

    def __init__(self, client: AuthlyClient):
        self._client = client

    def __call__(
        self,
        creds: Annotated[
            HTTPAuthorizationCredentials, Depends(HTTPBearer(auto_error=True))
        ],
    ) -> Claims:
        """
        Verify the token from the Authorization header.
        """
        token = creds.credentials
        try:
            return self._client.verify(token)
        except TokenExpiredError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except TokenInvalidError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
