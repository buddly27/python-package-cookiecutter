# -*- coding: utf-8 -*-

from click.testing import CliRunner

from {{ cookiecutter.package }}.command_line import main


def test_with_defaults():
    """Command executes successfully with defaults."""
    runner = CliRunner()
    result = runner.invoke(main, ["fix_me"])
    assert result.exit_code == 0
    assert not result.exception
