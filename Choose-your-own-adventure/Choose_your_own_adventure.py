from logging import WARN


print("\nHello! I have a story to tell you about a solder making his way to the frontlines. Please answer the following questions before we begin.")

keepGoing = "yes"
while keepGoing.lower() == "yes":
    
    warName = input("\nWhat war is your solder taking place?  ")
    while len(warName) ==0:
        warName = input("War name can not be blank! Please enter a War name!  ")
    else:
        print(f"\nWelcome to the frontlines of {warName}.")
    
    characterRank = input("\nWhat rank is the character?  ")
    while len(characterRank) ==0:
        characterRank = input("Character rank can not be blank! Please enter a Character rank!  ")
    else:
        print(f"\nYou have enlisted as a {characterRank}.")

    timeServed = input("\nHow long has the solder been serving? Please enter a numerical value. ")
    while len(timeServed) ==0:
        timeServed = input("Time served can not be blank! Please enter a numerical value!  ")
    else:
        print(f"\nYou have seen the effects of war for {timeServed} years.")
    
    characterName = input("\nWhat is the name of the main character?  ")
    while len(characterName) ==0:
        characterName = input("Character name can not be blank! Please enter a name!  ")
    else:
        print(f"\nGood to have {characterName} back in action!")
    
    frontlineLocation = input("\nWhere is the frontline close to?  ")
    while len(frontlineLocation) ==0:
        frontlineLocation = input("frontline location can not be blank! Please enter a Location!  ")
    else:
        print(f"\nWelcome to the frontlines of {frontlineLocation}.")
    
    print(f"\n{characterRank} {characterName} is located near the frontlines of {frontlineLocation} however {characterName} is not close enough to assist his fellow solders. You must decide how your solder will assist!")

    print(f"\nWhile Traversing to the frontlines of {frontlineLocation} to support your fellow men at arms, you notice just ahead of {characterRank} {characterName} what would be a decent spot for an enemy ambush! The solders around {characterRank} {characterName} are only concerned with making it to the battle of {frontlineLocation} as quickly as possible, thus ignoring the risk.") 

    method1 = input(f"\nShould {characterRank} {characterName} lead the charge?")
    while method1 not in ["yes", "no"]:
        method1 = input("Please enter yes/no:")
    
    if method1.lower() == "yes":
        print(f"\n{characterRank} {characterName} jumps at the opportunity to lead others into battle! A burst of energy jolts through {characterRank} {characterName} and {characterName} picks up the pace to that of a lion! After a few seconds the pace begins to slow as {characterRank} {characterName} hears a distance whistling.... Dread sets in, fear and an immediate fade to black......")
    else:
        print(f"\n{characterRank} {characterName} takes a moment to gather their breath, in order to muster the courage to make it through the long day ahead. Not a second later {characterRank} {characterName} hears the other solders cry out 'RUUUUUNNNNN!!!!!' Instantly {characterRank} {characterName} finds themself on your feet. Just ahead the other solders that were leading the tip of the spear for the charge are cut down systematically by artilley fire. {characterRank} {characterName} takes cover, after a few minutes the explosions begin to calm. {characterRank} {characterName} can now advance past the souls of those braver than yourself.")

    print(f"\n{characterRank} {characterName} finds themselves dazed and confused from the artillery shelling on {frontlineLocation} Remembering your training, {characterRank} {characterName} puts there feet under themself, and recovers there breath. {characterRank} {characterName} starts advancing after seeing a group of others ahead of {characterRank} {characterName}. Instantly {timeServed} sharp pains are felt through {characterRank} {characterName} left leg.")
    method2 = input(f"\nShould {characterRank} {characterName} receive medical attention?")
    while method2 not in ["yes", "no"]:
        method2 = input("please enter yes/no:")
    
    if method2.lower() == "yes":
        print(f"\n{characterRank} {characterName} receives medical attention from the nearest {frontlineLocation} battlefield medic. The medic removes {timeServed} peices of shrapnel from {characterRank} {characterName} leg. The surgery makes {characterRank} {characterName} miss the rest of the war. The war of {warName} on the battlefields of {frontlineLocation} is over. {characterRank} {characterName} lives to fight another day.")
    else:
        print(f"\n{characterRank} {characterName} pushes through the pain. Making it to the frontlines of {warName}. It took longer than most to make it due to the {timeServed} shrapnel in {characterRank} {characterName} leg. The fighting is intense, and the warfare is violent! {characterRank} {characterName} sees a group of well entrenched enemies and preps a grenade for them. {characterRank} {characterName} pulls the pin on the grenade and {characterRank} {characterName} throws there arm back to throw the grenade. Just as {characterRank} {characterName} expects to see the grenade leaving their hand there entire body goes numb, collapsed.... the grenade is lost under your feet somewhere. Seconds feel like hours and {characterRank} {characterName} manages to grasp what feels like an egg an in attempt to save as many as possible. This is {characterRank} {characterName} final act.")

    if method1.lower() == "yes" and method2.lower() == "yes":
        print(f"\n{characterRank} {characterName} does not make it to {frontlineLocation} to support the other men during the battle of {warName}. {characterRank} {characterName} Lives to fight another day.")
    elif method1.lower() == "no" and method2.lower() == "no":
        print(f"\n{characterRank} {characterName} makes it to {frontlineLocation} to support the others, however this will be the last battle {characterRank} {characterName} will fight in. {characterRank} {characterName} succumbed to there injures, however saving many more in the process.")
    else:
        print(f"\nThe men rally around {characterRank} {characterName}, taking care of any injuries {characterRank} {characterName} has. This gives {characterRank} {characterName} the courage to lead the men into battle at the frontline of {warName}. The {frontlineLocation} is your home now, and the solders around {characterRank} {characterName} are like family. Fighting for a better tommorrow, today!")

    keepGoing = input("Do you want to play again? yes/no?")
    while keepGoing.lower() not in ["yes", "no"]:
        keepGoing = input("please enter value: yes or no:")


