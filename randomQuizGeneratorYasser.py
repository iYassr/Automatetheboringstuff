import random

quizYasser = {'Fastest':'C++','Simplist':'Python','Verbosest':'Java','Elegentent':'Ruby',"Weirdest":'Lisp'}
print(len(quizYasser.keys()))
for quizNum in range(3):
    fileQuiz = open("QuizNum%s.txt"% quizNum,'w')
    fileQuiz.write('\n')
    quests = list(quizYasser)
    fileQuiz.write('    Quiz Num %s    ' % quizNum)
    random.shuffle(quests)
    for i in range(quizYasser.__len__()):
        fileQuiz.write('Question Number %s' % (i))
        fileQuiz.write('\n')
        fileQuiz.write(quests[i] + ':   ')
        fileQuiz.write('\n')
        correctAnswer = quizYasser[quests[i]]
        options = list(quizYasser.values())
        del options[options.index(correctAnswer)]
        options = options[0:3]
        options += [correctAnswer]
        random.shuffle(options)
        for j in range (4):
            fileQuiz.write('%s: %s' % ('ABCD'[j], options[j]))
            fileQuiz.write('\n')
        fileQuiz.write('Correct Answer is: %s \n' % correctAnswer)
