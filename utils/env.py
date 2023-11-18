def get_env(envName: str) -> str:
    import os
    env = os.getenv(envName)

    if env is None:
        raise Exception(f'Environment variable {envName} is not set.')

    return env
