arr = [10, 20, 30, 40, 50, 60, 70]
x = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        print("Element found at position", mid + 1)
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")