"""
 This class utilize NPL (spaCy) to segment the input questions and grab key information.
"""

from coredata import interrogatives, nauInf, calls

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

    # grab the common entities
    def entities(self, questions):
        doc = nlp(questions)
        # store the key information
        keyInf = {}
        # find the common entities
        for entity in doc.ents:
            keyInf[entity.text] = entity.label_
        return keyInf

    # grab the nau entities
    def nau(self, questions):
        nauKeyInf = {}
        words = self.segmentList(questions)
        for nauWord in words:
            if nauWord in nauInf:
                nauKeyInf[nauWord] = 'ORG'
        return nauKeyInf

    # grab the special name and label 'Person'
    def expandPerson(self, questions):
        sepPer = {}
        words = self.segmentList(questions)
        for named in words:
            if named in calls:
                spePerInd = words.index(named) + 1
                sepPer[words[spePerInd]] = 'Person'
        return sepPer

    # package all grab function
    def intention(self, questions):
        self.interrogative(questions)
        self.nau(questions)
        self.entities(questions)