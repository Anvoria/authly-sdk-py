from .config import DEFAULT_JWKS_PATH
from .jwt import JWTVerifier
from .types import Claims


class AuthlyClient:
    def __init__(
        self, *, issuer: str, audience: str, jwks_path: str = DEFAULT_JWKS_PATH
    ) -> None:
        self._issuer = issuer.rstrip("/")
        self._audience = audience
        self._jwks_path = jwks_path

        self._verifier = JWTVerifier(
            issuer=self._issuer,
            audience=self._audience,
            jwks_url=f"{self._issuer}{self._jwks_path}",
            algorithms=self._algorithms,
        )

    def verify(self, token: str) -> Claims:
        """
        Verify a token and return the claims.
        """
        return self._verifier.verify(token)