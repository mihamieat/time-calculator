# -*- coding: utf-8 -*-
"""version 0.1.0"""

import click

from src.time_calculator.time_calculator import add_time


@click.command()
@click.option(
    "--time",
    "-t",
    prompt="Enter initial time in HH:MM AM format: ",
    help="Initial time in HH:MM AM format",
)
@click.option(
    "--duration",
    "-d",
    prompt="Enter duration you want to add to the time in HH:MM format: ",
    help="Duration time in HH:MM AM format",
)
@click.option(
    "--day",
    "-y",
    prompt="Enter the initial day of the week",
    help="The day of the week",
    required=False,
    default="",
    show_default=False,
)
def time_calculator(time, duration, day=None):
    """Time calculator CLI command."""
    click.echo(add_time(time, duration, day=day))


if __name__ == "__main__":
    # pylint: disable=E1120
    time_calculator()
