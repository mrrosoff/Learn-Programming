
if __name__ == "__main__":

    # This file will discuss how to read files. When reading data files, one traditionally uses the pandas library.
    # However, this file will discuss the traditional form of reading files.

    # Open a file using the open function, with the second argument as "r"

    # The file path is usually relative, or based on the scripts file location. The two dots here indicate that I want
    # to start up one directory. If I wanted to access a file in the same directory, I would write "./aFile.txt"

    aFile = open("../Instructions.md", "r")

    # Python for loops are beautiful, let us use them as so...

    for line in aFile:

        # Get rid of any extra whitespace like 'enter's at the end

        line = line.strip()

        print(line)

        # You would then process the line here, instead of printing

        # You can split a line of a file on a character using line.split(" "). This example shown here is to split a
        # string variable called line based on spaces.
