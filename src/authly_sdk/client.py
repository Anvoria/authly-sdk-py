from .config import DEFAULT_JWKS_PATH
from .jwt import JWTVerifier
from .types import Claims


class AuthlyClient:
    """
    A client for verifying Authly JWT tokens.

    This client handles the validation of tokens against a specific issuer and audience,
    fetching the public keys (JWKS) automatically.
    """

    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        jwks_path: str = DEFAULT_JWKS_PATH,
        algorithms: list[str] | None = None,
    ) -> None:
        """
        Initialize the Authly client.

        Args:
            issuer: The base URL of the identity provider (e.g., "https://auth.example.com").
            audience: The expected audience claim (aud) in the token.
            jwks_path: The path to the JWKS endpoint relative to the issuer. Defaults to "/.well-known/jwks.json".
            algorithms: A list of allowed signing algorithms. If None, defaults to ["RS256"].
        """
        self._issuer = issuer.rstrip("/")
        self._audience = audience
        self._jwks_path = jwks_path
        self._algorithms = algorithms

        self._verifier = JWTVerifier(
            issuer=self._issuer,
            audience=self._audience,
            jwks_url=f"{self._issuer}{self._jwks_path}",
            algorithms=self._algorithms,
        )

    def verify(self, token: str) -> Claims:
        """
        Verify a JWT token and return its decoded claims.

        This method verifies the token's signature using the provider's JWKS,
        and validates standard claims like expiration, issuer, and audience.

        Args:
            token: The encoded JWT token string.

        Returns:
            Claims: A dictionary-like object containing the token claims (e.g., sub, iss, aud).

        Raises:
            TokenExpiredError: If the token has expired.
            TokenInvalidError: If the token is invalid (e.g., bad signature, invalid audience).
        """
        return self._verifier.verify(token)
