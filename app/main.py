def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"], "message": error["text"], "name": error["code"], "source": "flake8" }

# result = {}
#    for i, v in error.items():
#        if i == "line_number":
#            result["line"] = v
#        elif i == "column_number":
#            result["column"] = v
#        elif i == "text":
#            result["message"] = v
#        elif i == "code":
#            result["name"] = v
#    result["source"] = "flake8"
#    return result


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(i) for i in errors], "path": file_path, "status": "failed" if errors else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(i, linter_report[i]) for i in linter_report]
