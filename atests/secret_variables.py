try:
    from robot.api.types import Secret
    DB_PASSWORD = Secret("password")
    PASSWORD_AS_SECRET = Secret("passw0rd")
    NEW_PASSWORD_AS_SECRET = Secret("P@$$w0rd")
except ImportError:
    DB_PASSWORD = str("password")  # type: ignore[assignment]
    PASSWORD_AS_SECRET = str("passw0rd")  # type: ignore[assignment]
    NEW_PASSWORD_AS_SECRET = str("P@$$w0rd")  # type: ignore[assignment]
