# source: https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org

def guess_game():
    secret_word = "Guessing"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = "Guessing"  # input("Enter guess: ")
            if secret_word.__contains__(guess):
                print("It's close!")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of Guesses, you lose!")
    else:
        print("You Win!")


for letter in "Academy":
    print(letter)

letters = ["A", "B", "C", "D", "E"]
for letter in letters:
    print(letter)

letters_index = len(letters)
for index in range(letters_index):
    print(letters[index])


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate("To bE or not to bE"))
