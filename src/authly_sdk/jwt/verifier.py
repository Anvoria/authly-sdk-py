from ..config import DEFAULT_ALGORITHMS
from jwt import PyJWK, PyJWKClient
import jwt
from ..exceptions import TokenExpiredError, TokenInvalidError
from ..types import Claims
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidAudienceError,
    InvalidIssuerError,
    InvalidSignatureError,
    PyJWTError,
)


class JWTVerifier:
    """
    Internal class for verifying JWT tokens using PyJWKClient.

    This class handles fetching public keys from a JWKS endpoint and
    performing the actual token verification and decoding.
    """

    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        jwks_url: str,
        algorithms: list[str] | None = None,
    ) -> None:
        """
        Initialize the JWT verifier.

        Args:
            issuer: The expected issuer (iss claim).
            audience: The expected audience (aud claim).
            jwks_url: The full URL to the JWKS endpoint.
            algorithms: List of allowed signing algorithms.
        """
        self._issuer = issuer
        self._audience = audience
        self._algorithms = algorithms or DEFAULT_ALGORITHMS

        self._jwks_client = PyJWKClient(jwks_url)

    def verify(self, token: str) -> Claims:
        """
        Verify the JWT token and return its claims.

        Args:
            token: The encoded JWT token string.

        Returns:
            Claims: The decoded claims from the token.

        Raises:
            TokenExpiredError: If the token's exp claim is in the past.
            TokenInvalidError: If the token is otherwise invalid.
        """
        try:
            signing_key = self.__get_signing_key(token)

            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=self._algorithms,
                audience=self._audience,
                issuer=self._issuer,
            )

            return Claims(*payload)
        except ExpiredSignatureError as e:
            raise TokenExpiredError("Token has expired") from e

        except (
            InvalidSignatureError,
            InvalidAudienceError,
            InvalidIssuerError,
        ) as e:
            raise TokenInvalidError("Token validation failed") from e

        except PyJWTError as e:
            raise TokenInvalidError("Invalid token") from e

    def __get_signing_key(self, token: str) -> PyJWK:
        """
        Retrieve the appropriate public key from the JWKS for the given token.
        """
        return self._jwks_client.get_signing_key_from_jwt(token)
