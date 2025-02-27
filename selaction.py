def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Given elements
elements = [22, 13, 4, 8, 17, 26, 53, 4]
sorted_elements = selection_sort(elements)
print("Sorted elements using Selection Sort:", sorted_elements)

output:-

![Screenshot 2024-08-02 211852](https://github.com/user-attachments/assets/17f9dd4f-2275-421c-a9c1-35daab9accdb)
