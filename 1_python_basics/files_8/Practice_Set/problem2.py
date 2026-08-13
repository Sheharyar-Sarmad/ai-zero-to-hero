
# Harry bhai logic
import random 

def game() :
    print("You are playing the game...")
    score = random.randint(1 , 62)
    print('')
    # Fetch the hiscore:
    with open("files_8/Practice_Set/hiscore.txt") as f :
        hiscore = f.read()
        if(hiscore != "") :
            hiscore = int(hiscore)
        else :
            hiscore = 0
    print(f"Your score is {score}")
    if(score > hiscore) :
        # write this hiscore to the file:
        with open("files_8/Practice_Set/hiscore.txt" , "w") as f :
            f.write(str(score)) 
    return score


game()

# My logic
import random
 
def gamemine(filePath , numbers) :
    print("You are playing a game: ")
    score = random.randint(numbers[0] , numbers[1])
    # Checking conditions for highscore:
    with open(filePath) as f :
        hiscore = f.read()
        if(hiscore == "") :
            hiscore = 0
        else :
            hiscore = int(hiscore)
    print(f"Your score is {score}")
    # Checking the hiscore and if the score is greater than hi score than replace it in file by score(beacuse its greater than previous hiscore):
    if(score > hiscore) :
        with open(filePath , "w") as f:
            f.write(str(score))

    return score

gamemine("files_8/Practice_Set/hiscore.txt" , [1 ,62])