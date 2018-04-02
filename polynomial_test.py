import unittest

from polynomial import Polynomial


class PolynomialTest(unittest.TestCase):

    def test_create(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act & Assert
        self.assertIsNotNone(p)

    def test_create_with_tuple(self):
        # Arrange
        p = Polynomial((1, 2, 3))

        # Act & Assert
        self.assertIsNotNone(p)

    def test_create_with_copy_constr(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act
        p1 = Polynomial(p)

        # Assert
        self.assertIsNotNone(p1)

    def test_create_with_empty_arg(self):
        # Arrange
        p = Polynomial()

        # Act & Assert
        expected = Polynomial(0)
        self.assertEqual(expected, p)

    def test_create_from_list_of_coeffs(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act & Assert
        self.assertIsNotNone(p)

    def test_create_with_first_zero(self):
        # Arrange
        p = Polynomial([0, 1, -2, 3])

        # Act & Assert
        expected = Polynomial([1, -2, 3])
        self.assertEqual(expected, p)

    def test_add(self):
        # Arrange
        p1 = Polynomial([1, 2])
        p2 = Polynomial([3, 4, 5])
        p3 = Polynomial([1])

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
        expected = Polynomial(1, 5)
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
        p = Polynomial(2, -2, 3, 0, -4)

        # Act
        p_str = str(p)

        # Assert
        expected = '2x^4-2x^3+3x^2-4'
        self.assertEqual(expected, p_str)

    def test_str_with_float(self):
        # Arrange
        p = Polynomial([3.2, 0, -2.1])

        # Act
        p_str = str(p)

        # Assert
        expected = '3.2x^2-2.1'
        self.assertEqual(expected, p_str)

    def test_zero_degree_str(self):
        # Arrange
        p = Polynomial([-4, 1])

        # Act
        p_str = str(p)

        # Assert
        expected = '-4x+1'
        self.assertEqual(expected, p_str)

    def test_radd(self):
        # Arrange
        c = 2
        p = Polynomial(1, -2, 3)

        # Act
        result = c + p

        # Assert
        expected = Polynomial([1, -2, 5])
        self.assertEqual(expected, result)

    def test_rmul(self):
        # Arrange
        c = 2
        p = Polynomial(1, -2, 3)

        # Act
        result = c * p

        # Assert
        expected = Polynomial([2, -4, 6])
        self.assertEqual(expected, result)

    def test_add_negative_value(self):
        # Arrange
        p1 = Polynomial([1, -1])
        p2 = Polynomial([-1, 1])

        # Act
        result = p1 + p2

        # Assert
        expected = Polynomial(0)
        self.assertEqual(expected, result)

    def test_create_with_incorrect_args(self):
        # Arrange & Act & Assert
        self.assertRaises(TypeError, Polynomial, [1, "fff", Polynomial()])

    def test_add_incorrect_value(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act & Assert
        self.assertRaises(TypeError, p.__add__, "fff")

    def test_radd_incorrect_value(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act & Assert
        self.assertRaises(TypeError, p.__radd__, "fff")

    def test_sub_incorrect_value(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act & Assert
        self.assertRaises(TypeError, p.__sub__, "fff")

    def test_mul_incorrect_value(self):
        # Arrange
        p = Polynomial([1, 2, 3])

        # Act & Assert
        self.assertRaises(TypeError, p.__mul__, "fff")

    def test_eq_with_number(self):
        # Arrange
        p = Polynomial([3])
        c = 3

        # Act & Assert
        self.assertEqual(c, p)

    def test_eq_with_incorrect(self):
        # Arrange
        p = Polynomial([3])
        s = "fff"

        # Act & Assert
        self.assertRaises(TypeError, p.__eq__, s)

    def test_str_without_coeff(self):
        # Arrange
        p = Polynomial([1, 0])

        # Act
        p_str = str(p)

        # Assert
        expected = 'x'
        self.assertEqual(expected, p_str)

    def test_str_with_zero_polynomial(self):
        # Arrange
        p = Polynomial()

        # Act
        p_str = str(p)

        # Assert
        expected = '0'
        self.assertEqual(expected, p_str)

    def test_add_zero_polynomial(self):
        # Arrange
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial()

        # Act
        result = p1 + p2

        # Assert
        expected = p1
        self.assertEqual(expected, result)

    def test_mul_zero_polynomial(self):
        # Arrange
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial()

        # Act
        result = p1 * p2

        # Assert
        expected = p2
        self.assertEqual(expected, result)

    def test_mul_zero_const(self):
        # Arrange
        p = Polynomial([1, 2, 3])
        c = 0

        # Act
        result = c * p

        # Assert
        expected = Polynomial()
        self.assertEqual(expected, result)

    def test_str_with_neg_one_polynomial(self):
        # Arrange
        p = Polynomial([2, -1, 3])

        # Act
        p_str = str(p)

        # Assert
        expected = '2x^2-x+3'
        self.assertEqual(expected, p_str)

    def test_str_with_one(self):
        # Arrange
        p = Polynomial([1])

        # Act
        p_str = str(p)

        # Assert
        expected = '1'
        self.assertEqual(expected, p_str)

    def test_str_with_neg_one(self):
        # Arrange
        p = Polynomial([-1])

        # Act
        p_str = str(p)

        # Assert
        expected = '-1'
        self.assertEqual(expected, p_str)

    def test_str_with_first_zero(self):
        # Arrange
        p = Polynomial([0, -1, 0])

        # Act
        p_str = str(p)

        # Assert
        expected = '-x'
        self.assertEqual(expected, p_str)

    def test_str_with_one_polynomial(self):
        # Arrange
        p = Polynomial([2, 1, 3])

        # Act
        p_str = str(p)

        # Assert
        expected = '2x^2+x+3'
        self.assertEqual(expected, p_str)


if __name__ == '__main__':
    unittest.main()