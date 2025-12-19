# Authly Python SDK

[![PyPI version](https://img.shields.io/pypi/v/authly-sdk.svg)](https://pypi.org/project/authly-sdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/authly-sdk.svg)](https://pypi.org/project/authly-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight and secure Python library for building authentication systems using [Authly](https://github.com/Anvoria/authly). This SDK provides simple tools to verify JWT tokens against Authly's identity provider.

## Installation

Install using `pip`:

```bash
pip install authly-sdk
```

Or using `uv`:

```bash
uv add authly-sdk
```

## Quick Start

```python
from authly_sdk import AuthlyClient, TokenInvalidError, TokenExpiredError

# 1. Initialize the client
client = AuthlyClient(
    issuer="https://auth.example.com",
    audience="your-api-identifier"
)

# 2. Verify a token
try:
    token = "eyJhbGciOiJSUzI1NiIs..."
    claims = client.verify(token)
    
    # Access standard and custom claims with full IDE support
    print(f"User Subject: {claims['sub']}")
    print(f"Session ID: {claims['sid']}")
    print(f"Permissions: {claims['permissions']}")
    
except TokenExpiredError:
    print("The token has expired")
except TokenInvalidError as e:
    print(f"Invalid token: {e}")
```

## Advanced Configuration

You can customize the JWKS path or allowed algorithms:

```python
client = AuthlyClient(
    issuer="https://auth.example.com",
    audience="your-api",
    jwks_path="/.well-known/jwks.json",
    algorithms=["RS256"]
)
```

## Development

We use `uv` for dependency management.

```bash
# Install dev dependencies
uv sync --dev

# Run type checks
uv run basedpyright src

# Format code
uv run ruff format .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.