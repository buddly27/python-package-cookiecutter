# -*- coding: utf-8 -*-

import {{ cookiecutter.package }}.command_line


def main():
    """Execute main command line interface passing command line arguments."""
    {{ cookiecutter.package }}.command_line.main(prog_name="{{ cookiecutter.repository }}")


if __name__ == "__main__":
    main()
