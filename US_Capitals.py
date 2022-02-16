
import os

def main():
    capital_list = {}
    capital_file = open('USCapitals.txt', 'r')
    for line in capital_file:
        key, val = line.strip('\n').split(', ')
        capital_list[key] = val
    
    capital_file.close()

    while True:
        choice = input('Input state: ')

        try:
            print(f'The capital of {choice} is {capital_list[choice]}.')
        except KeyError:
            print("That is not an American State. Please try again.")
        else:
            break

if __name__ == '__main__':
    main()