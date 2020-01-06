
if __name__ == "__main__":

    # This file will discuss how to read files. When reading data files, one traditionally uses the pandas library.
    # However, this file will discuss the traditional form of reading files.

    # Open a file using the open function, with the second argument as "r"

    aFile = open("../ChapterTwoInstructions.txt", "r")

    # Python for loops are beautiful, let us use them as so...

    for line in aFile:

        # Get rid of any extra whitespace like 'enter's at the end

        line = line.strip()

        print(line)
