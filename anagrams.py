def main():
    word_dictionary = {}

    first_word = input('Input first word: ')
    second_word = input('Input second word: ')

    word_dictionary[first_word]=list(first_word)
    word_dictionary[second_word]=list(second_word)
    
    anagram_status = True

    if len(first_word) == len(second_word):
        for i in word_dictionary[second_word]:
            if i not in word_dictionary[first_word]:
                anagram_status = False
                break
    else:
        anagram_status = False
        
    
    print("These words are anagrams." if anagram_status else "These word are not annagrams.")
    


if __name__ == '__main__':
    main()