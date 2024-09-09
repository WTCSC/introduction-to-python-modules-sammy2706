"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""
# Open sample.txt as file
with open("sample.txt" , "r") as file:
    # Sets total number of lines and words to 0
    total_lines = 0
    total_words = 0
    for line in file.readlines():
        # For every line in text it adds to the total
        total_lines += 1
        # Counts the number of words in the line and adds it to the total number of words
        total_words += len(line.split(" "))
# Takes the total word and divides it by the total line to find average and rounds it down
print(f"Average words per line: {total_words // total_lines}")

