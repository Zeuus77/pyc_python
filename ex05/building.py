import sys
import string

def char_count(txt):
    count = {
        "upper":0,
        "lower":0,
        "space":0,
        "digits":0,
        "punctuation":0
    }
    for char in txt:
        if char.isupper():
            count["upper"] += 1
        elif char.islower():
            count["lower"] += 1
        elif char.isspace():
            count["space"] += 1
        elif char.isdigit():
            count["digits"] += 1
        elif char in string.punctuation:
            count["punctuation"] +=1

    return count

def main():
    try:
        argc = len(sys.argv)
        if argc > 2:
            raise AssertionError("more than one argument is provided")
        if argc == 1:
            txt = input("What is the text to count?\n")
        else:
            txt = sys.argv[1]
            
        counts = char_count(txt)

        print(f"The text contains {len(txt)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['space']} space")
        print(f"{counts['digits']} digits")

    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()