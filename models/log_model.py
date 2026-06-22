from pydantic import BaseModel
from pydantic import Field

class LogItem(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=100
    )

    content: str = Field(
        min_length=1,
        max_length=1000
    )

    author: str = Field(
        min_length=2,
        max_length=30
    )

class UpdateLogItem(BaseModel):

    title: str

    content: str

    author: str