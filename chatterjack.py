from segmentation import Segment

if __name__ == '__main__':
    grab = Segment()
    questions = input()
    print(grab.entities(questions))
    print(grab.interrogative(questions))
    while True:
        if (questions == "Exit"):
            break
        else:
            questions = input()
            print(grab.entities(questions))
            print(grab.interrogative(questions))