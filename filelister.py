import os

with open("file_list.txt", "w") as outputFile:
    for path, subdirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for filename in files:
            # Get the file name without the path
            file_name = os.path.basename(filename)
            # Get the file name without the extension
            file_name_without_extension = os.path.splitext(file_name)[0]
            # Remove line breaks from the file name
            file_name_without_extension = file_name_without_extension.replace("\n", "")
            # Write the file name to the output file without a newline character
            outputFile.write(file_name_without_extension + "\n")
