import pickle

notes = []

# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
if notes.pickle:
    for n in notes.pickle:
        notes[n] = notes.pickle[n]

# B. Print out notes
    for x in range(len(notes)):
        print(notes[x])
# C. Read in a string from the user using input() and append it to notes
    user_input = input("Enter string ")
    notes.append(user_input)
# D. Save notes to notes.pickle
    notes.pickle = [None] * len(notes)
    for i in notes:
        notes.pickle[i] = notes[i]
