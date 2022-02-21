from segmentation import Segment
from greet_mess import Greetings

if __name__ == '__main__':
    grab = Segment()
    greet = Greetings()

    # conversation starts from here
    greet.start()
    questions = input()
    print(grab.intention(questions))
    grab.clean()
    """
    print(grab.entities(questions))
    print(grab.interrogative(questions))
    print(grab.nau(questions))
    print(grab.expandPerson(questions))
    """
    while True:
        if greet.ending(questions):
            greet.endingMess()
            break
        else:
            greet.nextQuestion()
            questions = input()
            if greet.keepAsking(questions):
                questions = input()
            print(grab.intention(questions))
            grab.clean()
            """
            print(grab.entities(questions))
            print(grab.interrogative(questions))
            print(grab.nau(questions))
            print(grab.expandPerson(questions))
            """