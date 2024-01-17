# -*- coding: utf-8 -*-
"""version 0.1.0"""


def format_result(hours, minutes, am_pm, extra_days=0):
    """Returns a string representation of the result of the operation."""
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)

    output_str = f"{hours}:{minutes} {am_pm}"

    if extra_days > 0:
        output_str += f" ({'next day' if extra_days == 1 else f'{extra_days} days later'})"

    return output_str
