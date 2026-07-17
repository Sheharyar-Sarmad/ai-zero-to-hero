

word = "Hello world"
vowels = "aeiouAEIOU"

countVowels = 0
countConsonants = 0

for char in word :
    if char.isalpha() :
        if char in vowels :
            countVowels += 1
        else :
            countConsonants += 1
        
print(countVowels)
print(countConsonants)