
import os

def main():

    first_file_name = 'textfile1.txt'
    second_file_name = 'textfile2.txt'

    list_one = []
    list_two = []
    
    with open(first_file_name, 'r') as text_file_one:
        for line in text_file_one:
            for word in line.strip('\n').split():
                if word.isalpha():
                    list_one.append(word)
    
    with open(second_file_name, 'r') as text_file_two:
        for line in text_file_two:
            for word in line.strip('\n').split():
                if word.isalpha():
                    list_two.append(word)
    
    unique_list_one = one_unique_list(list_one, first_file_name)
    unique_list_two = one_unique_list(list_two, second_file_name)

    combine_unique_list(unique_list_one, unique_list_two)

    unique_list_of_list(unique_list_one, unique_list_two, first_file_name)
    unique_list_of_list(unique_list_two, unique_list_one, second_file_name)

    unique_from_both_lists(unique_list_one, unique_list_two)




def one_unique_list(open_list, which_file):
    unique_list = []
    for word in open_list:
        if word not in unique_list:
            unique_list.append(word)

    print(f'\n\nNumber of unique words in {which_file}: {len(unique_list)}')
    print(*unique_list, sep=", ")

    return unique_list


def combine_unique_list(unique_list_one, unique_list_two):
        combined_unique = unique_list_one.copy()
        for word in unique_list_two:
            if word not in combined_unique:
                combined_unique.append(word)
        print('\n\nCommon unique words from both lists: ')
        print(*combined_unique, sep=', ')

def unique_list_of_list(unique_list_one, unique_list_two, file_name):
        unique_list = []
        for word in unique_list_one:
            if word not in unique_list_two:
                unique_list.append(word)

        print(f'\n\nWords unique for {file_name}: ')
        print(*unique_list, sep=', ')

def unique_from_both_lists(unique_list_one, unique_list_two):
    unique_both_lists = []
    for word in unique_list_one:
        if word in unique_list_two:
            unique_both_lists.append(word)
    print('\n\nCombined unique words: ')
    print(*unique_both_lists, sep=', ')


if __name__ == '__main__':
    main()