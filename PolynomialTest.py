import unittest

from Polynomial import Polynomial


class PolynomialTest(unittest.TestCase):

    def test_create(self):
        # Arrange
        p = Polynomial(1, 2, 3)

        # Act & Assert
        self.assertIsNotNone(p)

    def test_create_with_copy_constr(self):
        # Arrange
        p = Polynomial(1, 2, 3)

        # Act
        p1 = Polynomial(p)

        # Assert
        self.assertIsNotNone(p1)

    def test_create_with_first_zero(self):
        # Arrange
        p = Polynomial(0, 1, -2, 3)

        # Act & Assert
        expected = Polynomial(1, -2, 3)
        self.assertEqual(expected, p)

    def test_add(self):
        # Arrange
        p1 = Polynomial(1, 2)
        p2 = Polynomial(3, 4, 5)
        p3 = Polynomial(1)

        # Act
        p = p1 + p2 + p3

        # Assert
        expected = Polynomial(3, 5, 8)
        self.assertEqual(expected, p)

    def test_sub(self):
        # Arrange
        p1 = Polynomial(1, 2)
        p2 = Polynomial(3, 4, 5)

        # Act
        p = p1 - p2

        # Assert
        expected = Polynomial(-3, -3, -3)
        self.assertEqual(expected, p)

    def test_add_const(self):
        # Arrange
        p1 = Polynomial(1, 2)
        c = 3

        # Act
        p = p1 + c

        # Assert
        expected = Polynomial(4, 5)
        self.assertEqual(expected, p)

    def test_mul(self):
        # Arrange
        p1 = Polynomial(1, 2)
        p2 = Polynomial(1, 2, 3)

        # Act
        p = p1 * p2

        # Assert
        expected = Polynomial(1, 4, 7, 6)
        self.assertEqual(expected, p)

    def test_mul_const(self):
        # Arrange
        p1 = Polynomial(1, 2)
        c = 3

        # Act
        p = p1 * c

        # Assert
        expected = Polynomial(3, 6)
        self.assertEqual(expected, p)

    def test_equals(self):
        # Arrange
        p1 = Polynomial(1, 2)
        p2 = Polynomial(1, 2)

        # Act & Assert
        self.assertTrue(p1 == p2)

    def test_not_equals(self):
        # Arrange
        p1 = Polynomial(1, 2)
        p2 = Polynomial(3, 2, 1)

        # Act & Assert
        self.assertTrue(p1 != p2)

    def test_str(self):
        # Arrange
        p = Polynomial(1, -2, 3, 0, -4)

        # Act
        p_str = str(p)

        # Assert
        expected = 'x^4 - 2x^3 + 3x^2 - 4'
        self.assertEqual(expected, p_str)
