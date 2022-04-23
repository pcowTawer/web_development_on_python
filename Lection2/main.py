def is_prime(n):
    for i in range(2, int(pow(n, 0.5))):
        if n % 2 == 0:
            return False
    return True


def print_prime_before(n):
    for i in range(1, n):
        if is_prime(i):
            print(i)


def find_nod(u, v):
    if v == 0:
        return u
    return find_nod(v, u % v)


def fibonachi_sequence(n):
    fib_num = 2
    last1 = 1
    if n <= 2:
        return last1
    if n == 3:
        return fib_num
    for i in range(3, n):
        last2 = last1
        last1 = fib_num
        fib_num = last1 + last2
    return fib_num


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, obj):
        return Complex(self.real + obj.real, self.imag + obj.imag)

    def __sub__(self, obj):
        return Complex(self.real - obj.real, self.imag - obj.imag)

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def __mul__(self, obj):
        return Complex((self.real * obj.real - self.imag * obj.imag), (self.real * obj.imag + obj.real * self.imag))

    def __truediv__(self, obj):
        return Complex((self.real * obj.real + self.imag * obj.imag) / (obj.real ** 2 + obj.imag ** 2),
                       (obj.real * self.imag - self.real * obj.imag) / (obj.real ** 2 + obj.imag ** 2))

    def __str__(self):
        if self.imag == 0:
            return str(self.real)
        if self.real == 0:
            return str(self.imag) + "*i"
        if self.imag == 1:
            return str(self.real) + " + " + "i"
        if self.imag == -1:
            return str(self.real) + " - " + "i"
        if self.imag < 0:
            return str(self.real) + " - " + str(-self.imag) + "*i"
        return str(self.real) + " + " + str(self.imag) + "*i"


def main():
    print(Complex(-2, 1))


if __name__ == "__main__":
    main()
