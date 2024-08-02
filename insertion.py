def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

elements = [1, 4, 2, 8, 23]
insertion_sort(elements)
print("Sorted elements:", elements)

output:-
![Screenshot 2024-08-02 213051](https://github.com/user-attachments/assets/41f14881-30b6-4667-9033-a39cd8df3b68)
