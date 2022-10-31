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


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))



def percent_letter(percent_str):
    percent_str = "".join(percent_str.lower())
    percent_dict = {}
    for letter in percent_str:
        if letter.isalpha():
            if letter in percent_dict:
                percent_dict[letter] += 1
            else:
                percent_dict[letter] = 1
    total_count = sum(percent_dict.values())
    for word, val in percent_dict.items():
        percent_dict[word] = round(val / total_count * 100, 1)
    return percent_dict


print(percent_letter(main_str))
