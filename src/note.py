import constants
import util

class Note:
    def __init__(self, note, string):
        self.note = note
        self.string = string

    def getNote(self):
        return self.note
    
    def setNote(self, note):
        self.note = note

    def getString(self):
        return self.string

    # find the fret number given a note and a string (both contained in the Note object)
    # params: Note
    # returns int 
    def getFret(self):

        # find where the tuning of the string and note are in the NOTES array
        noteIndex = util.getNoteLetterIndex(self.getNote())
        stringIndex = util.getNoteLetterIndex(self.getString())

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

    def setString(self, string):
        self.string = string
    
    def __eq__(self, other):
        return self.note == other.note and self.string == other.string

    def __str__(self):
        return self.note + ", " + self.string + " string"

# class to handle sharps and flats
class AltNote(Note):
    def __init__ (self, lowNote, highNote, string):
        # default to sharps
        super().__init__(lowNote + "#", string)

        self.lowNote = lowNote + '#'
        self.highNote = highNote + 'b'
    
    # toggle between '#' and 'b' for key changes
    def switch(self):
        if(self.note[1] == "#"):
            self.note = self.highNote
        else:
            self.note = self.lowNote