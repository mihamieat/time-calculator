# -*- coding: utf-8 -*-
"""Test formatter modules."""

import unittest
from src.time_calculator.formatter import format_result


class TestFormatter(unittest.TestCase):
    """Test formatter."""

    def test_correct_formatter_output(self):
        """Test correct formatter output."""
        output = format_result(12, 3, "PM", 1)
        expected = "12:03 PM (next day)"
        self.assertEqual(output, expected)

    def test_correct_formatter_output_no_extra_day(self):
        """Test correct formatter output."""
        output = format_result(12, 30, "PM")
        expected = "12:30 PM"
        self.assertEqual(output, expected)

    def test_correct_formatter_output_more_extra_days(self):
        """Test correct formatter output."""
        output = format_result(12, 30, "PM", 2, "Monday")
        expected = "12:30 PM, Monday (2 days later)"
        self.assertEqual(output, expected)
