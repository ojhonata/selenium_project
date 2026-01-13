import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

from typing import Optional

from dotenv import load_dotenv
import os

load_dotenv()

__engine: Optional[Engine] = None

def create_engine() -> Engine:
    global __engine

    if __engine:
        return __engine

    conn_str = os.environ['database_url']
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine

def cerate_session() -> Session:
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()
    return session

def create_table() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models
    #ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)