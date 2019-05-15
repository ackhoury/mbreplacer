import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "sys", "PyQt5", "qtpy"], "include_files": ["resources"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="mbtool",
      version="0.0.1",
      description="Tool for importing monkeyball levels config into root.",
      options={"build_exe": build_exe_options},
      executables=[Executable("mbtool.py", base=base)])