# -*- coding: utf-8 -*-
"""version 0.1.0"""

import sys
import re

import click


def parse_clock(time_string):
    """Parse 12-hour clock format (ending in AM or PM)."""
    pattern = re.compile(
        r"\b(0?[1-9]|1[0-2]):(0?[0-9]|[1-5][0-9]) ([a, A]|[p, P])[m, M]\b"
    )
    match = pattern.search(time_string)
    try:
        wrong_value(match)
    except WrongInputError as e:
        click.echo(
            f"Error int the clock format. Should be HH:MM [AM|PM]: {e}"  # noqa
        )
        sys.exit(1)

    hours = match.group(1)
    minutes = match.group(2)
    am_pm = match.group(3)
    clock_dict = {
        "hour": int(hours),
        "min": int(minutes),
        "am_pm": am_pm.upper() + "M",
    }
    return clock_dict


def parse_duration(duration_string):
    """Parse a duration string."""
    pattern = re.compile(r"\b([0-9]+):(0?[0-9]|[1-5][0-9])\b")
    match = pattern.search(duration_string)
    try:
        wrong_value(match)
    except WrongInputError as e:
        click.echo(
            f"Error int the duration format. Should be HH:MM {e}"  # noqa
        )
        sys.exit(1)

    hours = match.group(1)
    minutes = match.group(2)
    duration_dict = {
        "hours": int(hours),
        "minutes": int(minutes),
    }
    return duration_dict


def parse_day(date_string):
    """Parse a date string."""
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "saturday"]
    if date_string.lower() in days:
        return date_string.lower()
    return None


class WrongInputError(ValueError):
    """Error when parsing input."""

    # pylint: disable=W0107

    pass


def wrong_value(value):
    """Handle invalid input format error."""
    if value is None:
        raise WrongInputError("Wrong format input")
