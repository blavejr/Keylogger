import cx_Freeze

executables = [cx_Freeze.Executable("main.pyw")]

cx_Freeze.setup(
    version="1.2",
    name="Watch",
    options={"build_exe":{"packages":["os", "getpass"]}},
    description="Windows system operations",
    executables=executables
)