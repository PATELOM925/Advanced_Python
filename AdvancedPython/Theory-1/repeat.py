def repeat_letters(word):
    x = int(input("Enter the times you want to repeat your letter"))
    repeated_word = ""
    for letter in word:
        repeated_word += letter * x
    return repeated_word

word = input("Enter the word: ")
result = repeat_letters(word)
print("your desired word:", result)
