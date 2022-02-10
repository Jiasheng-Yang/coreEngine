from coredata import interrogatives

import spacy
nlp = spacy.load("en_core_web_sm")


class Segment():
    def __init__(self):
        self.question = ""

    def segmentSentence(self, questions):
        doc = nlp(questions)
        for token in doc:
            return token.text

    # store the lower token words in the list
    def segmentList(self, questions):
        words = []
        doc = nlp(questions)
        for token in doc:
            words.append(token.lower_)
        return words

    # grab the interrogative from the list
    def interrogative(self, questions):
        words = self.segmentList(questions)
        for word in words:
            if word in interrogatives:
                return word

    # grab the entities
    def entities(self, questions):
        doc = nlp(questions)
        # find the entities
        for entity in doc.ents:
            return entity.text, entity.label_

"""
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
"""