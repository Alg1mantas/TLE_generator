import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name="TLE",
    version="0.1",
    description="TLE_generator",
    options={"build_exe": build_exe_options},
    executables=[Executable("TLE.py", base=base)],
)