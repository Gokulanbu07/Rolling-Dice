import random

def roll_dice(num_dice, num_sides):
    rolls = []  
    for _ in range(num_dice):
        roll_result = random.randint(1, num_sides)  
        rolls.append(roll_result)
    return rolls  

def display_results(rolls):
    print("Results of each roll:")
    for i, roll in enumerate(rolls, start=1):  
        print("Die", i, ":", roll)
    print("Total sum:", sum(rolls)) 

def main():
    num_dice = int(input("Enter the number of dice: ")) 
    num_sides = int(input("Enter the number of sides per die: "))
    
    rolls = roll_dice(num_dice, num_sides)
    display_results(rolls)
    
    while True:  
        reroll_option = input("Do you want to reroll some or all dice? (yes/no): ").lower()  
        if reroll_option != 'yes':
            break
        
        dice_to_reroll = input("Enter the dice you want to reroll (comma-separated, e.g., 1,3,5), or 'all' to reroll all dice: ")
        if dice_to_reroll.lower() == 'all':  
            rolls = roll_dice(num_dice, num_sides)
        else:
            dice_to_reroll = list(map(int, dice_to_reroll.split(','))) 
            for die in dice_to_reroll:  
                rolls[die - 1] = random.randint(1, num_sides) 
        display_results(rolls) 

if __name__ == "__main__":
    main() 

