class Note:
    def __init__(self, note, string, level = 0):
        self.note = note
        self.string = string
        self.level = level

    def getNote(self):
        return self.note
    
    def setNote(self, note):
        self.note = note

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

    def getString(self):
        return self.string

    def setString(self, string):
        self.string = string
    
    def __str__(self):
        return self.note + ", " + self.string + " string" + ", level " + str(self.level)

# class to handle sharps and flats
class AltNote(Note):
    def __init__ (self, lowNote, highNote, string, level=0):
        # default to sharps
        super().__init__(lowNote + "#", string, level)

        self.lowNote = lowNote + '#'
        self.highNote = highNote + 'b'
    
    # toggle between '#' and 'b' for key changes
    def switch(self):
        if(self.note[1] == "#"):
            self.note = self.highNote
        else:
            self.note = self.lowNote