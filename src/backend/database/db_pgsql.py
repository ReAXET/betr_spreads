"""Main Database Connection for Postgres Database."""

# Standard Library
from typing import Any, Dict, List, Sequence
from sqlmodel import create_engine, Session, Table, MetaData, Column, text
from sqlalchemy import Table, MetaData, Column, Engine, Row

from backend.common.log import BetrLogger
from backend.core.config import settings

log = BetrLogger().setup_logger()

def create_engine_and_session() -> tuple[Engine, Session]:
    """Create and return a new engine and session."""
    engine = create_engine(settings.DB_URL, echo=True, future=True, pool_pre_ping=True, pool_size=20, max_overflow=0, pool_recycle=3600, pool_timeout=30, pool_reset_on_return='rollback')
    session = Session(engine)
    return engine, session


def create_database(engine: Engine, database_name: str) -> None:
    """Create a new database."""
    with engine.connect() as connection:
        statement = f"CREATE DATABASE {database_name}"
        connection.execute(text(statement))
        log.info(f"Database {database_name} created.")
        connection.close()



def create_table(engine: Engine, table_name: str, columns: List[Dict[str, Any]]) -> Table:
    """Create a new table in the database."""
    metadata = MetaData()
    table = Table(table_name, metadata)
    for column in columns:
        table.append_column(Column(column['name'], column['type'], primary_key=column['primary_key'], nullable=column['nullable']))
    metadata.create_all(engine)
    return table


def drop_table(engine: Engine, table_name: str) -> None:
    """Drop a table from the database."""
    metadata = MetaData()
    table = Table(table_name, metadata)
    table.drop(engine)


def get_table(engine: Engine, table_name: str) -> Table:
    """Get a table from the database."""
    metadata = MetaData()
    return Table(table_name, metadata, autoload_with=engine)


def get_table_data(engine: Engine, table_name: str) -> Sequence[Row[Any]]:
    """Get data from a table in the database."""
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {table_name}"))
        return result.fetchall()    


def validate_table_exists(engine: Engine, table_name: str) -> bool:
    """Validate that a table exists in the database and has data with the name of the table."""
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {table_name}"))
        return bool(result.fetchall())
    



