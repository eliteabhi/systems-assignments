def binary_search( arr: list[int], x: int ) -> int:

    right: int = len( arr ) - 1
    left: int = 0

    if arr[left] == x:
        return left

    elif arr[right] == x:
        return right

    while left <= right:
        mid: int = ( left + right ) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            left = mid + 1;

        if arr[mid] > x:
            right = mid - 1

    return mid

# ----------------------------------------------------------------

array = [n for n in range(10)]
print(binary_search(array, 3))
print(binary_search(array, 7))
print(binary_search(array, 11))
print(binary_search(array, 20))
