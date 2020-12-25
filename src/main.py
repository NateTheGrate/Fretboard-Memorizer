from note import AltNote, Note
from card import Card
import constants
import util

import random

guitar = util.generateGuitar()

cards = []
for string in guitar:
    for note in string: 
        cards.append(Card(note))


def leveler(card: Card, isRight):
    cardLevel = card.getLevel()
    if(isRight):
        card.setLevel(cardLevel + 1)
    elif(cardLevel > 0):
        card.setLevel(cardLevel - 1)
    
    # else do nothing because you can't go negative in levels

def fretQuiz():
    randCard = random.choice(cards)
    print(randCard)
    val = input("Enter fret number: ")
    userNote = util.fretToNote(guitar, int(val), randCard.getNote().getString())
    
    isRight = randCard.getNote() == userNote
    leveler(randCard, isRight)

    print("level on card is now", str(randCard.getLevel()))

def noteQuiz():
    randNote = util.getRandomNote(guitar)

    if(isinstance(randNote, AltNote)):
        randNote.switch()
    
    randFret = randNote.getFret()
    print(str(randFret) + ", " + randNote.getString() + " string")

    val = input("Enter note: ")
    
    print(randNote.note == val)

fretQuiz()