```
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    sample = [5, 12, 18, 25, 32, 40, 47]
    target = 32

    result = binary_search(sample, target)

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")
```
