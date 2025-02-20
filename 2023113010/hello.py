"""Module to find the maximum sum of a contiguous subarray."""

def max_subarray_sum(arr):
    """Finds the maximum sum of a contiguous subarray using Kadane's Algorithm."""
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

if __name__ == "__main__":
    import sys
    import pylint.lint
    import pytest

    pylint_output = pylint.lint.Run([__file__], do_exit=False)
    with open("pylint_output.txt", "w", encoding="utf-8") as f:
        f.write(str(pylint_output))
    
    pytest.main(["-v", "--junitxml=test_output.xml"])

# Test cases for pytest
def test_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    assert max_subarray_sum([42]) == 42