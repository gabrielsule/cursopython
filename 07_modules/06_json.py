import json
from pathlib import Path

data = [
    {"id": 1, "descipcion": "lorem"},
    {"id": 2, "descipcion": "ipsum"}
]

ver = json.dumps(data)
Path("data.json").write_text(ver)
print(ver)

data = Path("data.json").read_text()
ver = json.loads(data)
print(ver)