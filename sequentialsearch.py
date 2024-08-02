def sequential_search(elements, search):
    for index, element in enumerate(elements):
        if element == search:
            return index
    return -1

elements = [1, 3, 5, 8, 10, 23, 35]
search_element = 10

result = sequential_search(elements, search_element)

if result != -1:
    print(f"Element {search_element} found at index {result}.")
else:
    print(f"Element {search_element} not found.")

output:-

![Screenshot 2024-08-02 185606](https://github.com/user-attachments/assets/58193e77-55ff-41bb-aa2e-b031629e9154)
