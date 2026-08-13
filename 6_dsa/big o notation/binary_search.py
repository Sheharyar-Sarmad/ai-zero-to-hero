def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Example
arr = [4, 9, 15, 21, 34, 57, 68, 91]
target = 68

result = binary_search(arr, target)

print(result)