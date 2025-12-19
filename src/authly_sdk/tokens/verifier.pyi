from ..types import Claims
from jwt import PyJWK as PyJWK, PyJWKClient as PyJWKClient
from jwt.exceptions import (
    ExpiredSignatureError as ExpiredSignatureError,
    InvalidAudienceError as InvalidAudienceError,
    InvalidIssuerError as InvalidIssuerError,
    InvalidSignatureError as InvalidSignatureError,
    PyJWTError as PyJWTError,
)

class JWTVerifier:
    def __init__(
        self,
        *,
        issuer: str,
        audience: str,
        jwks_url: str,
        algorithms: list[str] | None = None,
    ) -> None: ...
    def verify(self, token: str) -> Claims: ...
