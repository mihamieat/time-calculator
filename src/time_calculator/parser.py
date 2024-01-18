# -*- coding: utf-8 -*-
"""version 0.1.0"""


def parse_hours(time_string):
    """Parse 12-hour clock format e.g. 08:04."""
    time_lst = time_string.split(":")
    hours = int(time_lst[0])
    minutes = int(time_lst[1])
    return hours, minutes


def parse_clock(time_string):
    """Parse 12-hour clock format (ending in AM or PM)."""
    time = time_string.split()
    am_pm = time[1]
    hours, minutes = parse_hours(time[0])
    clock_dict = {
        "hour": int(hours),
        "min": int(minutes),
        "am_pm": am_pm.upper(),
    }
    return clock_dict


def parse_duration(duration_string):
    """Parse a duration string format e.g 16:04."""
    hours, minutes = parse_hours(duration_string)
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
