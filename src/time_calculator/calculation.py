# -*- coding: utf-8 -*-
"""version 0.1.0"""


def add_hours(clock_hours, duration_hours, ap_pm, extra_hour=0):
    """Add hours to the clock hours."""
    if ap_pm == "PM":
        clock_hours = clock_hours + 12

    raw_hours_sum = clock_hours + duration_hours + extra_hour
    days = raw_hours_sum // 24
    hours_sum = raw_hours_sum % 24

    ap_pm_result = "AM"
    if hours_sum == 12:
        ap_pm_result = "PM"
    if hours_sum > 12:
        hours_sum -= 12
        ap_pm_result = "PM"

    return hours_sum, days, ap_pm_result


def add_minutes(clock_minutes, duration_minutes):
    """Add minutes to a clock minutes."""
    raw_minutes_sum = clock_minutes + duration_minutes
    extra_hours = raw_minutes_sum // 60
    minutes_sum = raw_minutes_sum % 60

    return minutes_sum, extra_hours
