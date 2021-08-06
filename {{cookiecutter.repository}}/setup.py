# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_PATH = os.path.join(ROOT_PATH, "source")
README_PATH = os.path.join(ROOT_PATH, "README.rst")

PACKAGE_NAME = "{{ cookiecutter.package }}"

# Read version from source.
with open(
    os.path.join(SOURCE_PATH, PACKAGE_NAME, "_version.py")
) as _version_file:
    VERSION = re.match(
        r".*__version__ = \"(.*?)\"", _version_file.read(), re.DOTALL
    ).group(1)

# Compute dependencies.
INSTALL_REQUIRES = [
    {%- if cookiecutter.command_line_interface == 'yes' %}
    "click >= 7, < 8",
    {%- endif %}
]

DOC_REQUIRES = [
    "sphinx >= 1.8, < 2",
    {%- if cookiecutter.command_line_interface == 'yes' %}
    "sphinx-click >= 1.2.0, < 2",
    {%- endif %}
    "sphinx_rtd_theme >= 0.1.6, < 1",
    "lowdown >= 0.2.0, < 2"
]

TEST_REQUIRES = [
    "pytest-runner >= 2.7, < 3",
    "pytest >= 4, < 5",
    "pytest-mock >= 1.2, < 2",
    "pytest-xdist >= 1.18, < 2",
    "pytest-cov >= 2, < 3",
]


# Execute setup.
setup(
    name="{{ cookiecutter.repository }}",
    version=VERSION,
    description="{{ cookiecutter.description }}",
    long_description=open(README_PATH).read(),
    url="https://github.com/{{ cookiecutter.github_group }}/{{ cookiecutter.repository }}",
    keywords="",
    author="{{ cookiecutter.author }}",
    packages=find_packages(SOURCE_PATH),
    package_dir={
        "": "source"
    },
    include_package_data=True,
    {%- if cookiecutter.python_version == '==2.7.*' %}
    python_requires="==2.7.*",
    {%- elif cookiecutter.python_version == '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5*' %}
    python_requires = (
        ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5*"
    ),
    {%- elif cookiecutter.python_version == '>=3.6' %}
    python_requires = ">=3.6.*",
    {%- endif %}
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    extras_require={
        "doc": DOC_REQUIRES,
        "test": TEST_REQUIRES,
        "dev": DOC_REQUIRES + TEST_REQUIRES
    },
    zip_safe=False,
    {%- if cookiecutter.command_line_interface == 'yes' %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.repository }} = {{ cookiecutter.package }}.__main__:main"
        ]
    },
    {%- endif %}
    classifiers=[
        "Programming Language :: Python",
        {%- if cookiecutter.python_version in ['>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5*'] %}
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        {%- endif %}
        {%- if cookiecutter.python_version in ['>=3.6', '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5*'] %}
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        {%- endif %}
        {%- if cookiecutter.architecture == 'noarch' %}
        "Operating System :: OS Independent",
        {%- elif cookiecutter.architecture in ['linux'] %}
        "Operating System :: POSIX ",
        "Operating System :: POSIX :: Linux ",
        {%- elif cookiecutter.architecture == 'osx' %}
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        {%- elif cookiecutter.architecture == 'windows10' %}
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        {%- endif %}
    ]
)
