# -*- coding: utf-8 -*-
"""Test main module."""

import unittest
from src.time_calculator.main import time_calculator


class TestTimeCalculator(unittest.TestCase):
    """Test time_calculator."""

    def test_time_calculator_success(self):
        """Test success calculation."""
        outpt = time_calculator("3:00 PM", "3:10")
        expected = "6:10 PM"
        self.assertEqual(outpt, expected)

    def test_time_calculator_success_2(self):
        """Test success calculation."""
        outpt = time_calculator("11:30 AM", "2:32")
        expected = "2:02 PM"
        self.assertEqual(outpt, expected)

    def test_time_calculator_success_3(self):
        """Test success calculation."""
        outpt = time_calculator("11:43 AM", "00:20")
        expected = "12:03 PM"
        self.assertEqual(outpt, expected)

    def test_time_calculator_success_4(self):
        """Test success calculation."""
        outpt = time_calculator("10:10 PM", "3:30")
        expected = "1:40 AM (next day)"
        self.assertEqual(outpt, expected)

    def test_time_calculator_success_5(self):
        """Test success calculation."""
        outpt = time_calculator("11:43 PM", "24:20")
        expected = "12:03 AM (2 days later)"
        self.assertEqual(outpt, expected)

    def test_time_calculator_success_6(self):
        """Test success calculation."""
        outpt = time_calculator("6:30 PM", "205:12")
        expected = "7:42 AM (9 days later)"
        self.assertEqual(outpt, expected)
