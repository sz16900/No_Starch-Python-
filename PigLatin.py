def PigLatin(word):
    newWord = []
    for letter in word:
        newWord.append(letter)
    newWord += newWord.pop(0)
    newWord = "".join(newWord) + "ay"
    return newWord

print(PigLatin("chao"))
