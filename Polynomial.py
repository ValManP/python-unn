class Polynomial:

    # input: a_n, .. , a_1, a_0 or other polynomial
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Polynomial):
            self.coeffs = args[0].coeffs[:]
        else:
            self.coeffs = args[::-1]
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
            res = [t + other for t in list(self.coeffs)]

        res = res[::-1]
        return Polynomial(*res)

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
            res = [t * other for t in list(self.coeffs)]

        res = res[::-1]
        return Polynomial(*res)

    def __eq__(self, other):
        return self.coeffs == other.coeffs

    def __ne__(self, other):
        return self.coeffs != other.coeffs

    def __str__(self):
        res = []

        for self_pow, self_coeff in enumerate(self.coeffs):
            if self_coeff:
                if self_pow == 0:
                    self_pow = ''
                elif self_pow == 1:
                    self_pow = 'x'
                else:
                    self_pow = 'x^' + str(self_pow)

                if self_coeff == 1:
                    self_coeff = ''
                elif self_coeff < 0:
                    self_coeff = '- ' + str(self_coeff * -1)
                else:
                    self_coeff = '+ ' + str(self_coeff)

                res.append(str(self_coeff) + self_pow)

        if res:
            res.reverse()
            return ' '.join(res)
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
