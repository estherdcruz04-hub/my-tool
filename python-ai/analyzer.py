import ast
import subprocess

def analyze_code(file_path):
    errors = []

    # Syntax check
    try:
        with open(file_path, "r") as f:
            ast.parse(f.read())
    except SyntaxError as e:
        errors.append(str(e))

    # Pylint analysis
    result = subprocess.run(
        ["pylint", file_path, "--disable=all", "--enable=E"],
        capture_output=True,
        text=True
    )

    if result.stdout:
        errors.append(result.stdout)

    return errors
