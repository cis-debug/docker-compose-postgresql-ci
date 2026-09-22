"""
API Flask + PostgreSQL

Routes:
- GET /        : test simple (API up)
- GET /health  : test DB (SELECT 1)

Note: on sépare la logique "create_app" pour faciliter les tests.
"""

import os
import psycopg2
from flask import Flask, jsonify


def get_db_connection():
    """Crée une connexion PostgreSQL à partir des variables d'environnement."""
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=int(os.environ.get("DB_PORT", "5432")),
        dbname=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "appuser"),
        password=os.environ.get("DB_PASSWORD", "apppassword"),
    )


def create_app():
    """Factory Flask (plus testable qu'un app global)."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(message="API is running")

    @app.get("/health")
    def health():
        # Vérifie que PostgreSQL répond
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT 1;")
            cur.fetchone()
            cur.close()
            conn.close()
            return jsonify(status="ok", db="connected")
        except Exception as e:
            return jsonify(status="error", db="not connected", detail=str(e)), 500

    return app


if __name__ == "__main__":
    # Important dans Docker: host=0.0.0.0
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
