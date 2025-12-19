from .types import Claims as Claims

class AuthlyClient:
    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        jwks_path: str = ...,
        algorithms: list[str] | None = None,
    ) -> None: ...
    def verify(self, token: str) -> Claims: ...
