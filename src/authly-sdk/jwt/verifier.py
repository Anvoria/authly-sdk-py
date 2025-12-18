from ..config import DEFAULT_ALGORITHMS
from jwt import PyJWKClient


class JWTVerifier:
    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        jwks_url: str,
        algorithms: list[str] | None = None,
    ) -> None:
        self._issuer = issuer
        self._audience = audience
        self._algorithms = algorithms or DEFAULT_ALGORITHMS

        self._jwks_client = PyJWKClient(jwks_url)
