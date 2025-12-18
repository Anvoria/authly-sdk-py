class AuthlyError(Exception):
    """
    Base exception for all Authly errors.

    Every exception in the library should inherit from this class.
    """

    pass


class TokenError(AuthlyError):
    """
    Base exception for all token errors.
    """

    pass


class TokenInvalidError(TokenError):
    """
    Exception raised when a token is invalid:
    - bad signature
    - bad format
    - bad iss / aud
    """

    pass


class TokenExpiredError(TokenError):
    """
    Exception raised when a token is expired.
    """

    pass
