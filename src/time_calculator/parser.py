# -*- coding: utf-8 -*-
"""version 0.1.0"""

import re


def parse_clock(time_string):
    """Parse 12-hour clock format (ending in AM or PM)."""
    pattern = re.compile(
        r"\b(0?[1-9]|1[0-2]):(0?[0-9]|[1-5][0-9]) ([a, A]|[p, P])[m, M]\b"
    )
    match = pattern.search(time_string)
    if match is None:
        print("Error in parsing clock input.")
        return None

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
    if match is None:
        print("Error in parsing duration input.")
        return None
    hours = match.group(1)
    minutes = match.group(2)
    duration_dict = {
        "hours": int(hours),
        "minutes": int(minutes),
    }
    return duration_dict
