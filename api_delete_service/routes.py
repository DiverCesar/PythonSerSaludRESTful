import os
import requests
from flask import Blueprint, jsonify

DB_SERVICE_URL = os.environ.get("DB_SERVICE_URL", "http://localhost:5001")

delete_bp = Blueprint("delete_service", __name__)


@delete_bp.route("/api/ser-salud/patient/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    try:
        resp = requests.delete(
            f"{DB_SERVICE_URL}/internal/patient/{patient_id}",
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@delete_bp.route("/api/ser-salud/doctor/<int:doctor_id>", methods=["DELETE"])
def delete_doctor(doctor_id):
    try:
        resp = requests.delete(
            f"{DB_SERVICE_URL}/internal/doctor/{doctor_id}",
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@delete_bp.route("/api/ser-salud/appointment/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    try:
        resp = requests.delete(
            f"{DB_SERVICE_URL}/internal/appointment/{appointment_id}",
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503
