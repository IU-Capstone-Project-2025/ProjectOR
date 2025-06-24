from os import getenv

# DATABASE_URL = (
#     f"postgresql+asyncpg://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@"
#     f"{getenv('POSTGRES_HOST')}:{getenv('POSTGRES_PORT')}/{getenv('POSTGRES_DB')}"
# )

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/projector"
