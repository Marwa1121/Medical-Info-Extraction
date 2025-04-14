from flask import Blueprint, request, jsonify
from .utils import extract_medical_details

medical_bp = Blueprint('medical', __name__)

@medical_bp.route('/process-medical-report', methods=['POST'])
def process_medical_report():
    report_text = request.json.get('report', '')
    if not report_text:
        return jsonify({"error": "Missing report content."}), 400

    result = extract_medical_details(report_text)
    return jsonify(result)
