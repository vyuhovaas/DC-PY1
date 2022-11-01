def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if letter in dict_:
                dict_[letter] += 1
            else:
                dict_[letter] = 1

    return dict_


def percent_letter(dict_):
    dict_two = {}
    total_count = sum(dict_.values())
    for word, val in dict_.items():
        dict_two[word] = round(val / total_count * 100, 1)
    return dict_two


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


print(get_count_char(main_str))
print(percent_letter(get_count_char(main_str)))




