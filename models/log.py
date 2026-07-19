from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Log(Base):

    __tablename__ = "logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String)

    content = Column(String)

    author = Column(String)

    created_at = Column(String)