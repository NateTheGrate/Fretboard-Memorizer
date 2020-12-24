import note as n
import constants
import random


# make a list of notes for each guitar string, defaulting to level 0
gtstrings = []
for string in constants.STRING_TUNING:
    index = 0
    # make note list for a string
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
    gtstrings.append(notes)


# THIS IS NOT A NOTE OBJECT, just the letter is all we need
def getNoteLetterIndex(noteLetter):
    # find the note in the NOTES array
    index = constants.NOTES.index(noteLetter[0].upper())

    # handle if the note is an accidental
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
    

# find the fret number given a note and a string (both contained in the Note object)
def toFretNum(note: n.Note):

    # find where the tuning of the string and note are in the NOTES array
    noteIndex = getNoteLetterIndex(note.getNote())
    stringIndex = getNoteLetterIndex(note.getString())

    # case 1: string index > note index
    #  need to find the amount of elements after the string (difference between length and string index), 
    #  and then add the note index to that
    if(stringIndex > noteIndex):
        return len(constants.NOTES) - stringIndex + noteIndex
    
    # case 2: string index < note index, don't need any fancy math here
    if(stringIndex < noteIndex):
        return noteIndex - stringIndex

    # case 3: string index = note index (fret 0 or 12 or 24 if you're crazy)
    return 0

test = n.AltNote('D', 'E', 'E#')
print(toFretNum(test))