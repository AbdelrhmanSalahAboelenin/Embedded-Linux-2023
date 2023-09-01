

def is_vowel(letter):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    return letter in vowels

letter=input("Enter a letter : ")


if len(letter) == 1 and letter.isalpha():
    if is_vowel(letter):
         print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")
else:
    print("Please enter a single letter.")





