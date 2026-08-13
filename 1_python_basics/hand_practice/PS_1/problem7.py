

word = "Hello World"
vowelWords = "aeiouAEIOU"
countVowel = 0


for letter in word :
    if letter in vowelWords:
        countVowel += 1
        
print(f"Count of vowel letter in string {word} is {countVowel}")


count = sum(1 for letter in word if word in vowelWords)
print(count)