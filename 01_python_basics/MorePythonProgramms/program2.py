

def PalindromeText(text : str) -> str :
    
    reversedText = text[::-1].lower()
    text = text.lower()
    
    if text == reversedText :
        return "\nPalindrome text!\n"
        
    else :
        return "\nNot Palindrome text!\n"        
    
text = input("\n\nEnter a name to check, if it is Palindrome or not: \n\n")

if __name__ == "__main__" :
    print(PalindromeText(text))