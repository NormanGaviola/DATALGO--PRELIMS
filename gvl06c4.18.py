"""Norman Raphael M. Gaviola
   DATALOG Lab02
   March 4,2020
   I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

def isConsonant(ch):
    return ch.upper() in ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

# Returns count of consonants in str
def countConsonant(str):
    count = 0
    for i in range(len(str)):

        # Check for consonants
        if isConsonant(str[i]):
            count += 1
    return count


str = input("Type any letters: ")

print("There are ", countConsonant(str), "consonants") #prints number of consonants