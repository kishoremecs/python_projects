"""
Hello World package.
A simple example of a Flask-based Python project.
"""

from .main import get_greeting, app

__version__ = "0.1.0"
__all__ = ["get_greeting", "app"]