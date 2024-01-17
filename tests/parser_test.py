# -*- coding: utf-8 -*-
"""Test parser package."""

import unittest
from src.time_calculator.parser import parse_clock


class TestClockParser(unittest.TestCase):
    """Test clock parser."""

    def test_correct_clock_no_zero(self):
        """Test correct clock format with zeros in single-digits."""
        clock = parse_clock("8:2 pm")
        expected = {
            "hour": 8,
            "min": 2,
            "am_pm": "PM",
        }
        self.assertEqual(clock, expected)

    def test_correct_clock_with_zero(self):
        """Test correct clock format with zeros in single-digits."""
        clock = parse_clock("08:02 pm")
        expected = {
            "hour": 8,
            "min": 2,
            "am_pm": "PM",
        }
        self.assertEqual(clock, expected)

    def test_error_hours_out_boundaries(self):
        """Test out of bound hours."""
        clock = parse_clock("18:02 pm")
        expected = None
        self.assertEqual(clock, expected)

    def test_error_minutes_out_boundaries(self):
        """Test out of bound minutes."""
        clock = parse_clock("1:72 pm")
        expected = None
        self.assertEqual(clock, expected)
