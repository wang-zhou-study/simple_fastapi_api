from pydantic import BaseModel


class LogItem(BaseModel):

    title: str

    content: str

    author: str


class UpdateLogItem(BaseModel):

    title: str

    content: str

    author: str