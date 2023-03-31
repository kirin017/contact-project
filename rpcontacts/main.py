# -*- coding: utf-8 -*-
# rpcontacts/main.py

"""This module provides RP Contacts application."""

import sys

from PyQt6.QtWidgets import QApplication

from .database import createConnection
from .views import Window

def main():
    """RP contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the data base before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec()) 