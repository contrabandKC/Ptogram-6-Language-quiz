##########################################################################
# CS 101
# Program : 6 Language quiz
# Name Erik Marquez
# Email eemxr9@mail.umkc.edu
# PROBLEM : Lamguage quiz
# ALGORITHM :
#   1. Ask user for a file to open
#   2. Validate the input
#   3. Create two files to save to
#   4. Take the data from the input and append to a dictionary
#   5. Output a monthly totals and a smoothed average total
# ERROR HANDLING:
# handled input File not found errors
# OTHER COMMENTS:
# Instructor did not provide a copy of the data. Could only confirm the first 3 values. They do match up
###########################################################################

import os
import random


class Question (object):

    def __init__ (self, file, question, answer, show=False):
        self.question = question
        self.answer = answer
        self.show = show
        self.file = file

    def __str__(self):
        return ('{} {} {}'.format(self.question,self.answer,self.file))

    def __repr__(self):
        return self.question

    def __len__(self):
        pass

class File_Reader(object):
    def __init__(self,file_name, list_wrds):
        '''Creates file instance'''
        self.file_name = file_name
        self.list_wrds = list_wrds


    def __str__(self):
        return ('{} {}'.format(self.file_name,self.list_wrds))

    def __repr__(self):
        return ('file ={} Numberofwords ={}'.format(self.file_name,len(self.list_wrds)))

    def question_maker(self):
        print('class q_maker', self.file_name)
        num = 1
        words_available = []

        for word in self.list_wrds:
            print(type(word))
            print(word)
            word = word.split(':')
            print(word)
            print('file name', self.file_name)
            file_name = self.file_name
            print('question',word[0].strip().split(','))
            question = word[0].strip().split(',')
            print('Answer =>',word[1].strip().split(','))
            answer = word[1].strip().split(',')
            print(question, answer, file_name)
            question_name = 'q' + str(num)
            print(question_name)
            question_name= Question(file_name, question, answer)

            print('Class', answer)

            print('q name', question_name)

            words_available.append(question_name)

            num += 1
        return words_available







def check_files():
    '''Check vocabulary files in directory, returns files in tuple'''
    f = os.listdir()
    #print(f)
    files = []

    for file in f:
        if file[-4:] == '.txt':
            files.append(file)

    #print(files)
    return files

def create_files(files : list):
    '''Creates txt files to dict'''
    number_of_files = 0
    for file in files:
        #print(file)
        f = open(file)
        fh = f.readlines()
        files[number_of_files]  = File_Reader(file, fh)
        number_of_files += 1
        #print(fh)
    return  files

def create_question(files):
    '''returns the questions'''
    print(type(files))
    print(files)
    for file in files:
        print('create question', file)
        File_Reader.question_maker(file)




def quiz_length():
    '''Prompt user for length of quiz, error handling -
    has to be greater than 0 and less than or equal to 10'''
    while True:
        try:
            user_input = int(input('\nHow many words in your quiz? ==>'))
            if user_input > 0 and user_input <= 10:
                break
            print('Number must be greater than zero and less than or equal to 10\n')
        except ValueError:
            print('You must enter an integer\n')
    return user_input

def random_quiz(quiz,num):
    '''Generate a random quiz'''

    questions = list(quiz.keys())
    print(questions)
    print(quiz)
    picker = random.sample(range(0, len(questions)), num)
    print(picker)
    correct = 0
    for times in range(0,num):
        print('correct',correct)
        question = questions[picker[times]]
        answer = quiz[question]
        print('#{}. Enter a valid spanish phrase for {}'.format(times+1, question))
        user_input = input('==>')
        if user_input == quiz[question]:
            print('Correct. Good work\n')
            correct +=1
        else:
            print('Incorrect, valid choice(s) were {}\n'.format(answer))
    return correct

def grade(num,correct):
    '''Gives user a grade'''
    print('You got {} out of {}, which is {:.2f}%'.format(correct,num,(correct/int(num))*100))

def user_menu():
    '''Creates user menu, pick the files to open, Q to quit'''
    key = ('1','2','Q')
    print('Vocabulary Program')
    print('Choose a file with the proper number or press Q to quit')
    print('\t1. places.txt')
    print('\t2. verbs.txt')
    print('\tQ. Quit Program')
    user_input = input('==>').upper()
    while True:
        if user_input in key:
            break
        print('You must choose one of the valid options Q,1,2')
        user_input = input('==>').upper()
    return user_input

def main_loop():
    '''Programs main function calls'''

    files = check_files()

    file_converter = create_files(files)



    questions = create_question(file_converter)

    print(questions)


    # while True:
    #     user_input = user_menu()
    #
    #     if user_input == "1":
    #         number = quiz_length()
    #         correct = random_quiz(words,number)
    #         grade(number,correct)


    print('Thank you for using Language Quiz.')


    print(q10)



main_loop()