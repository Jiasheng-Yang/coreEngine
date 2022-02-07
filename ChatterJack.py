import spacy
nlp = spacy.load("en_core_web_sm")

class Segment():
    def __init__(self):
        self.question = ""

    def interrogative(self, questions):
        doc = nlp(questions)
        # grab the interrogative
        for token in doc:
            return token.text

    def entities(self, questions):
        doc = nlp(questions)
        # find the entities
        for entity in doc.ents:
            print(entity.text, entity.label_)

if __name__ == '__main__':
    segment = Segment()
    questions = input()
    print(type(segment.interrogative(questions)))
    segment.entities(questions)
    while True:
        if (questions == "Exit"):
            break
        else:
            questions = input()
            segment.entities(questions)
            segment.interrogative(questions)