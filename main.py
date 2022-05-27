# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # convert the word string into a list of individual characters
    word2char = list(word)
    word2char.sort()  # sort the characters in place

    anagram2char = list(anagram)
    anagram2char.sort()
    return (word2char == anagram2char)


str1 = input("Please enter a word: ")
str2 = input("Please enter another word: ")

print(find_anagram(str1, str2))
