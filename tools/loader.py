import os
import sys

folder_names = ["61c-tools", "tools", "sp21-tools", "."]
paths = []
if "CS61C_TOOLS_DIR" in os.environ:
    paths.append(os.environ["CS61C_TOOLS_DIR"])
for depth in range(5):
    for folder_name in folder_names:
        paths.append(os.path.join("../" * depth, folder_name))
for path in paths:
    bootstrap_path = os.path.join(path, "61c_tools.py")
    if os.path.isfile(bootstrap_path):
        program_name = os.path.basename(sys.modules["__main__"].__file__)
        os.execv(sys.executable, ["python", bootstrap_path, program_name] + sys.argv[1:])
        raise Exception("Failed to start program")
raise Exception("Could not find your 61c-tools install")
