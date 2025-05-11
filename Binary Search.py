import bisect

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 23
idx = bisect.bisect_left(arr, key)
print(f"Found at index {idx}" if idx < len(arr) and arr[idx] == key else "Not Found")