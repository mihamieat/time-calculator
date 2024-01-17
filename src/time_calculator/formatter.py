# -*- coding: utf-8 -*-
"""version 0.1.0"""


def format_result(hours, minutes, am_pm, extra_days=0, dayofweek=None):
    """Returns a string representation of the result of the operation."""
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)

    output_str = f"{hours}:{minutes} {am_pm}"

    if extra_days > 0:
        if extra_days == 1:
            day_info_str = "next day"
        else:
            day_info_str = f"{extra_days} days later"

        if dayofweek:
            output_str += f", {dayofweek} ({day_info_str})"
        else:
            output_str += f" ({day_info_str})"
    elif dayofweek:
        output_str += f", {dayofweek}"

    return output_str
