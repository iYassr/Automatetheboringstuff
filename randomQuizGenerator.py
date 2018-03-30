#! python3
#randomQuizGenerator.py
import os

mylist = ['a','b']
print (mylist.index('a'))


print(os.getcwd())
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New'
   : 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
    : 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
quizNum = 35
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizFile = open('captialsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz%s_answers.txt' % (quizNum + 1), 'w')
    # TODO: Write out header for the quiz

    quizFile.write('Name:\n \nDate: \nPeriod: \n\n')
    quizFile.write((' ' * 20 + 'State Capitals Quiz (Form %s') % (quizNum + 1))
    quizFile.write('\n\n')


    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        quizFile.write('%s. What is the capital of %s \n' % (questionNum + 1, states[questionNum]))
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        answerOptions = wrongAnswers + [ correctAnswer ]
        random.shuffle(answerOptions)
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))

            quizFile.write('\n')




quizFile.close()
answerKeyFile.close()






