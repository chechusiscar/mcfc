import re


def read_multiline_strings_from_file(filename):
    """
    Given the name of a file in the current directory, reads all of the lines from the file,
    and returns a list of multiline strings. The re pattern "\n\d+. " is used to split the lines.
    """
    with open(filename, "r") as f:
        # Read all lines from the file
        lines = f.readlines()
    
    # Join all lines into a single string
    lines_joined = "".join(lines)
    
    # Split the string into a list of multiline strings
    multiline_strings = re.split(r"[\n\r]+\d+.", lines_joined)

    multiline_strings[0] = multiline_strings[0].replace("1.", "")
        
    for multiline_string in range(len(multiline_strings)):
        # Remove extra whitespace from the beginning and end of each multiline string
        multiline_strings[multiline_string] = multiline_strings[multiline_string].strip()
        # Remove all tab characters from each multiline string
        multiline_strings[multiline_string] = multiline_strings[multiline_string].replace("\t", " ")
        # Replace "\s(?=[A-Za-z]\))" with "\n(?=[A-Za-z]\))"
        multiline_strings[multiline_string] = re.sub(r"\s(?=[A-Za-z]\))", r"\n", multiline_strings[multiline_string])
        multiline_strings[multiline_string] = re.sub(r"(?<=\n[A-Za-z])\)", r".", multiline_strings[multiline_string])
        # Remove multiple newlines
        multiline_strings[multiline_string] = re.sub(r"\n\s*\n", r"\n", multiline_strings[multiline_string])

    
    # Return the list of multiline strings
    return multiline_strings


    


def parse_answers(filename):
    with open(filename, "r") as f:
        # Read all lines from the file
        lines = f.readlines()
    
    # Loop all each line in the file, and add the first letter in the line to the list of answers if it's not empty
    answers = []
    for line in lines:
        if line.strip() != "":
            # Get the first character in the line that's either an uppercase or lowercase letter
            # Output: "A" or "a"
            first_letter = re.search(r"[A-Za-z]", line).group(0)
        
            # Add the first letter to the list of answers
            answers.append(first_letter)

    # Return the list of answers
    return answers



questions = read_multiline_strings_from_file("questions.txt")
answers = parse_answers("answers.txt")


def check_file(filename):
    with open(filename, "r") as f:
        # Read all lines from the file
        lines = f.readlines()
    
    accounted = []

    for line in lines:
        if line.strip() != "":
            number = re.search(r"^\d+", line)

            if number is not None:
                accounted.append(number.group(0))

    for i in range(len(questions)):
        if int(accounted[i]) != i + 1:
            print("Error at line", i + 1)

check_file("questions.txt")


# Loop through all the questions and answers, writing the question and answer to a file, replacing the current contents of the file

print(len(questions), len(answers), min(questions, key=len))    

with open("output.txt", "w") as f:
    for i in range(len(questions)):
        f.write(questions[i])
        f.write("\n\n")
        f.write(answers[i])
        f.write("\n\n\n")

