import os
from functools import cached_property, lru_cache
from typing import Literal, Union

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from backend.core.path_config import LOGPATH

# Load .env file
load_dotenv()


class Settings(BaseSettings):

    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=('.env', '.env.prod'), env_file_encoding='utf-8', extra='allow')

    # Environment Config
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')

    # DB Postgres Config
    DB_HOST: str = os.getenv('DB_HOST', 'localhost')
    DB_PORT: Union[str, int] = os.getenv('DB_PORT', 5432)
    DB_USER: str = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'postgres')
    DB_NAME: str = os.getenv('DB_NAME', 'postgres')
    DB_ECHO: Union[str, bool] = os.getenv('DB_ECHO', False) == 'True'
    DB_URL: str = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'  # noqa

    # SQLALCHEMY Config
    ASQLALCHEMY_DATABASE_URL: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'  # noqa
    SQLALCHEMY_DATABASE_URL: str = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'  # noqa

    # Redis Config
    REDIS_HOST: str = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT: Union[str, int] = os.getenv('REDIS_PORT', 6379)
    REDIS_DB: Union[int, str] = os.getenv('REDIS_DB', 0)
    REDIS_PASSWORD: str = os.getenv('REDIS_PASSWORD', '')

    # Celery Config
    CELERY_REDIS_HOST: str = os.getenv('CELERY_REDIS_HOST', 'localhost')
    CELERY_REDIS_PORT: Union[str, int] = os.getenv('CELERY_REDIS_PORT', 6379)
    CELERY_REDIS_PASSWORD: str = os.getenv('CELERY_REDIS_PASSWORD', '')
    CELERY_BROKER_REDIS_DB: Union[str, int] = os.getenv(
        'CELERY_BROKER_REDIS_DB', 0)
    CELERY_BACKEND_REDIS_DB: Union[str, int] = os.getenv(
        'CELERY_BACKEND_REDIS_DB', 0)

    # RabbitMQ Config
    RABBITMQ_HOST: str = os.getenv('RABBITMQ_HOST', 'localhost')
    RABBITMQ_PORT: Union[str, int] = os.getenv('RABBITMQ_PORT', 5672)
    RABBITMQ_USER: str = os.getenv('RABBITMQ_USER', 'guest')
    RABBITMQ_PASSWORD: str = os.getenv('RABBITMQ_PASSWORD', 'guest')

    # Token
    TOKEN_SECRET_KEY: str = os.getenv('TOKEN_SECRET__KEY', 'secret')

    # FastAPI Config
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'betr API'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'An all in one sports betting machine learning platform desinged to help you make smarter bets.'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOC_URL: str | None = f'{API_V1_STR}/redoc'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'

    # Demo Mode
    # Only for development, only allows GET, OPTIONS requests
    DEMO_MODE: bool = False
    DEMO_MODE_EXCLUDE: set[tuple[str, str]] = {
        ('POST', f'{API_V1_STR}/auth/login'),
        ('POST', f'{API_V1_STR}/auth/logout'),
        ('GET', f'{API_V1_STR}/auth/captcha')
    }

    # Uvicorn Config
    UVICORN_HOST: Union[str, None] = 'localhost'
    UVICORN_PORT: Union[str, int] = os.getenv('PORT', 8000)
    UVICORN_RELOAD: bool = True

    # Static Files Server Config
    STATIC_FILES: bool = False

    # Location Parsing
    LOCATION_PARSE: Literal['online', 'offline', 'false'] = 'offline'

    # Limiters
    LIMITER_REDIS_PREFIX: str = 'betr_limiter'

    # Date Time Format
    DATETIME_TIMEZONE: str = 'America/Chicago'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    DATE_FORMAT: str = '%Y-%m-%d'
    TIME_FORMAT: str = '%H:%M:%S'

    # PGSQL

    DB_NAME: str = 'sports_db'
    DB_CHARSET: str = 'utf8mb4'

    # Redis
    REDIS_TIMEOUT: int = 5

    # Token
    TOKEN_ALGORITHM: str = 'HS256'
    TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # 7 days
    TOKEN_REFRESH_EXPIRE_SECONDS: int = 60 * 60 * 24 * 30  # 30 days
    TOKEN_URL_SWAGGER: str = f'{API_V1_STR}/auth/swagger_login'
    TOKEN_REDIS_PREFIX: str = 'betr_token'
    TOKEN_REFRESH_REDIS_PREFIX: str = 'betr_token_refresh'
    TOKEN_EXCLUDE: list[str] = [
        f'{API_V1_STR}/auth/login',

    ]

    # Captcha
    CAPTCHA_LOGIN_REDIS_PREFIX: str = 'betr_captcha_login'
    CAPTCHA_LOGIN_EXPIRE_SECONDS: int = 60 * 5  # 5 minutes

    # Logging
    LOG_STDOUT_FILENAME: str = 'betr_access.log'
    LOG_STDERR_FILENAME: str = 'betr_err.log'
    LOG_LEVEL: Literal['DEBUG', 'INFO',
                       'WARNING', 'ERROR', 'CRITICAL'] = 'INFO'
    LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    LOG_MAX_BYTES: int = 1024 * 1024 * 10  # 10 MB
    LOG_BACKUP_COUNT: int = 5
    LOG_PATH: str = str(LOGPATH)

    # Middleware
    MIDDLEWARE_CORS: bool = True
    MIDDLEWARE_GZIP: bool = True
    MIDDLEWARE_ACCESS: bool = False

    # RBAC Permission
    PERMISSON_MODE: Literal['casbin', 'role-menu'] = 'casbin'
    RBAC_REDIS_PREFIX: str = 'betr_rbac'

    # Casbin Auth
    CASBIN_EXCLUDE: set[tuple[str, str]] = {
        ('POST', f'{API_V1_STR}/auth/swagger_login'),
        ('POST', f'{API_V1_STR}/auth/login'),
        ('POST', f'{API_V1_STR}/auth/logout'),
        ('POST', f'{API_V1_STR}/auth/register'),
        ('GET', f'{API_V1_STR}/auth/captcha')
    }

    # Role Menu Auth
    ROLE_MENU_EXCLUDE: list[str] = [
        'sys:monitor:redis',
        'sys:monitor:server',
    ]

    # Opera Log
    OPERA_LOG_EXCLUDE: list[str] = [
        'favicon.ico',
        DOCS_URL,
        REDOC_URL,
        OPENAPI_URL,
        f'{API_V1_STR}/auth/swagger_login',
    ]

    OPERA_LOG_ENCRYPT: int = 1
    OPERA_LOG_ENCRYPT_INCLUDE: list[str] = [
        'password',
        'old_password',
        'new_password',
        'confirm_password',
    ]

    # IP Location
    IP_LOCATION_REDIS_PREFIX: str = 'betr_ip_location'
    IP_LOCATION_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # 7 days

    # CELERY
    CELERY_BROKER: Literal['rabbitmq', 'redis'] = 'redis'
    CELERY_BACKEND_REDIS_PREFIX: str = 'betr_celery'
    CELERY_BACKEND_REDIS_TIMEOUT: float = 5.0
    CELERY_BACKEND_REDIS_ORDERED: bool = True
    CELERY_BEAT_SCHEDULE_FILENAME: str = './logs/celery_beat_schedule'
    CELERY_BEAT_SCHEDULE: dict = {
        'task_async_betr': {
            'task': 'tasks.task_async_betr',
            'schedule': 5.0,

        },
    }

    @cached_property
    def CELERY_BROKER_URL(self) -> str:
        if self.CELERY_BROKER == 'rabbitmq':
            return f'amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}'
        elif self.CELERY_BROKER == 'redis':
            return f'redis://{self.CELERY_REDIS_HOST}:{self.CELERY_REDIS_PORT}/{self.CELERY_BROKER_REDIS_DB}'
        else:
            raise ValueError('Invalid CELERY_BROKER')

    @cached_property
    def CELERY_BACKEND_URL(self) -> str:
        if self.CELERY_BROKER == 'rabbitmq':
            return f'amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}'
        elif self.CELERY_BROKER == 'redis':
            return f'redis://{self.CELERY_REDIS_HOST}:{self.CELERY_REDIS_PORT}/{self.CELERY_BACKEND_REDIS_DB}'
        else:
            raise ValueError('Invalid CELERY_BROKER')


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
