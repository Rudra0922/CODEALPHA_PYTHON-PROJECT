import random

words = ["networking", "html", "dbms", "java", "python"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")
print("Word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("🎉 You win! The word was:", word)
else:
    print("💀 Game over! The word was:", word)
