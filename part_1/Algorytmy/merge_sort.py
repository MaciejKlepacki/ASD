def merge(arr, left, mid, right):
    # Tworzenie podtablic za pomocą slicing
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0  # Indeksy dla left_part i right_part
    k = left   # Indeks dla głównej tablicy

    # Scalanie dwóch podtablic
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Dodanie pozostałych elementów z left_part
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Dodanie pozostałych elementów z right_part
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        # Oblicz środek
        mid = left + (right - left) // 2

        # Sortowanie lewej i prawej części
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        # Scalanie posortowanych części
        merge(arr, left, mid, right)


# Kod testowy
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:", *arr)

    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array is:", *arr)