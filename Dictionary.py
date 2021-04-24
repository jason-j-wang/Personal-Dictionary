# Changelog:
#       11/19/2019 (V 1.0) - began project
#       11/20/2019 (V 1.1) - changed print statements to better inform user on what changed inside dictionary
#       11/25/2019 (V 1.2) - implemented 5th option
#       11/29/2019 (V 1.3) - implemented .txt file to save user inputs
#       12/02/2019 (V 1.4) - debugged file write error for options 4 and 5, added file.close()

# TDL:
#       Make ! exit out of the program instead of stopping
#       Make the space bar and enter buttons invalid for new words and defs

import os

version = 1.4
print("Dictionary V", version, "\n -------------")
print('''Press "1" to search for a word and its definition
Press "2" to print out a list of words starting with same letter
Press "3" to add a word and its definition
Press "4" to change a word or definition
Press "5" to remove a word and its definition 
Press "~" to go back to the main menu  
Press "?" to print out this list again 
Press "!" to stop the program    ''')   # change later so ! will exit the program instead

my_dictionary = {}


def open_file():

    global file

    create_file = open("Dictionary.txt", "a")  # if the file does not exist, it creates a new one
    create_file.close()
    file = open("Dictionary.txt", "r+")
    dictionary_list = file.readlines()

    for item in dictionary_list:
        item_list = item.split(":")
        if len(item_list) > 1:
            my_dictionary.update({item_list[0]: item_list[1]})

# search_letter - searches the letter with search_input


def start():
    open_file()
    user_input = input("\nEnter your search option here: ")
    if user_input == "1":
        option_1()
    elif user_input == "2":
        option_2()
    elif user_input == "3":
        option_3()
    elif user_input == "4":
        option_4()
    elif user_input == "5":
        option_5()
    elif user_input == "!":
        print("Program complete!")
        file.close()
    elif user_input == "~":
        print("You are already on the main menu!")
        start()
    elif user_input == "?":
        main_menu()
        start()
    else:
        print("Invalid input, please try again!")
        start()


def main_menu():
    print('''
Press "1" to search for a word and its definition
Press "2" to print out a list of words starting with same letter
Press "3" to add a word and its definition
Press "4" to change a word or definition
Press "5" to remove a word and its definition 
Press "~" to go back to the main menu  
Press "?" to print out this list again 
Press "!" to stop the program 
    ''')
    start()


def option_1():

    found = False
    user_input = input("\nEnter to search a word: ")

    if user_input == "~":
        start()
    elif user_input == "!":
        print("Program complete!")
        file.close()
    elif user_input == "?":
        main_menu()
        start()
    else:

        words = list(my_dictionary.keys())
        print("Searching...")
        for word in words:
            if user_input.lower() == word:
                print("Word found!")
                print(word, "-", my_dictionary[word])
                start()
                found = True
        if not found:
            print("Word not found!")
            option_1()


def option_2():
    found = False
    user_input = input("\nEnter in a letter: ")

    if user_input == "~":
        start()
    elif user_input == "!":
        print("Program complete!")
        file.close()
    elif user_input == "?":
        main_menu()
        start()
    else:

        print("Searching...\n")
        words = list(my_dictionary.keys())
        words.sort()

        for word in words:
            if user_input[0].lower() == word[0]:
                found = True
        if not found:
            print("No words in dictionary starting with the letter \"" + user_input[0] + "\"!")
            option_2()
        if found:
            for word in words:
                if user_input[0].lower() == word[0]:
                    print(word)
            start()


def option_3():
    words = list(my_dictionary.keys())
    new_word = input("\nEnter a new word: ")

    if new_word == "~":
        start()
    elif new_word == "!":
        print("Program complete!")
        file.close()
    elif new_word == "?":
        main_menu()
        start()
    else:

        if new_word.lower() in words:
            print("This word already exists!")
            option_3()

        new_definition = input("Enter in the definition: ")
        print("Adding word and definition...")
        my_dictionary.update({new_word.lower(): new_definition.lower()})
        file.write(new_word.lower() + ":" + new_definition.lower() + "\n")
        print("Word and definition added!")
        start()


def option_4():
    selections = input('''Options:
"1" to change a word
"2" to change a definition
"3" to change a word and definition

Enter: ''')
    if selections == "1":
        option_4_1()
    elif selections == "2":
        option_4_2()
    elif selections == "3":
        option_4_3()
    elif selections == "~":
        start()
    elif selections == "!":
        print("Program complete!")
        file.close()
    elif selections == "?":
        main_menu()
        start()
    else:
        print("Invalid input!")
        option_4()


def option_4_1():
    updated_dictionary = []
    defs = list(my_dictionary.values())
    words = list(my_dictionary.keys())
    original_word = input("\nEnter in the word you want to change: ")

    if original_word == "~":
        start()
    elif original_word == "!":
        print("Program complete!")
        file.close()
    elif original_word == "?":
        main_menu()
        start()
    else:

        print("Finding word...")

        if original_word.lower() not in words:
            print("Word doesn't exist in dictionary! \n")
            option_4_1()

        print("Found word!")
        new_word = input("Enter in the new word: ")

        for word in words:
            if word == original_word:
                print("Updating word...")
                updated_dictionary.append(new_word.lower())
            else:
                updated_dictionary.append(word)

        zipped = zip(updated_dictionary, defs)   #zips two lists together
        my_dictionary.clear()
        my_dictionary.update(zipped)   #puts the two zipped lists into a dictionary
        file.close()
        file_write()
        print("Updated the word to \"" + new_word.lower() + "\"!")
        start()
1

def option_4_2():
    words = list(my_dictionary.keys())
    defs = list(my_dictionary.values())
    find_word = input("\nEnter a word to change its definition: ")

    if find_word == "~":
        start()
    elif find_word == "!":
        print("Program complete!")
        file.close()
    elif find_word == "?":
        main_menu()
        start()
    else:

        print("Finding word...")

        if find_word.lower() not in words:
            print("Word does not exist in dictionary!\n")
            option_4_2()

        print("Found word!")
        new_def = input("Enter in the new definition: ")
        print("Updating...")
        index = words.index(find_word.lower())  #finds index of the word, its definition is the same index as well
        defs[index] = new_def.lower()           #replacing the index where the old def is located with new one
        zipped = zip(words, defs)
        my_dictionary.clear()
        my_dictionary.update(zipped)
        file.close()
        file_write()
        print("Updated the definition of \"" + find_word.lower() + "\" to \"" + new_def.lower() + "\"!")
        start()


def option_4_3():
    updated_dictionary = []
    words = list(my_dictionary.keys())
    defs = list(my_dictionary.values())
    find_word = input("\nEnter the word you want to change: ")

    if find_word == "~":
        start()
    elif find_word == "!":
        print("Program complete!")
        file.close()
    elif find_word == "?":
        main_menu()
        start()
    else:

        index = words.index(find_word.lower())

        if find_word.lower() not in words:
            print("\"" + find_word.lower() + "\" doesn't exist in dictionary!")
            option_4_3()

        print("Found word!")
        new_word = input("Enter in the new word: ")

        for word in words:
            if word == find_word:
                print("Updating word...")
                updated_dictionary.append(new_word.lower())
                print("Updated!")
            else:
                updated_dictionary.append(word)

        new_def = input("Enter in a new definition: ")
        print("Updating definition...")
        defs[index] = new_def.lower()
        zipped = zip(updated_dictionary, defs)
        my_dictionary.clear()
        my_dictionary.update(zipped)
        file.close()
        file_write()
        print("Updated to \"" + new_word.lower() + "\" and its definition!" )
        start()


def option_5():
    find_word = input("\nEnter in a word to delete: ")
    words = list(my_dictionary.keys())

    if find_word == "~":
        start()
    elif find_word == "!":
        print("Program complete!")
        file.close()
    elif find_word == "?":
        main_menu()
        start()
    else:

        if find_word not in words:
            print("Word not found!")
            option_5()

        print("Word found!")
        print("Deleting...")
        my_dictionary.pop(find_word)
        file.close()
        file_write()
        print("Deleted \"" + find_word.lower() + "\"!")
        start()


def file_write():

    file = open("Dictionary.txt", "w+")
    my_list = []
    dic_keys = list(my_dictionary.keys())
    dic_values = list(my_dictionary.values())
    length = len(dic_keys)

    for i in range(length):
        my_list.append(dic_keys[i])
        my_list.append(dic_values[i])

    i = 0
    while i <= length * 2 - 1:
        file.write(my_list[i] + ":" + my_list[i + 1] + "\n")
        i = i + 2
    file.close()


start()