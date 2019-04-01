##########################################################################
# CS 101
# Program : 6 Language quiz
# Name Erik Marquez
# Email eemxr9@mail.umkc.edu
# PROBLEM : Lamguage quiz
# ALGORITHM :
#   1. Search and open TXT files
#   2. parse through txt files and create quiz
#   3. ask the user to pick which test to take
#   4. ask the user for the number of words he will be quizzed on.
#   5. grade the user on the amount they for correct.
#   5.Repeat
# ERROR HANDLING:
# handled input File not found errors, input errors
# OTHER COMMENTS:
# Can open handle multiple files
###########################################################################

import random
import os


class Question(object):

    def __init__(self, question, answer, file, tries=3, see=False):
        '''Creates questions instance with attributes, see is not used'''
        self.question = question
        self.answer = answer
        self.file = file
        self.tries = tries
        self.see = see

    def __str__(self):
        print(input('Q -> {}'.format(self.question)))

    def __repr__(self):
        return 'Q -{}'.format(self.question)

    def num_tries(self):
        '''Used to decrement the number of tries a user has'''
        self.tries -= 1

    def correct(self):
        '''not used, planed on using but did not'''
        self.see = not self.see

    def ask_question(self):
        '''This is the question function. the the user for the correct answer
        checks to see if there are many answers and handles them appropriately
        returns 1 if correct and 2 if not. This is used for the grading the quiz.
        Lets the user see the words they got incorrect
        '''

        while True:
            user_input = input('Enter a valid spanish phrase for {} ==>'.format(self.question)).title()
            # print(self.answer)
            if len(self.answer) == 2:
                if user_input == self.answer[0] or user_input == self.answer[1]:
                    print('Correct. Good work\n')
                    return 1

            if user_input == self.answer[0]:
                print('Correct. Good work\n')
                return 1

            if self.tries == 1:
                print('\nIncorrect, valid choice(s) were:')
                for word in self.answer:
                    print(word)
                print()
                return 0

            self.num_tries()


def openfiles():
    '''Searches the enclosing folder for .txt files
    returns the the file names in a list
    Allows the user to add more txt files
    '''
    f = os.listdir()
    # print(f)
    files = []

    for file in f:
        if file[-4:] == '.txt':
            # print(file)
            files.append(file)

    # print(files)
    return files


def extract_qustions(txt_files: object):
    '''Uses the file list from open files funtion to open the files
    reads through the lines and creates a dictionary of the file, words, and question object
    returns the dictionary of words
    '''
    # print(txt_files)

    word_list = {}

    for file in txt_files:
        f = open(file)
        fh = f.readlines()
        # print(file)

        for words in fh:
            questions = words.strip().title().split(':')
            answer = questions[1].split(',')
            # print('Q',questions[0])
            # print('A',answer)

            file = file.title()
            word_list[file[:-4]] = word_list.get(file[:-4], {})
            word_list[file[:-4]][questions[0]] = word_list[file[:-4]].get(questions[0],
                                                                          Question(questions[0], answer, file))

    # print('word List',word_list)

    return word_list


def file_choices(words_lst):
    '''Extracts the keys from the dictionary from the  extract questions function
    reruns a list of keys
    '''
    files_list = []

    for key in words_lst.keys():
        files_list.append(key)

    return files_list


def user_menu(files_lst):
    '''Creates user menu, pick the files to open, Q to quit
    returns the user input
    handles improper inputs
    '''
    menu_dict = {'Q': 'Q'}
    num = 1
    key = ['Q']
    # print(files_lst)
    print('Vocabulary Program')
    print('Choose a file with the proper number or press Q to quit')
    for file in files_lst:
        print('\t{}. {}'.format(num, file))
        key.append(str(num))
        menu_dict[str(num)] = menu_dict.get(str(num), file)
        num += 1

    print('\tQ. Quit Program')

    user_input = input('==>').upper()
    while True:
        if user_input in key:
            break
        print('You must choose one of the valid options Q,1,2')
        user_input = input('==>').upper()

    # print(menu_dict)
    return menu_dict[user_input]


def quiz_length(word_dict):
    '''counts the the words dictionary
    returns the amount of words in an integer
    '''
    len_choices = {}
    for dict, words in word_dict.items():
        # print(dict,len(words))
        len_choices[dict] = len_choices.get(dict, len(words))

    return len_choices


def len_selection(length_q, question):
    '''Prompt user for length of quiz, error handling -
    has to be greater than 0 and less than or equal to 10
    uses the number from quiz length for error handling
    '''
    while True:
        try:
            user_input = int(input('\nHow many words in your quiz? ==>'))
            if user_input > 0 and user_input <= length_q[question]:
                break
            print('Number must be greater than zero and less than or equal to {}\n'.format(length_q[question]))
        except ValueError:
            print('You must enter an integer\n')
    return user_input


def quiz_random(word_dict, dict_selection, num_of_questions):
    '''Generates a list of the words from our words dictionary
    Randomises the list to create a random quiz every time
    returns that list
    '''
    word_lst = []
    for question in word_dict[dict_selection].keys():
        word_lst.append(question)
    # print(word_lst)
    random.shuffle(word_lst)
    # print(word_lst)

    return word_lst


def quiz(rand_word_list, quiz_len, word_dict, file_selection):
    '''Main quiz function
    pulls a random word from the words dictionry for the user to answer
    keeps track of how many were correct
    breaks when the user length is reached
    return how many were answered correct
    '''
    count = 0
    correct = 0
    for word in rand_word_list:
        # print(word)
        count += 1
        if count > quiz_len:
            break

        print('{}). '.format(count), end='')
        answer = word_dict[file_selection][word].ask_question()
        correct += answer
    return correct


def quiz_score(score, length):
    '''Grades the user and prints a score'''
    print('You got {} out of {}, which is {:.2f}%'.format(score, length, (score / length) * 100), '\n')


def main_loop():
    '''Main loop of program'''
    while True:
        file_list = openfiles()

        words = extract_qustions(file_list)

        files = file_choices(words)

        selection = user_menu(files)

        if selection == 'Q':
            break

        length = quiz_length(words)

        user_len = len_selection(length, selection)

        rand_word_list = quiz_random(words, selection, user_len)

        words_correct = quiz(rand_word_list, user_len, words, selection)

        quiz_score(words_correct, user_len)


main_loop()

print('\nThank you for playing!')
