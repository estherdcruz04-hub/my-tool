import autopep8

def clean_code(code):
    return autopep8.fix_code(code, options={"aggressive": 1})


