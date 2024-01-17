# -*- coding: utf-8 -*-
"""Test calculations modules."""

import unittest
from src.time_calculator.calculation import add_hours


class TestHoursCalculation(unittest.TestCase):
    """Test hours calculation"""

    def test_correct_hours_hours_sum(self):
        """Test correct hours calculation."""
        hours_sum, days, am_pm = add_hours(6, 6, "AM")
        self.assertEqual(hours_sum, 12)
        self.assertEqual(days, 0)
        self.assertEqual(am_pm, "AM")

    def test_correct_hours_hours_sum_extra_days_am(self):
        """Test correct hours calculation."""
        hours_sum, days, am_pm = add_hours(12, 18, "AM")
        self.assertEqual(hours_sum, 6)
        self.assertEqual(days, 1)
        self.assertEqual(am_pm, "AM")

    def test_correct_hours_hours_sum_extra_days_pm_midnight_result(self):
        """Test correct hours calculation."""
        hours_sum, days, am_pm = add_hours(6, 30, "PM")
        self.assertEqual(hours_sum, 0)
        self.assertEqual(days, 2)
        self.assertEqual(am_pm, "AM")

    def test_correct_hours_hours_sum_extra_days_pm_result(self):
        """Test correct hours calculation."""
        hours_sum, days, am_pm = add_hours(6, 43, "PM")
        self.assertEqual(hours_sum, 1)
        self.assertEqual(days, 2)
        self.assertEqual(am_pm, "PM")
