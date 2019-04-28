#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key
# from this https://automatetheboringstuff.com/chapter8/

import random

# The quiz data.  Keys are provinces and values are their capitals

capitals = {'Alberta': 'Edmonton', 'British Columbia': 'Victoria', 'Saskatchewan': 'Regina',
            'Manitoba': 'Winnipeg', 'Ontario': 'Toronto', 'Quebec': 'Quebec City',
            'Nova Scotia': 'Halifax', 'New Brunswick': 'Fredericton',
            'Prince Edward Island': 'Charlottetown', 'Newfoundland and Labrador': 'St. Johns'}

# Generate quiz files
for quizNum in range(2):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nTeacher:\n\n')
    quizFile.write((' ' * 20) + 'Province Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Write out the header for the answer file.
    answerKeyFile.write('This is the answer key for Test %s' % (quizNum + 1))
    answerKeyFile.write('\n\n')

    # Shuffle the order of the provinces
    provinces = list(capitals.keys())
    random.shuffle(provinces)

    # Loop through all 10 provinces, making a question for each.
    for questionNum in range(10):
        # Get right and wrong answers.
        correctAnswer = capitals[provinces[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file
        quizFile.write('%s What is the capital of %s?\n' % (questionNum + 1,
                       provinces[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
