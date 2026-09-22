"""
conftest.py
Pytest charge ce fichier automatiquement.

Objectif:
- ajouter la racine du projet dans sys.path
- permettre: from api.app import create_app
même quand pytest est lancé depuis un autre contexte (CI).
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
