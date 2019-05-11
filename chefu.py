import fileinput
import random


def chefu_solution(numbers):
    possibilities = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            possibilities.append((i, j))

    def get_next():
        chosen = random.choice(possibilities)
        return numbers[chosen[0]] + numbers[chosen[1]]

    return get_next

def real_solution(numbers):
    assert(len(numbers) > 1)
    max = numbers[0] + numbers[1]
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) > max:
                max = numbers[i] + numbers[j]
    return max


def is_equal(numbers):
    successes = 0
    tries = 1000000
    real_max = real_solution(numbers)
    sol = chefu_solution(numbers)
    for _ in range(tries):
        ch_max = sol()
        if ch_max == real_max:
            successes += 1
    return successes / tries


def read_test():
    input_stream = fileinput.input()
    num_tests = int(next(input_stream))
    for _ in range(num_tests):
        num_numbers = int(next(input_stream))
        numbers = list(map(lambda x: int(x), (next(input_stream).split())))
        assert(num_numbers == len(numbers))
        yield numbers


if __name__ == "__main__":
    for numbers in read_test():
        prob = is_equal(numbers)
        print(prob)
