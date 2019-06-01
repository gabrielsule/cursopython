import setuptools

setuptools.setup(
    name = "lorem ipsum",
    version = 1.0,
    long_description = "Nulla laboris commodo deserunt nulla.",
    packages = setuptools.find_packages(exclude = ["data", "test"])
)