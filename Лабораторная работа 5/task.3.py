import random


def get_unique_list_numbers(start=-10, stop=10, n=15) -> list[int]:
    return random.sample(range(start, stop), n)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))



