from pathlib import Path

path = Path("c:\\code")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("c:\\code2")

for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir()]
print(paths)    