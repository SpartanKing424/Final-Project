note_names = ["C", "D", "E", "F", "G", "A", "B"]
octave_numbers = [1, 2, 3, 4, 5, 6, 7]
# creates a list of 
real_notes = []
for octave in octave_numbers:
    for note in note_names:
        real_notes.append(note + str(octave))


'''
Not used anymore, but still useful info:
    DEFAULT_NOTE = real_notes[21]      
    DEFAULT_INDEX = 21
C4(middle C) is the default note for the first note in a measure, and index 21 in real notes
'''