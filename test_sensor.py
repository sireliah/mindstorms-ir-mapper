from unittest import TestCase

from robot_utils import prox_to_cm, robot_degrees_to_rotations


class TestSensor(TestCase):

    def test_prox_to_cm(self):
        result = prox_to_cm(100)

        self.assertEqual(result, 70)

    def test_robot_degrees_to_rotations(self):
        result = robot_degrees_to_rotations(180)

        self.assertEqual(result, 2.39999994)

    def test_robot_degrees_to_rotations_neg(self):
        result = robot_degrees_to_rotations(-90)

        self.assertEqual(result, -1.19999997)
