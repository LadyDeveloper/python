#TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    list_name = names.readlines()

with open("./Input/Letters/starting_letter.docx") as letters:
    letter_content = letters.read()
    for name in list_name:
        stripped_name =  name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp