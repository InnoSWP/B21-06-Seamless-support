#!/usr/bin/env python
import os
import sys
import subprocess


def main():
    files = ["telegram_sender.py", "telegram.py"]
    for file in files:
        subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoApp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
