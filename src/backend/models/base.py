"""Base Model for all existing models."""
import re
import time
from datetime import datetime
from typing import Any, Optional, Self

import pandas as pd
from pydantic_settings import SettingsConfigDict
from sqlalchemy import inspect
from sqlalchemy.orm import declared_attr
from sqlmodel import Field, SQLModel
from backend.common.log import BetrLogger

log = BetrLogger().setup_logger()

class Base(SQLModel):
    """Base Model for all existing models."""
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.fromtimestamp(time.time()))
    updated_at: datetime = Field(default_factory=lambda: datetime.fromtimestamp(time.time()))
    updated_by: Optional[str] = Field(default=None)
    deleted_at: Optional[datetime] = Field(sa_column_kwargs={'onupdate': datetime.now()})
    deleted_by: Optional[str] = Field(default=None)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub(r'([a-z\d])([A-Z])', r'\1_\2', cls.__name__).lower()
    


class BasesqlModel(SQLModel):
    """
    Base Model for all existing models.

    Attributes:
        model_config (SettingsConfigDict): Configuration for the model.
        created_at (datetime): The timestamp when the model instance was created.
        updated_at (datetime): The timestamp when the model instance was last updated.
        deleted_at (Optional[datetime]): The timestamp when the model instance was deleted (if applicable).

    Class Methods:
        populate(*args, **kwargs): Raises a NotImplementedError. Must be implemented in the subclass.
        primary_keys() -> DataFrame: Get the primary keys of the model.
        get_or_create(session, **kwargs) -> tuple[Self | Any, bool]: Get or create an instance of the model.
        save(session) -> Self: Save an instance of the model to the database.
        get(session, **kwargs) -> Self | Any: Get an instance of the model.
        validate_table_exists(engine, table_name) -> bool: Validate that a table exists in the database and has data with the name of the table.
        get_table(engine, table_name) -> DataFrame: Get a table from the database.
        validate_data(df) -> Any: Validate data using a DataValidationModel.
        get_table_data(engine, table_name) -> DataFrame: Get data from a table in the database.

    Examples:
        primary_keys = Model.primary_keys()
        instance, created = Model.get_or_create(session, **kwargs)
        instance = Model.save(session)
        instance = Model.get(session, **kwargs)
        table_exists = Model.validate_table_exists(engine, table_name)
        table = Model.get_table(engine, table_name)
        validated_data = Model.validate_data(df)
        table_data = Model.get_table_data(engine, table_name)
    """

    model_config = SettingsConfigDict(extra="allow", from_attributes=True,
                                      arbitrary_types_allowed=True, env_file='.env', env_file_encoding='utf-8')

    created_at: datetime = Field(
        default_factory=lambda: datetime.fromtimestamp(time.time()))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.fromtimestamp(time.time()))
    deleted_at: Optional[datetime] = Field(
        sa_column_kwargs={'onupdate': datetime.now()})

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub(r'([a-z\d])([A-Z])', r'\1_\2', cls.__name__).lower()

    @classmethod
    def populate(cls, *args, **kwargs):
        raise NotImplementedError(
            "populate method must be implemented in the subclass")

    @classmethod
    @property
    def primary_keys(cls):  # sourcery skip: inline-immediately-returned-variable
        """
        Get the primary keys of the model.

        Returns:
            DataFrame: A DataFrame containing the primary keys of the model.

        Examples:
            primary_keys = Model.primary_keys()
        """

        mapper = inspect(cls)
        primary_keys = [column.name for column in mapper.primary_key]
        primary_keys = cls.__table__.columns.keys()
        return primary_keys

    @classmethod
    def get_or_create(cls, session, **kwargs) -> tuple[Self | Any, bool]:
        """Get or create an instance of the model."""
        instance = session.query(cls).filter_by(**kwargs).first()
        created = False
        if instance is None:
            instance = cls(**kwargs)
            session.add(instance)
            session.commit()
            created = True
        return instance, created

    def save(self, session):
        """Save an instance of the model to the database."""
        session.add(self)
        session.commit()
        return self

    @classmethod
    def get(cls, session, **kwargs) -> Self | Any:
        """Get an instance of the model."""
        return session.query(cls).filter_by(**kwargs).first()

    @classmethod
    def validate_table_exists(cls, engine, table_name):
        """Validate that a table exists in the database and has data with the name of the table."""
        return engine.dialect.has_table(engine, table_name)

    @classmethod
    def get_table(cls, engine, table_name):
        """Get a table from the database."""
        return pd.read_sql_table(table_name, engine)

    @classmethod
    def validate_data(cls, df):
        """"""
        class DataValidationModel(Base):
            __root__: list[cls]

        try:
            df_dict = df.to_dict(orient='records')
            return DataValidationModel.model_validate(df_dict)
        except Exception as e:
            log.error(f"Error: {e}")
            return e

    @classmethod
    def get_table_data(cls, engine, table_name):
        """Get data from a table in the database."""
        return pd.read_sql_table(table_name, engine)
