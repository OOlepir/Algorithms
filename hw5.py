def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Сливаем
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    # Сравниваем элементы и добавляем наименьший
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result += left[i:]
    result += right[j:]

    return result


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(merge_sort([]))                          # пустой
print(merge_sort([5, 5, 5, 5]))                # одинаковые
print(merge_sort([9, 7, 5, 3, 1]))             # убывание
print(merge_sort([1, 2, 3, 4, 5]))             # уже отсортирован
print(merge_sort([1]))                         # один элемент
print(merge_sort([4, 2]))                      # два элемента


# Сам код реализации
def read_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))

def merge_files(file_list):
    all_numbers = []

    for file in file_list:
        numbers = read_file(file)
        all_numbers = merge(all_numbers, numbers)

    return all_numbers

# Пример использования:
files = ["file1.txt", "file2.txt", "file3.txt"]
sorted_result = merge_files(files)

# Сохраняем результат в файл
with open("merged_output.txt", "w") as f:
    f.write(" ".join(map(str, sorted_result)))
