# -*- coding: utf-8 -*-
"""Test parser package."""

import unittest
from src.time_calculator.parser import parse_clock, parse_duration


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


class TestDurationPrser(unittest.TestCase):
    """Test duration parser."""

    def test_correct_duration(self):
        """Test correct duration."""
        duration = parse_duration("180:56")
        excepted = {"hours": 180, "minutes": 56}
        self.assertEqual(duration, excepted)

    def test_correct_duration_zeros(self):
        """Test correct duration."""
        duration = parse_duration("04:06")
        excepted = {"hours": 4, "minutes": 6}
        self.assertEqual(duration, excepted)

    def test_duration_minutes_out_of_bound(self):
        """Test out of bound minutes."""
        duration = parse_duration("04:66")
        excepted = None
        self.assertEqual(duration, excepted)
