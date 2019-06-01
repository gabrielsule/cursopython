from pathlib import Path
from time import ctime
import shutil

path = Path("c:\\code\\data.json")

# path.exist()
# path.rename("data.txt")
# path.write_text("{}")
# path.unlink()

print(path.stat())
print(ctime(path.stat().st_ctime))
print(path.read_text())

source = Path("c:\\code\\data.json")
target = Path() / "data.txt"

# target.write_text(source.read_text())
shutil.copy(source, target)
