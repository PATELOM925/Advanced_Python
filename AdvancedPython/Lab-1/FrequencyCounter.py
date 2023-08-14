from collections import Counter

def frequencyCounter(word):
    word = word.lower() #converting the word to lowercase
    letter_freq = Counter(word) 
    two_most_freq_letter = letter_freq.most_common(2)
    
    return two_most_freq_letter

input = input("Enter any word")
top_two = frequencyCounter(input)

for letters,frequency in top_two:
    print("{}: {}: frequecny".format(letters,frequency))
    
    