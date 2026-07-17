
line = "Python is a my mother tongue in programming"
vowels = "aeiouAEIOU"

countVowels = 0
countConsonants = 0

for char in line :
   if char.isalpha() :
       if char in vowels :
           countVowels += 1
       else :
           countConsonants += 1
        
print(countConsonants)
print(countVowels)
