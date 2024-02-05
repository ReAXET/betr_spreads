#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Path config module for the fastapi backend."""

from __future__ import annotations

import os
from pathlib import Path

# Root directory path
ROOT_DIR = Path(__file__).resolve().parents[3]

# Backend directory path
BACKEND_DIR = Path(__file__).resolve().parents[1]

# Versions directory path
VERSIONS = Path(BACKEND_DIR, 'alembic', 'versions')

# Log directory path
LOGPATH = Path(BACKEND_DIR, 'logs')

# Data directory path
DATA_PATH = Path(BACKEND_DIR, 'data')

# NBA data directory path
NBA_DATA_PATH = Path(BACKEND_DIR, 'data', 'nba')

# NHL data directory path
NHL_DATA_PATH = Path(BACKEND_DIR, 'data', 'nhl')

# MLB data directory path
MLB_DATA_PATH = Path(BACKEND_DIR, 'data', 'mlb')

# NFL data directory path
NFL_DATA_PATH = Path(BACKEND_DIR, 'data', 'nfl')

# UFC data directory path
UFC_DATA_PATH = Path(BACKEND_DIR, 'data', 'ufc')

# DB directory path
DB_PATH = Path(BACKEND_DIR, 'database')

# API directory path
API_PATH = Path(BACKEND_DIR, 'api')

# Core directory path
CONFIG_PATH = Path(BACKEND_DIR, 'core')

# Models directory path
MODELS_PATH = Path(BACKEND_DIR, 'models')

# Scripts directory path
SCRIPTS_PATH = Path(BACKEND_DIR, 'scripts')

# Utils directory path
UTILS_PATH = Path(BACKEND_DIR, 'utils')
