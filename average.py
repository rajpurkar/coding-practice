"""Beginner task at https://www.codechef.com/problems/SIMPSTAT."""
import fileinput


def remove_bottom_k(numbers, k):
    """Remove the smallest k numbers."""
    numbers.sort()
    return numbers[k:]


def remove_top_k(numbers, k):
    """Remove the largest k numbers."""
    numbers.sort(reverse=True)
    return numbers[k:]


def average(numbers):
    """Simple mean the numbers."""
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)


def average_after_process(numbers, k):
    """Mean the numbers after removing smallest and largest k numbers."""
    numbers = remove_top_k(numbers, k)
    numbers = remove_bottom_k(numbers, k)
    avg = average(numbers)
    return avg


def generate_test_cases():
    """Generate the next test case."""
    input_stream = fileinput.input()
    num_tests = int(next(input_stream))
    for test in range(num_tests):
        line = next(input_stream)
        split_line = line.split()
        assert(len(split_line) == 2)
        num_numbers = int(split_line[0])
        k = int(split_line[1])

        line = next(input_stream)
        numbers = list(map(lambda x: int(x), line.split()))
        assert(len(numbers) == num_numbers)
        yield numbers, k


if __name__ == "__main__":
    for numbers, k in generate_test_cases():
        avg = average_after_process(numbers, k)
        print(avg)
