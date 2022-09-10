from distutils.core import setup
import py2exe
import tkinter as tk
from datetime import datetime
import math

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "main.py"}],
    zipfile = None,
)