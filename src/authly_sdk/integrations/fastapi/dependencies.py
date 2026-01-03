from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ...client import AuthlyClient
from ...exceptions import TokenExpiredError, TokenInvalidError
from .schemas import AuthlyUser


class AuthlyDep:
    """
    FastAPI dependency for Authly token verification.

    This class serves as a callable dependency that validates Bearer tokens
    and returns a Pydantic model representing the authenticated user.

    Attributes:
        _client (AuthlyClient): The initialized Authly client used for verification.
    """

    _client: AuthlyClient

    def __init__(self, client: AuthlyClient):
        """
        Initialize the Authly dependency.

        Args:
            client: An instance of AuthlyClient configured with the correct issuer and audience.
        """
        self._client = client

    def __call__(
        self,
        creds: Annotated[
            HTTPAuthorizationCredentials, Depends(HTTPBearer(auto_error=True))
        ],
    ) -> AuthlyUser:
        """
        Verify the token extracted from the Authorization header.

        This method is called by FastAPI when the dependency is injected.
        It handles the extraction of the token from the Bearer header,
        verifies it using the AuthlyClient, and converts the claims into
        an AuthlyUser model.

        Args:
            creds: The HTTP authorization credentials automatically injected by FastAPI.

        Returns:
            AuthlyUser: A Pydantic model containing the verified user claims.

        Raises:
            HTTPException:
                - 401 Unauthorized if the token is expired.
                - 401 Unauthorized if the token is invalid (bad signature, wrong audience, etc.).
        """
        token = creds.credentials
        try:
            claims = self._client.verify(token)
            return AuthlyUser(**claims)
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
