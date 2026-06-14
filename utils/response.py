def success_response(data=None, message="success"):

    return {
        "code": 200,
        "message": message,
        "data": data
    }


def error_response(message="error"):

    return {
        "code": 400,
        "message": message,
        "data": None
    }