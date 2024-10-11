from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


print("Naivní metoda iterování velkým seznamem")
#lst = get_n_primes(70000)
#for elem in lst:
#    print(elem)


print("=" * 80)
print("Iterator: PrimeIterator")


class PrimeIterator:
    # Iterator that allows you to iterate over n primes
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


iter = PrimeIterator(10)
print(f"Prvočíslo: {iter.__next__()}")
print(f"Prvočíslo: {iter.__next__()}")
print(f"Prvočíslo: {iter.__next__()}")
print(f"Prvočíslo: {iter.__next__()}")
print(f"Prvočíslo: {iter.__next__()}")
print(f"Prvočíslo: {iter.__next__()}")
print("-" * 40)
prime_numbers = []
for elem in iter:
    print(elem)
    prime_numbers.append(elem)

print(prime_numbers)


print("=" * 80)
print("Iterátor Fibonacciho posloupnosti")
# 1, 1, 2, 3, 5, 8, 13, ...


class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers >= self.n:
            raise StopIteration
        #result = self.a + self.b
        self.a, self.b = self.b, self.a + self.b
        self.generated_numbers += 1
        return self.a


fibonacci_iterator = FibonacciIterator(10)
for fib in fibonacci_iterator:
    print(fib)


print("=" * 80)
print("Prime numbers generator")


def prime_generator(n):
    # Generator for iterating over n primes
    print("Inside 'prime_generator'")
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        print(f"\tnumber={number}, generated_numbers={generated_numbers}")
        if is_prime(number):
            yield number
            print("\tafter yield")
            generated_numbers += 1
        number += 1


gen = prime_generator(20)
print(next(gen))
print("-" * 40)
print(next(gen))
print("-" * 40)
print(next(gen))

#for elem in gen:
#    print(elem)


def fibonacci_generator(n):
    a = 0
    b = 1
    generated_numbers = 0
    while generated_numbers < n:
        a, b = b, a+b
        generated_numbers += 1
        yield a


print("=" * 80)
print("Fibonacci numbers")
fib_gen = fibonacci_generator(10)
for elem in fib_gen:
    print(elem)


print("Konec")
