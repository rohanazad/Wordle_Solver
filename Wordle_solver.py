'''
This Python code takes a character string as input of any length and gives out all the 
possible English dictionary words of any length that can be made from it. 

Suppose your input is "evil", the output will be- [i, ie, lie, live, evil, vile, veil].

Along with this Python code, you will need a file named- English_words.csv, it contains
around 4 Lakh English words. Its location has to be passed inside this code at line #17.

That's it, Enjoy your daily Wordle without fail !!!    
'''


import pandas as pd

english_words_list_csv = pd.read_csv(
    "Insert local address of the excel file- English_words.csv")
list_of_english_words = list(english_words_list_csv.List_of_words)


def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)


def add_element(element_index, word_in_list, list_input, list_working):
    count_of_new_words = len(word_in_list) + 1
    for c in range(count_of_new_words):
        new_word = \
            word_in_list[:len(word_in_list)-c] + \
            list_input[element_index] + \
            word_in_list[len(word_in_list)-c:]
        list_working.append(new_word)
    return list_working


def find_next_combination(index, last_index):
    counter = 0
    if last_index + 1 < len(input_list):
        function_combination_list = input_list[last_index + 1:]
        for d in function_combination_list:
            counter = counter + 1
            combination_list_letter.append(combination_list_letter[index] + d)
            combination_list_index.append(last_index + counter)


def make_permut(input_string):
    list_input = list(input_string)
    list_working = []
    list_for_function = []
    list_input_index = -1
    for a in list_input:
        list_input_index = list_input_index + 1
        if list_input_index == 0:
            list_working.append(a)
        else:
            list_for_function = list_working[-factorial(list_input_index):]
            for b in list_for_function:
                # call function
                list_working = add_element(
                    list_input_index, b, list_input, list_working)
    return list_working[-factorial(len(input_string)):]


input_string = 'evil'  # ENTER THE INPUT STRING
input_list = list(input_string)
input_list_index = -1
actual_index = -1
combination_list_letter = []
combination_list_index = []
working_list_combination_letter = []
working_list_combination_index = []


for a in range(len(input_list)):
    if a == 0:
        for b in input_list:
            input_list_index = input_list_index+1
            combination_list_index.append(input_list_index)
            combination_list_letter.append(b)
    else:
        working_list_combination_index = combination_list_index[int(
            -factorial(len(input_list))/(factorial(a)*factorial(len(input_list)-a))):]
        working_list_combination_letter = combination_list_letter[int(
            -factorial(len(input_list))/(factorial(a)*factorial(len(input_list)-a))):]
        for c in working_list_combination_index:
            actual_index = actual_index + 1
            # call function
            find_next_combination(actual_index, c)

dedup_combination_list = list(set(combination_list_letter))

final_collection = []
final_permutation_list = []
final_english_words_list = []

for k in dedup_combination_list:
    final_collection.append(make_permut(k))

for i in final_collection:
    for j in i:
        final_permutation_list.append(j)

dedup_permutation_list = list(set(final_permutation_list))

for i in dedup_permutation_list:
    if i in list_of_english_words:
        final_english_words_list.append(i)

final_english_words_list.sort(key=len)

print(final_english_words_list)
print(len(final_english_words_list))
