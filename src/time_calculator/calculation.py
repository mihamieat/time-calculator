# -*- coding: utf-8 -*-
"""version 0.1.0"""


def add_hours(clock_hours, duration_hours, ap_pm, extra_hour=0):
    """Add hours to the clock hours."""
    if ap_pm == "PM":
        clock_hours = clock_hours + 12
    days = 0
    hours_sum = extra_hour
    raw_hours_sum = clock_hours + duration_hours
    if raw_hours_sum > 24:
        days = int(raw_hours_sum / 24)
        hours_sum = raw_hours_sum - days * 24
    else:
        hours_sum += raw_hours_sum
    if hours_sum == 24:
        hours_sum = 0

    ap_pm_result = "AM"
    if hours_sum > 12:
        hours_sum = hours_sum - 12
        ap_pm_result = "PM"

    return hours_sum, days, ap_pm_result
