# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


letter = ""
while len(letter) != 1 or letter in "abcdefghijklmnopqrstuvwxyz" == False:
  letter = input("Please enter a letter from the alphabet (a-z or A-Z): ").lower()
  if letter in "aeiou" and len(letter) == 1:
    print(f"The letter {letter} is a vowel")
  elif letter in "bcdfghjklmnpqrstvwxyz" and len(letter) == 1:
    print(f"The letter {letter} is a consonant")
  else:
    print("HEY I asked for a single letter pal!")


