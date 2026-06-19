from fastapi import HTTPException


class LogNotFoundException(HTTPException):

    def __init__(self):

        super().__init__(
            status_code=404,
            detail="日志不存在"
        )