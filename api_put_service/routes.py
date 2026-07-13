import os
import requests
from flask import Blueprint, request, jsonify

DB_SERVICE_URL = os.environ.get("DB_SERVICE_URL", "http://localhost:5001")

put_bp = Blueprint("put_service", __name__)


@put_bp.route("/api/ser-salud/patient/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    try:
        data = request.get_json()
        data.pop("id", None)
        resp = requests.put(
            f"{DB_SERVICE_URL}/internal/patient/{patient_id}",
            json=data,
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@put_bp.route("/api/ser-salud/doctor/<int:doctor_id>", methods=["PUT"])
def update_doctor(doctor_id):
    try:
        data = request.get_json()
        data.pop("id", None)
        resp = requests.put(
            f"{DB_SERVICE_URL}/internal/doctor/{doctor_id}",
            json=data,
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@put_bp.route("/api/ser-salud/appointment/<int:appointment_id>", methods=["PUT"])
def update_appointment(appointment_id):
    try:
        data = request.get_json()
        data.pop("id", None)
        resp = requests.put(
            f"{DB_SERVICE_URL}/internal/appointment/{appointment_id}",
            json=data,
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503
