#### instalación de herramientas para el empaquetado y distribución
```
pip install setuptools wheel twine
```

#### empaquetado de la aplicación
```
python setup.py sdist bdist_wheel
```

#### subir la aplicación al repositorio
```
twine upload dist/*
```

