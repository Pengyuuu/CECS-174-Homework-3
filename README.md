# CECS-174-Homework-3
An application that plays musical notes, scales, and entire songs according to a user's request

NOTES list: contains a series of tuples of two values each: a note letter, and  the interger value corresponding to that note

MAJOR_INTERVALS list: contains the intervals of the major scale

MINOR_INTERVALS list: contains the intervals of the minor scale

note_to_int(note): given a string representing a note, the function returns the interger value corresponding to that note

print_menu(): prints the program's main menu

get_menu_choice(): reads the user's selected menu option, validates it, and returns it

get_scale(): ask user to input the name of a scale, validate it, and returns a tuple of the integer value of the scale's note and the word "major" or "minor" depending on what scale was entered

scale_to_ints(scale): given a tuple, creates a list of 8 integers corresponding to the 8 notes of the given scale, returns the list

menu_play_scale(): implements menu option 1, "Play scale". Call get_scale to get the user's chosen scale to play, pass that scale to scale_to_ints to receive a list of notes to play, play each note one at a time

get_song_file(): ask the user to input the name of a file to play a song from

play_song(file_name): given a file name of a song file, plays the song found in that file

menu_play_song(): implements menu option 2, "Play song". Calls get_song_file to get the user's selected song file, and pass the file name to play_song
