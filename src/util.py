import note as n
import constants
import random

# returns index of a n.Note in the n.NoteS array
# params: char[1] or char[2] 
# returns int
def getNoteLetterIndex(noteLetter):
    # find the n.Note in the n.NoteS array
    index = constants.NOTES.index(noteLetter[0].upper())

    # handle if the n.Note is an accidental
    if(len(noteLetter) > 1):
        # check if sharp
        if(noteLetter[1] == '#'):
            # if sharp add one to the index
            # shouldn't have to deal with wrapping around the array in this case
            index += 1
        if(noteLetter[1] == 'b'):
            # now need to wrap backwards because Ab is at the end and indexof('A') = 0 and 0 - 1 = -1
            index = (index - 1) % len(constants.NOTES)

    return index

# given a string, a fret number, and a guitar layout
# params: n.Note objects(n.n.Note[][]), fret number(int), string(char[1] or char[2])
# returns: either an accidental or natural n.Note
def fretToNote(notes, fretnum, string):

    # get string index in the tuning array for the index of the first dimension
    stringTuneIndex = constants.STRING_TUNING.index(string)
    # get string index in the notes array for the second dimension
    stringIndex = getNoteLetterIndex(string)

    # get music n.Note in the n.Notes array
    return notes[stringTuneIndex][(stringIndex + fretnum) % len(notes[stringTuneIndex])]
    
# given an array of n.Notes it returns a random one
# param: n.Notes array
# returns: random n.Note
def getRandomNote(notes):
    return random.choice(random.choice(notes))


# make a list of n.Notes for each guitar string to represent a guitar
# params: none
# returns: 2d array where rows represent a guitar string and columns represent frets
def generateGuitar():
    guitar = []
    for string in constants.STRING_TUNING:
        index = 0
        # make n.Note list for a string
        notes = []
        for note in constants.NOTES:
            # handle accidentals
            if(note == 'Z'):
                newAltNote = n.AltNote(constants.NOTES[index - 1], constants.NOTES[(index + 1) % len(constants.NOTES)], string)
                notes.append(newAltNote)
            else:
                # handle naturals
                newNote = n.Note(note, string)
                notes.append(newNote)

            index += 1
        # append list to 
        guitar.append(notes)
    
    return guitar