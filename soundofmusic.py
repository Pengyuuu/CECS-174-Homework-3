import musicbox

my_music = musicbox.MusicBox()

NOTES = [("C", 60), ("D", 62), ("E", 64), ("F", 65), ("G", 67), ("A", 69), ("B", 71)]
MAJOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_INTERVALS = [2, 1, 2, 2, 1, 2, 2]


def note_to_int(note):
    value = 0
    integer = 0

    # find last position of an octave
    octave = note.rfind("^")

    # note would be one after last position of octave
    noteSection = octave + 1

    # add octave to total value
    value = ((octave + 1) * 12)

    # split note into a list
    noteList = note.split('^')

    # copy the list and assign the letter
    noteList = noteList[noteSection]
    noteLetter = noteList[0]

    # if the note has a suffix, isolate it, then change the value
    if len(noteList) > 1:
        noteSuffix = noteList[1]
        if noteSuffix == 'b':
            value -= 1
        elif noteSuffix == '#':
            value += 1

    # for every item in NOTES iterate, that many times: 7
    for i in NOTES:
        # for every item in one of those lists, iterate: 2
        for c in i:
            # x is the letter stored, y is the integer
            x = i[0]
            y = i[1]
            if noteLetter == x:
                integer = y

    if integer == 0:
        value = -1
        return value

    value += integer

    for i in range(len(note)):
        if note[i].isalpha() is False and note[i] != "^" and note[i] != "b" and note[i] != "#":
            value = -1

    return value


def print_menu():
    print("Main menu: \n"
          "1. Play scale \n"
          "2. Play song \n"
          "3. Quit")


def get_menu_choice():
    choice = int(input("Please enter a selection: "))
    while choice < 1 or choice > 3:
        choice = int(input("Please enter a selection: "))
    return choice


def get_scale():
    integer = -1
    # checks if there is a space, major, or minor in input
    while integer == -1 or "Major" not in scale and "Minor" not in scale and " " not in scale and "major" not in scale \
            and "minor" not in scale:
        scale = input("Please enter a scale name: ")

        # split at the space into a list
        scale = scale.split(" ")

        # send the note to find it's integer
        integer = int(note_to_int(scale[0]))

    # assign major or minor to a new variable
    scale = scale[1]

    # create a list with the integer and major or minor
    choice = (integer, scale)

    return choice


def scale_to_ints(scale):
    # assign major or minor to a variable
    x = scale[1]

    # if the variable is major, do this
    if x == "Major" or x == "major":
        # set returned integer to a variable
        y = scale[0]

        # create a list and append y to it
        notes = []
        notes.append(y)

        # loop for each step in the list
        for i in MAJOR_INTERVALS:
            # add the step to y and append it
            y += i
            notes.append(y)

    # if the variable is minor, do this
    elif x == "Minor" or x == "minor":
        # set returned integer to a variable
        y = scale[0]
        # create a list and append y to it
        notes = []
        notes.append(y)
        # loop for each step in the list
        for i in MINOR_INTERVALS:
            # add the step to y and append it
            y += MINOR_INTERVALS[i]
            notes.append(y)

    # return the list
    return notes


def menu_play_scale():
    # get scale
    scale = get_scale()

    # send scale to turn into an integer
    scale = scale_to_ints(scale)

    # loop through the scale, it should always be 8
    for i in range(8):
        # assign whatever integer scale is to x
        x = scale[i]
        my_music.play_note(x, 500)


def get_song_file():
    file = input('Please enter a song file name: ')

    return file


def play_song(file_name):
    first_line = True

    # loop for each line in file
    for line in open(file_name):

        # if there's a // in line, s=pass it
        if "//" in line:
            first_line = False
            continue

        # split line, separating it into notes and duration by spaces
        line_split = line.split(" ")
        # assign duration to timing as the duration will be the last in the list
        timing = int(line_split[-1])

        # if the split list has a length more than 2, there is a chord
        if len(line_split) > 2:

            # create a list to store chords
            chord = []

            # loop for the length of the list
            for i in range(len(line_split)):
                # do this as long as it's a note and not the duration
                if line_split[i] != line_split[-1]:
                    # assign note to x
                    x = line_split[i]
                    # send x to first function, returns an integer
                    integer = note_to_int(x)
                    # put that integer into the chord list
                    chord.append(integer)

            # play the list of chords along with the duration
            my_music.play_chord(chord, timing)

        elif len(line_split) == 2:
            # assign the note to note variable
            note = line_split[0]

            # if it's a P, do a pause
            if note == "P":
                my_music.pause(timing)
            # if it's a I, change instruments
            elif note == "I":
                my_music.change_instrument(timing)
            # otherwise, send it to first function, return integer, play the note
            else:
                note = note_to_int(note)
                my_music.play_note(note, timing)


def menu_play_song():
    # get song file
    song = get_song_file()
    # play the song
    play_song(song)


def main():
    choice = 0

    while choice != 3:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            menu_play_scale()
        elif choice == 2:
            menu_play_song()

    print('Goodbye!')


main()

my_music.close()
