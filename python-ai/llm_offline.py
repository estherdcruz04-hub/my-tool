def convert_code(code):
    """
    Reliable Python 2 → Python 3 converter
    Preserves indentation
    """

    lines = code.split("\n")
    new_lines = []

    for line in lines:
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]

        # Convert print statement
        if stripped.startswith("print ") and not stripped.startswith("print("):
            content = stripped[6:]
            new_lines.append(f"{indent}print({content})")

        # Convert xrange → range
        elif "xrange(" in stripped:
            new_lines.append(indent + stripped.replace("xrange(", "range("))

        else:
            new_lines.append(line)

    return "\n".join(new_lines)

