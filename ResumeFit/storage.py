import json
from ResumeFit.exceptions import EmptyFileError
from ResumeFit.models import Document

def load_txt_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    if not text.strip():
        raise EmptyFileError("File is empty")
    return Document(path, text)

def save_json_file(result, path="report.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(result.to_dict(), file, indent=4)
    print ("Report saved to", path)

