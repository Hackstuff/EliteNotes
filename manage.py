#!/usr/bin/env python
import os
import sys

PROJECT_NAME = 'EliteNotes'
ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.join(ROOT, PROJECT_NAME)
USE_SETTINGS = 'settings_local.py'

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EliteNotes.settings")

    if os.path.isfile(os.path.join(PROJECT, USE_SETTINGS)):
        os.environ["DJANGO_SETTINGS_MODULE"] = PROJECT_NAME + ".settings_local"
    else:
        os.environ["DJANGO_SETTINGS_MODULE"] = PROJECT_NAME + ".settings"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
