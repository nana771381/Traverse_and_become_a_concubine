import random

king = 0
prince = 0


print("Boom! I was in the back seat of the car and the car suddenly crashed. My conscious started fading away...")
print(".................")
print("I woke up while my head is in pain.....")
print("I looked around it was very unfamiliar")

print('''
\"Where am I...\" I asked.
\"5555 you're finally awake miss\" Lily, my maid answered.
\"The king is launching a ball to choose his concubines, you refused to join the ball and jumped into the lake yourself\"
\"Miss, can you please join the ball\"
''')

a = input("Do you agree to join the ball? (Y/N)").lower()

if a == "y":
    print("\"Yay! Finally you agreed to join! I'm so happy.\"")
    dress = input('''
    0 - red blossom dress
    1 - elegant dark blue gown
    2 - gothic black dress
    ''')

    print('''
    You joined the ball and you were so gorgeous everyone noticed you.    
    ''')

    if dress == 0:
        print('''
        The king noticed you but his eyes were furious.
        Red dress is a taboo because only queen are allowed to wear red dress.
        You resembled the late queen too much.
        
        The king announced to kill you and your whole family.
        
        End.
        ''')
    elif dress == 1:
        print('''
        The king noticed you. The gown you wore resembles the calmness of the ocean and it suits you a lot.
        ''')
        king += 2

    else:
        print('''
        The king just looked an eye at you and turned away. You were a bit down because you didn't get the king's 
        attention. However, you didn't notice a pair of eyes that followed you throughout the ball.
        ''')
        prince += 2

    if king == 2 or prince == 2:
        print('''
        The king chose you to become his concubine. You moved to the palace. 
        On the first day in the palace, the highest ranking concubine, Jessie summoned everyone to assemble
        during teatime. 
        
        During teatime, there were a total of 4 concubines, Jessie, you, and two other concubines.
        
        Jessie disliked you and served you a tea with a dead cockroach inside. She wants you to drink you to drink it.
        ''')

        choice = input("Will you drink the cockroach tea? (Y/N)").lower()

        if choice == "y":
            print('''
            You endure with her awful request and decides to revenge her in the future.
            -------------------------
            The awful teatime experience is finally over. You endure the disgusting feeling of the tea and walks back
            to your own room.
            ''')
            direction = input("Do you turn Left or Right? (L/R)").lower()

            if direction == "l":
                print('''
                On the way back to your room, you saw the King.
                ''')
                cry = input("Do you choose to cry in front of the king? (Y/N").lower()

                if cry == "y":
                    print('''
                    The king feels pitiful of you and comforts you softly.
                    ''')
                    king += 1

                else:
                    print('''
                    You try hard not to cry in front of the King but the King feels your wronged and caress you softly.
                    ''')
                    king += 2

            else:
                print('''
                You force your tears back into your eyes while you walk back to your room with your head dejected 
                to the ground.
                
                As your head facing the ground, you saw a leg just beside your room. You raise your head and saw a 
                handsome young man looking at you deeply.
                
                He didn't say anything, but put a rose on the floor in front of your room and left.
                
                You lowered your body and picked up the rose and wrapped it in your shoulders. It was the only care 
                someone gave after enduring that humiliation.
                ''')
                prince += 2

            print('''
            After 3 months, the king finally summoned you to serve him at night.
            ''')

            dress2 = input('''
            Which dress do you choose to wear?
            0 - pink yarn dress
            1 - blue silk dress
            ''')

            if dress2 == 1:
                king += 1



                if king < 3:
                    if prince < 2:
                        print("The king didn't like you and never summoned you to serve him again. You lived in the palace"
                              "lonely ever after all")
                    else:
                        print('''
                        The king never summoned you again.
                        After 2 years...
                        
                        You met the prince coincidentally in royal garden.
                        ''')

                        if direction == "r":
                            print('''
                            You remembered the rose he gave you, the only comfort you received during your years in the
                            palace...
                            ''')


                        print('''
                        The prince took ur hand and kissed the back of ur hand, gently, as if he was treating the most
                        precious thing of his life.
                        ''')


                        print('''
                        You immediately pulled your hand away from the prince and felt nervous of what he did.
                        The prince confessed to you. 
                        ''')

                        agree = input("Do you agree to his confession? (Y/N)").lower()

                        random_num = random.randint(0, 9)

                        if agree == "y":


                            if random_num < 4:
                                print('''
                                The prince successfully took the throne from the king. He secretly changes your identity
                                and marries you. You became the queen to the new king (prince).
                                ''')

                            else:
                                print('''
                                The prince tries to overthrow the King's throne but failed. The kind killed the prince.
                                He knows your betrayal so he kills you and your family too.''')

                        else:
                            if random_num > 4:
                                print('''
                                The prince successfully overthrow the throne. You were supposed to be buried together
                                with the king. You drank the poison.....
                                    
                                But then you opened your eyes and discovered you didn't die??!!
                                    
                                The prince saved your life and kept you in the basement. The prince enslaved you.
                                ''')
                            else:
                                print('''
                                You lived lonely in the palace after all.
                                ''')

            else:
                print('''
                The king loves you a lot. He makes you his queen.
                You went to Jessie's room and gave her a mouthful of cockroach before killing her. 
                    
                You and the king lived happily ever after.
                ''')



        else:
            print("Jessie punished you in the name of being disrespectful. You have no money or power to acquire"
                  "medicine and soon dies in the palace without anyone noticing you.")


else:
    print("The king is frustrated and decided to kill you and your whole family")

print("Game Over!")
