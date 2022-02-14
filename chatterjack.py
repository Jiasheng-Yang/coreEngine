from segmentation import Segment
from greet_mess import Greetings


if __name__ == '__main__':
    grab = Segment()
    greet = Greetings()
    greet.start()
    questions = input()
    while True:
        if greet.ending(questions):
            greet.endingMess()
            break
        else:
            greet.nextQuestion()
            questions = input()
            if greet.keepAsking(questions):
                questions = input()
