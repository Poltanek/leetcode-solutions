def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid  # Target found, return index
        elif guess > target:
            high = mid - 1  # Target is in the lower half
        else:
            low = mid + 1  # Target is in the upper half

    return -1  # Target not found

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    target = 7
    result = binary_search(arr, target)
    print(f"Target found at index: {result}")