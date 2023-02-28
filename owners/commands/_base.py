from __future__ import annotations

from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from functools import cached_property
from typing import ClassVar, TextIO

from .._colors import Colors


@dataclass
class Command:
    name: ClassVar[str]
    args: Namespace
    stdout: TextIO

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--no-colors', action='store_true',
            help='disable colored output.',
        )

    def run(self) -> int:
        raise NotImplementedError

    def print(self, *args: str, end: str = '\n', sep: str = ' ') -> None:
        print(*args, file=self.stdout, end=end, sep=sep)

    @cached_property
    def colors(self) -> Colors:
        return Colors(disabled=self.args.no_colors)
