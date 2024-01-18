# -*- coding: utf-8 -*-
"""version 0.1.0"""

from src.time_calculator.calculation import add_hours, add_minutes, add_days
from src.time_calculator.parser import parse_clock, parse_duration
from src.time_calculator.formatter import format_result


def add_time(clock_time, duration_time, day=None):
    """Main function of adding duration to a clock."""
    clock = parse_clock(clock_time)
    duration = parse_duration(duration_time)

    minutes, extra_hours = add_minutes(clock["min"], duration["minutes"])
    hours, extra_days, am_pm = add_hours(
        clock["hour"],
        duration["hours"],
        clock["am_pm"],
        extra_hour=extra_hours,
    )

    if day:
        day = add_days(day, extra_days)

    return format_result(
        hours, minutes, am_pm, extra_days=extra_days, dayofweek=day
    )
