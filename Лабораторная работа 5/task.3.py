from random import randint


def get_unique_list_numbers(start=-10, stop=10, n=15) -> list[int]:
    list_number = []
    list_number = [randint(start, stop) for num in range(n) if num not in list_number if len(list_number) != n]
    return list_number


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))



