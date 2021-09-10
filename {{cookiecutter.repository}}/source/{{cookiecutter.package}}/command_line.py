# -*- coding: utf-8 -*-

import collections
import logging

import click

from {{ cookiecutter.package }} import __version__

#: Click default context for all commands.
CONTEXT_SETTINGS = dict(
    max_content_width=90,
    help_option_names=["-h", "--help"],
)

#: Available levels with corresponding labels ordered by severity.
LEVEL_MAPPING = collections.OrderedDict([
    ("debug", logging.DEBUG),
    ("info", logging.INFO),
    ("warning", logging.WARNING),
    ("error", logging.ERROR),
])


@click.command(
    context_settings=CONTEXT_SETTINGS
)
@click.version_option(version=__version__)
@click.option(
    "-v", "--verbosity",
    help="Set the logging output verbosity.",
    type=click.Choice(LEVEL_MAPPING.keys()),
    default="info"
)
def main(**kwargs):
    """{{ cookiecutter.project }} command line interface."""
    logging.basicConfig(level=LEVEL_MAPPING[kwargs["verbosity"]])

    logger = logging.getLogger(__name__ + ".main")
    logger.info("Hello from {{ cookiecutter.project }}!")
