#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration file for CodeSelect

This file contains default settings for CodeSelect that can be
overridden by command-line arguments.
"""

# Default directory to scan (relative to current directory)
DEFAULT_DIRECTORY = "."

# Default output format (txt, md, llm)
DEFAULT_FORMAT = "llm"

# Default output filename (None = auto-generate based on directory name)
DEFAULT_OUTPUT = None

# Skip the selection interface and include all files
SKIP_SELECTION = False

# Enable automatic copy to clipboard
COPY_TO_CLIPBOARD = False

# Default ignore patterns for files and directories
DEFAULT_IGNORE_PATTERNS = [
    '.git',
    '__pycache__',
    '*.pyc',
    '.DS_Store',
    '.idea',
    '.vscode',
    'node_modules',
    'venv',
    '.env',
    '*.log'
]
