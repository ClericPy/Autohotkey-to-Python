from setuptools import setup, find_packages
import sys
import platform
"""
linux:
rm -rf "dist/*";rm -rf "build/*";python3 setup.py bdist_wheel;twine upload "dist/*;rm -rf "dist/*";rm -rf "build/*""
win32-git-bash:
rm -rf dist;rm -rf build;python3 setup.py bdist_wheel;twine upload "dist/*";rm -rf dist;rm -rf build;rm -rf ichrome.egg-info
"""

version = '0.0.1'
if sys.version_info < (3, 6):
    sys.exit("pypinfo requires Python 3.6+")

if 'windows' not in platform.platform().lower():
    sys.exit("pypinfo requires Windows platform")
py_version = sys.version_info
with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="goahk",
    version=version,
    keywords=("autohotkey"),
    description="run autohotkey code in python with autohotkey.dll",
    license="MIT License",
    install_requires=[],
    long_description=README,
    long_description_content_type="text/markdown",
    py_modules=["goahk"],
    author="ClericPy",
    author_email="clericpy@gmail.com",
    url="https://github.com/ClericPy/Autohotkey-to-Python",
    packages=find_packages(),
    platforms="windows",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
