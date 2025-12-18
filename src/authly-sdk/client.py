from .config import DEFAULT_JWKS_PATH

class AuthlyClient:
    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        jwks_path: str = DEFAULT_JWKS_PATH
    ) -> None:
        self._issuer = issuer.rstrip("/")
        self._audience = audience
        self._jwks_path = jwks_path