def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Main function
if __name__ == "__main__":
    arr = []
    n = int(input("Enter the value of n: "))

    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    # Perform selection sort
    selection_sort(arr)

    # Print the sorted array
    print("Sorted array:", " ".join(map(str, arr)))