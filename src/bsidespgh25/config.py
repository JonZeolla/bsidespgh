"""
Configuration management for bsidespgh25
"""

import logging
from argparse import ArgumentParser

from bsidespgh25 import (
    __project_name__,
    __version__,
    constants,
)

LOG = logging.getLogger(__name__)


def create_arg_parser() -> ArgumentParser:
    """Create an argument parser"""
    parser = ArgumentParser()

    parser.add_argument("--version", action="version", version=__version__)

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--debug",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        help="enable debug logging",
    )
    group.add_argument(
        "--verbose",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
        help="enable informational logging",
    )
    parser.set_defaults(loglevel=logging.WARNING)

    return parser


def get_args_config() -> dict:
    """Turn parse arguments into a config"""
    parser = create_arg_parser()
    return vars(parser.parse_args())


def setup_logging(loglevel: int = logging.WARNING) -> logging.Logger:
    """Setup logging

    Args:
        loglevel: Logging level to use

    Returns:
        Configured logger
    """
    logging.basicConfig(level="WARNING", format=constants.LOG_FORMAT)
    log = logging.getLogger(__project_name__)
    logging.getLogger().setLevel(loglevel)
    return log
