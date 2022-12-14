from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from builder import build_query
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        data = BatchRequestParams().load(request.json)
    except ValidationError as e:
        return e.messages, 400

    result = None
    for query in data['queries']:
        result = build_query(cmd=query['cmd'], param=query['value'], data=result)

    return jsonify(result)
