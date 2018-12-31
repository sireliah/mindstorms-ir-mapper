from unittest import TestCase

from server import calculate_coords, parse_data


class TestServer(TestCase):

    def test_parse_data_ok(self):
        data = bytes('60 20'.encode('utf-8'))
        angle, dist = parse_data(data)

        self.assertEqual(angle, 60)
        self.assertEqual(dist, 20)

    def test_parse_data_error(self):
        data = bytes('60 i20'.encode('utf-8'))
        with self.assertRaises(ValueError):
            (a, d) = parse_data(data)

        self.assertEqual(1, 1)

    def test_calculate_coords_acute(self):
        (x, y) = calculate_coords(60, 20)

        self.assertEqual((x, y), (10.000000000000002, 17.32050807568877))

    def test_calculate_coords_obtuse(self):
        (x, y) = calculate_coords(130, 20)

        self.assertEqual((x, y), (15.32088886237956, -12.855752193730785))

    def test_calculate_coords_200(self):
        (x, y) = calculate_coords(200, 20)

        self.assertEqual((x, y), (6.840402866513377, -18.793852415718167))

    def test_calculate_coords_320(self):
        (x, y) = calculate_coords(320, 20)

        self.assertEqual((x, y), (-12.85575219373079, 15.320888862379558))

    def test_calculate_coords_angle_zero(self):
        (x, y) = calculate_coords(0, 20)

        self.assertEqual((x, y), (20.0, 0))

    def test_calculate_coords_right_angle(self):
        (x, y) = calculate_coords(90, 20)

        # Close enough, float!
        self.assertEqual((x, y), (1.2246467991473533e-15, 20.0))

    def test_calculate_coords_180(self):
        (x, y) = calculate_coords(180, 20)

        self.assertEqual((x, y), (1.2246467991473533e-15, -20.0))
