from unittest import TestCase

from robot_utils import adjust_gears


class TestSensor(TestCase):

    def test_adjust_gears(self):
        result = adjust_gears(90)

        self.assertEqual(result, 330.0)

    def test_adjust_gears2(self):
        result = adjust_gears(180)

        self.assertEqual(result, 300.0)

    def test_adjust_gears3(self):
        result = adjust_gears(270)

        self.assertEqual(result, 270.0)

    def test_adjust_gears4(self):
        result = adjust_gears(360)

        self.assertEqual(result, 240.0)

    def test_adjust_gears_reset(self):
        result = adjust_gears(1080)

        self.assertEqual(result, 0)
