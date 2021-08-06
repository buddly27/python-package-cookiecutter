# -*- coding: utf-8 -*-

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.command_line_interface }}" != "yes":
        remove_file("doc/command_line.rst")
        remove_file("source/{{ cookiecutter.package }}/__main__.py")
        remove_file("source/{{ cookiecutter.package }}/command_line.py")
        remove_file("test/unit/test_command_line.py")
