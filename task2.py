dict_ = {}


def get_count_char(str_):
    str_ = "".join(str_.lower().split())
    for letter_ in str_:
        if letter_.isalpha():
            if letter_ not in dict_:
                dict_[letter_] = 1
            else:
                dict_[letter_] += 1
    return dict_


def two_dict_(dict_):
    sum_ = sum(dict_.values())
    for i in dict_:
        dict_[i] = round((dict_[i] / sum_) * 100, 3)
    print(sum(dict_.values()))
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
