class Recursion:

    def exponent(self, c, n):
        if n == 1:
            return c
        else:
            return c * self.exponent(c, n - 1)

    def handshakes(self, n):
        if n == 2:
            return 1
        else:
            return n - 1 + self.handshakes(n - 1)

    def is_divisible(self, n, d):
        if n < 0:
            return False
        elif n == 0:
            return True
        else:
            return self.is_divisible(n - d, d)

    def is_prime_helper(self, n, d):
        if d > n / 2:
            return True
        elif n % d == 0:
            return False
        else:
            return self.is_prime_helper(n, d + 1)

    def is_prime(self, n):
        return self.is_prime_helper(n, 2)
