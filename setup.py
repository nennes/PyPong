import cx_Freeze

executables = [cx_Freeze.Executable("PyPong.py")]

cx_Freeze.setup(
    name="Pong Madness",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables

    )