class Polynomial(object):
    # input: a_n, .. , a_1, a_0 or other polynomial or list of coeffs
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Polynomial):
            self.coeffs = args[0].coeffs[:]
        elif len(args) == 0:
            self.coeffs = [0]
        elif isinstance(args[0], list):
            self.coeffs = args[0][::-1]
        else:
            self.coeffs = args[::-1]

        for i in self.coeffs:
            if not isinstance(i, (int, float)):
                raise TypeError("Only int or float is expected")

        self.trim()

    def __add__(self, other):
        res = []

        if isinstance(other, Polynomial):
            for i in range(max(len(self.coeffs), len(other.coeffs))):
                if i >= len(self.coeffs):
                    res.append(other.coeffs[i])
                elif i >= len(other.coeffs):
                    res.append(self.coeffs[i])
                else:
                    res.append(self.coeffs[i] + other.coeffs[i])
        else:
            if not isinstance(other, (int, float)):
                raise TypeError("Only int or float is expected")
            res = list(self.coeffs)
            res[0] += other

        res = res[::-1]
        return Polynomial(*res)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            s = list(self.coeffs)
            o = list(other.coeffs)

            res = [0] * (len(s) + len(o) - 1)
            for self_pow, self_coeff in enumerate(s):
                for other_pow, other_coeff in enumerate(o):
                    res[self_pow + other_pow] += self_coeff * other_coeff
        else:
            if not isinstance(other, (int, float)):
                raise TypeError("Only int or float is expected")
            res = [t * other for t in list(self.coeffs)]

        res = res[::-1]
        return Polynomial(*res)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        elif isinstance(other, (int, float)):
            return self == Polynomial(other)
        else:
            raise TypeError("Polynomial or int or float is expected")

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        res = []

        for self_pow, self_coeff in enumerate(self.coeffs):
            if self_coeff:
                if self_pow == 0:
                    str_value = ''
                elif self_pow == 1:
                    str_value = 'x'
                else:
                    str_value = 'x^' + str(self_pow)

                if self_coeff == 1 and self_pow != 0:
                    self_coeff = ''
                elif self_coeff == -1 and self_pow != 0:
                    self_coeff = '-'
                elif self_coeff < 0:
                    self_coeff = '-' + str(self_coeff * -1)
                elif self_pow == (len(self.coeffs) - 1):
                    self_coeff = str(self_coeff)
                else:
                    self_coeff = '+' + str(self_coeff)

                res.append(str(self_coeff) + str_value)

        if res:
            res.reverse()
            return ''.join(res)
        else:
            return '0'

    def trim(self):
        coeffs = list(self.coeffs)
        if coeffs:
            max_not_empty = len(coeffs) - 1
            if coeffs[max_not_empty] == 0:
                max_not_empty -= 1
                while max_not_empty >= 0 and coeffs[max_not_empty] == 0:
                    max_not_empty -= 1
                del coeffs[max_not_empty + 1:]
        self.coeffs = tuple(coeffs)
