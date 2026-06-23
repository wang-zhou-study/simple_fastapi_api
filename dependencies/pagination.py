from fastapi import Query


def pagination_params(
    page: int = Query(
        1,
        ge=1
    ),
    size: int = Query(
        5,
        ge=1,
        le=50
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