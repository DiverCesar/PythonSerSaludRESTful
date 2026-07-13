import os
import requests
from flask import Blueprint, request, jsonify
from datetime import datetime

DB_SERVICE_URL = os.environ.get("DB_SERVICE_URL", "http://localhost:5001")

post_bp = Blueprint("post_service", __name__)


@post_bp.route("/api/ser-salud/patient", methods=["POST"])
def create_patient():
    try:
        data = request.get_json()
        data.setdefault("isActive", True)
        resp = requests.post(
            f"{DB_SERVICE_URL}/internal/patient",
            json=data,
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@post_bp.route("/api/ser-salud/doctor", methods=["POST"])
def create_doctor():
    try:
        data = request.get_json()
        data.setdefault("isActive", True)
        resp = requests.post(
            f"{DB_SERVICE_URL}/internal/doctor",
            json=data,
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@post_bp.route("/api/ser-salud/appointment", methods=["POST"])
def create_appointment():
    try:
        data = request.get_json()
        data.setdefault("status", "pending")
        data.setdefault("createdAt", datetime.now().isoformat())
        data.setdefault("isActive", True)
        resp = requests.post(
            f"{DB_SERVICE_URL}/internal/appointment",
            json=data,
            timeout=5,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503


@post_bp.route("/api/ser-salud/seed", methods=["POST"])
def seed_database():
    try:
        resp = requests.post(
            f"{DB_SERVICE_URL}/internal/seed",
            timeout=10,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Database service unavailable"}), 503
