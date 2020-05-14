from functools import wraps
from libs.route.errors import BaseError
from libs.route.login_required import login_required
from flask import jsonify
from flask import Response
import json


def route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response_msg, status_code = func(*args, **kwargs)
        except BaseError as e:
            response_msg, status_code = e.json(), e.code
        return response_msg, status_code
    return wrapper

