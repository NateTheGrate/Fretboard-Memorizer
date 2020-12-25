from note import Note

class Card:
    def __init__(self, note: Note, level=0):
        self.note = note
        self.level = level
    
    def getNote(self):
        return self.note

    def setNote(self, note: Note):
        self.note = note
    
    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level

    def __str__ (self):
        return str(self.getNote()) + " " + str(self.getLevel())