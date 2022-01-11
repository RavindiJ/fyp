import spacy
from spacy import displacy
from svo import svo

NER = spacy.load("en_core_web_sm")

def addToLabel(tag, word, labels):
    if (tag in labels):
        labels[tag].append(word)
    else:
        labels[tag]  = [word]

def ner(sentences):
    for sentence in sentences:
        text = NER(sentence)
        labels = dict()

        for word in text.ents:
            label = word.label_
            if (label == 'ORG'):
                addToLabel('ORG', word, labels)

            if (label == 'LOC'):
                addToLabel('LOC', word, labels)

            if (label == 'PERSON'):
                addToLabel('PERSON', word, labels)

            if (label == 'DATE'):
                addToLabel('DATE', word, labels)

            if (label == 'TIME'):
                addToLabel('TIME', word, labels)

            if (label == 'PRODUCT'):
                addToLabel('PRODUCT', word, labels)

            if ( label == 'FAC'):
                addToLabel('FAC', word, labels)

            if (label == 'EVENT'):
                addToLabel('EVENT', word, labels)

        subject, verb, attribute, question, wh_word = svo(sentence)
        if ((len(labels) > 2) and  (subject and verb and attribute)):
            print(sentence)
            print()
            print(labels)
            print()
            print("svo:, subject: {}, verb: {}, object: {}".format(subject, verb, attribute, question, wh_word))
            print()
            print()
            print()