from fastapi import Query
from config import (
    DEFAULT_PAGE_SIZE,
    MAX_PAGE_SIZE
)

def pagination_params(
    page: int = Query(
        1,
        ge=1
    ),
    size: int = Query(
    DEFAULT_PAGE_SIZE,
    ge=1,
    le=MAX_PAGE_SIZE
    ),
    order: str = Query(
        "DESC"
    )
):

    if order not in [
        "ASC",
        "DESC"
    ]:
        order = "DESC"

    return {
        "page": page,
        "size": size,
        "order": order
    }