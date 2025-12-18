from typing import NotRequired, TypedDict


class Claims(TypedDict):
    """
    Decoded JWT claims found in an Authly token.

    This dictionary contains both standard OIDC claims and Authly-specific claims
    like session ID (sid) and permissions.
    """

    sub: str
    """Subject identifier - the unique ID of the user."""

    iss: str
    """Issuer identifier - the URL of the identity provider."""

    aud: str | list[str]
    """Audience(s) for which the token is intended."""

    exp: int
    """Expiration time (Unix timestamp)."""

    iat: int
    """Issued at time (Unix timestamp)."""

    sid: str
    """Session ID identifier."""

    permissions: dict[str, int]
    """Dictionary of permissions granted to the user, where keys are resource names and values are permission levels."""

    pver: NotRequired[int]
    """Protocol version."""

    scope: NotRequired[str]
    """Space-separated list of scopes."""
