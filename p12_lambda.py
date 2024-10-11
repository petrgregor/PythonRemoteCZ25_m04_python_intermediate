from functools import reduce


def to_lower(sentence):
    return sentence.lower()


lower_lambda = lambda sentence: sentence.lower()


def squared_func(numbers):
    squared = []
    for number in numbers:
        squared.append(number ** 2)
    return squared


if __name__ == '__main__':
    sentence = "HA HA HA"
    print(to_lower(sentence))
    print(lower_lambda("AHOJ"))

    numbers = [1, 2, 3, 4, 5]
    print(squared_func(numbers))
    print(list(map(lambda x: x ** 2, numbers)))
    print(f"filter: {list(filter(lambda x: x % 2 == 0, numbers))}")
    print(f"filter: {list(filter(lambda x: x > 2, numbers))}")

    print(f"reduce: {reduce(lambda x, y: x + y, numbers)}")
    print(f"reduce: {reduce(lambda x, y: x * y, numbers)}")
    for i in range(1, 6):
        print(i)
    print(f"reduce: {reduce(lambda x, y: x * y, range(1, 6))}")
