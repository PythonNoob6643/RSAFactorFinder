from math import pow,gcd
from Crypto.Util.number import isPrime


class PeriodFinder:
    def __init__(self, n, min_loop, verbose, factors):
        self.n = n
        self.min_loop = min_loop
        self.verbose = verbose
        self.factors_needed = factors

        self.numbers = []

    def Class_Control(self):
        verbose = self.verbose
        count = verbose

        for i in range(self.min_loop,  self.n - 1, 1):
            if i == verbose:
                verbose += count
                print(f"i : {i}")
                print(f"Complete : {round((i / self.n) * 100, 2)} %")

            try:
                result = self.Period(i)
                self.Factor_of_N(result)

                if len(self.numbers) == self.factors_needed:
                    print(f" Factor of N : {i}")
                    break
            except KeyboardInterrupt:
                break

            except Exception as e:
                pass

    def Period(self, i):
        if isPrime(i) and i < self.n:
            result = gcd(i, self.n)
            return result
        else:
            return None

    def Factor_of_N(self, result):
        if self.n % result == 0 and isPrime(result):
            self.numbers.append(result)
            print("-" * 80)
            print(f" N : {self.n}")
            print(f"Factor of N : {result}")
            print("-" * 80)
        else:
            pass


def main():
    N = None
    min_loop = None
    verbose = None
    factors = None

    # Accept user input
    while True:
        try:
            n = int(input("The Value of N :"))
            if n is not None:
                N = n
                print("-" * 80)
                break

        except Exception as e:
            print("Please enter an int")

    while True:
        try:
            user_loop = int(input("Starting Number :"))
            if user_loop is not None:
                min_loop = user_loop
                print("-" * 80)
                break

        except Exception as e:
            print("Please enter an int")

    while True:
        try:
            verBose = int(input("Verbose Rate:"))
            if verBose is not None:
                verbose = verBose
                print("-" * 80)
                break

        except Exception as e:
            print("Please enter an int")

    while True:
        try:
            fac = int(input("How Many Factors // > 0 :"))
            if fac is not None:
                factors = fac
                print("-" * 80)
                break

        except Exception as e:
            print("Please enter an int")

    if min_loop is not None and N is not None and verbose is not None and factors is not None:
        pp = PeriodFinder(N, min_loop, verbose, factors)
        pp.Class_Control()
    else:
        print("Answer has A None Type.")


if __name__ == '__main__':
    main()