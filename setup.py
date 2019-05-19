import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_files": ["resources",  "README.md", "mbreplacer_diagram.png"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="mbreplacer",
      version="1.0-beta",
      description="Tool for replacing monkeyball levels in root from obj/mtl/config",
      options={"build_exe": build_exe_options},
      executables=[Executable("mbreplacer.py", base=base)])
