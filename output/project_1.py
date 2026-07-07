from typing import List

def sort_numbers(numbers: List[int]) -> List[int]:
    try:
        numbers.sort()
        return numbers
    except TypeError as e:
        print("Invalid input, ensure all elements are integers.", str(e))

# Test the function
print(sort_numbers([45, 32, 8, 33, 1]))