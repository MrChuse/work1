import math

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(a, b, c):
    if max(a, b, c) >= a + b + c - max(a, b, c) or min(a, b, c) <= 0:
        raise ValueError('Enter proper lengths')
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def is_right_angle(a, b, c):
    mn = min(a, b, c)
    mx = max(a, b, c)
    if mx >= a + b + c - mx or mn <= 0:
        raise ValueError('Enter proper lengths')
    md = a + b + c - mn - mx
    return mn ** 2 + md ** 2 - mx ** 2 <= 1e-8

if __name__ == "__main__":
    import unittest
    class TestArea(unittest.TestCase):

        def test_circle_area(self):
            self.assertAlmostEqual(circle_area(1), math.pi)
            self.assertAlmostEqual(circle_area(10), 314.159265359)
            self.assertAlmostEqual(circle_area(5), 78.5398163397)

        def test_triangle_area(self):
            self.assertAlmostEqual(triangle_area(1, 1, 2 ** 0.5), 0.5)
            self.assertAlmostEqual(triangle_area(2, 2, 2 * (2 ** 0.5)), 2)
            self.assertAlmostEqual(triangle_area(1, 1, 1), 0.25 * 3**0.5)
            self.assertAlmostEqual(triangle_area(3, 4, 5), 6)
            self.assertAlmostEqual(triangle_area(127, 92, 150), 345/4 * 4551 ** 0.5)
            with self.assertRaises(ValueError):
                triangle_area(1, 1, 2)
            with self.assertRaises(ValueError):
                triangle_area(50, 100, 200)
            with self.assertRaises(ValueError):
                triangle_area(-1, 1, 2)

        def test_is_right_angle(self):
            self.assertTrue(is_right_angle(1, 1, 2 ** 0.5))
            self.assertTrue(is_right_angle(2, 2, 2 * 2 ** 0.5))
            self.assertFalse(is_right_angle(1, 1, 1))
            self.assertTrue(is_right_angle(3, 4, 5))
            self.assertFalse(is_right_angle(127, 92, 150))
            with self.assertRaises(ValueError):
                is_right_angle(1, 1, 2)
            with self.assertRaises(ValueError):
                is_right_angle(50, 100, 200)
            with self.assertRaises(ValueError):
                is_right_angle(-1, 1, 2)

    unittest.main()
