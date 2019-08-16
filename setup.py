from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("Main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "SmartCane",
    options = options,
    version = "1.0",
    description = 'Bengala Inteligente',
    executables = executables
)