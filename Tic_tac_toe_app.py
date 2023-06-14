try:
                pattern=[]
                #tic tac toe pattern 
                def pattern_list(pattern):
                   for pattern_i in range(9):
                          pattern.append(' ')
                          
               #tic tac toe pattern print
                def print_pattern(pattern):
                        pattern_list(pattern)
                        print(f'{pattern[0]}  | {pattern[1]} | {pattern[2]}')
                        print("---|---|---")
                        print(f'{pattern[3]}  | {pattern[4]} | {pattern[5]}')
                        print("---|---|---")
                        print(f'{pattern[6]}  | {pattern[7]} | {pattern[8]}')

                user_input_list=[]
                def user_input(player_name):
                        global player_turn
                        global user_input_list
                        player_turn=True
                        player=None
                        print("Please print a number between 1 to 9")
                        while player_turn:
                                player_list=['1','2','3','4','5','6','7','8','9']
                                while player not in player_list:
                                           player=input(f'{player_name} your turn . . . Enter a number  : ')
                                player=int(player)-1
                                if 0<= player <10:
                                        if player in user_input_list:
                                                print(f'{player_name} This position is already filled ! ! ! Try again another position > > >>>')
                                                continue
                                        user_input_list.append(player)
                                        #print(user_input_list)
                                        return player
                def winner_result(pattern,player1_name,player2_name):
                        global player_turn
                        if pattern[0]==pattern[1]==pattern[2]=='X' or pattern[3]==pattern[4]==pattern[5]=='X'or  pattern[6]==pattern[7]==pattern[8]=='X' or pattern[0]==pattern[3]==pattern[6]=='X'   or pattern[1]==pattern[4]==pattern[7]=='X' or pattern[2]==pattern[5]==pattern[8]=='X'or pattern[2]==pattern[4]==pattern[6]=='X' or pattern[0]==pattern[4]==pattern[8]=='X' :
                                    print(f'Congratulations {player1_name}. You Won the game ...!!! !!!')
                                    print("\t")
                                    print("Game Over !!! Thank You for playing Tic Tac Toe  ! ! ! . .  Play Again > > >. . . ")
                                    player_turn=False
                                    restart_game(pattern)
                                     
                        elif pattern[0]==pattern[1]==pattern[2]=='O' or pattern[3]==pattern[4]==pattern[5]=='O'or  pattern[6]==pattern[7]==pattern[8]=='O' or pattern[0]==pattern[3]==pattern[6]=='O' or pattern[1]==pattern[4]==pattern[7]=='O'or  pattern[2]==pattern[5]==pattern[8]=='O' or   pattern[2]==pattern[4]==pattern[6]=='O' or pattern[0]==pattern[4]==pattern[8]=='O':
                                    print(f'Congartulations {player2_name}. You Won the game ...!!! !!!') 
                                    print("\t")
                                    print("Game Over !!! Thank You for playing Tic Tac Toe  ! ! ! . .  Play Again > > >. . . ")
                                    player_turn=False
                                    restart_game(pattern)
                def restart_game(pattern):
                          
                          global user_input_list
                          global player_turn
                          player_turn=False
                          pattern.clear()
                          user_input_list.clear()
                          print("\t")
                          play_again=input("Restart the game !!! ... >>> > > > Enter  yes/no : ").lower()
                          if play_again=='yes':
                             pattern=[]
                             pattern_list(pattern)
                             tic_tac_toe()
                          else:
                              print("\t")
                              print("Game End ! ! ! ... Thank you for playing Tic Tac Toe... ... !!! !!!  >>> > >>")
                              exit()
                        
                def tic_tac_toe():
                        global player_turn
                        global player_list
                        print("Start the game ! ! ! >>>>")
                        print("................................")
                        print("Players... >>> Choose who is player 1 and player 2. . . The player 1 sign is 'X' and player 2 sign is 'O' . . . .")
                        player1_name=input("Player 1...>>> Enter your name : ").capitalize()
                        player2_name=input("Player 2...>>> Enter your name : ").capitalize()
                        print("\t")
                        print(f'Thank you {player1_name} >>>Player 1... and {player2_name}>>>Player 2... for joining. . . > > >>>')
                        print("\t")
                        print("Instructions are here . . . Must read!!! !!!")
                        print("-------------------------------")
                        print("1.Players take turns putting their marks in empty positions. ")
                        print("2.Insert the pattern position , enter number from 1 to 9 on keyboard.")
                        print("3.The first player to get 3 of her marks in a row (row,column or diagonal) is the winner.")
                        print("4.When all 9 squares are full, the game ends.")
                        print("5.If no player has 3 marks in a row,col or diagonal ,the game ends in a draw.")
                        print("6.Player 1 will go first")
                        print("7.Player 1 sign will always- 'X' and player 2 sign will always 'O' ")
                        print("\t")
                        print("Tic Tac Toe Pattern . . . . ")
                        print_pattern(pattern)
                        print("\t")
                        print(f'{player1_name} sign is - X ')
                        print(f'{player2_name} sign is - O')
                        print("................................")
                        print("Start. . . the game TIC TAC TOE. . . . > >>")
                        print("\t")
                        for pattern_i in range(0,9):
                                if pattern_i%2==0:
                                        user=user_input(player1_name)
                                        pattern[user]='X'
                    
                                else :
                                        user=user_input(player2_name)
                                        pattern[user]='O'
                                print_pattern(pattern)
                                winner_result(pattern,player1_name,player2_name)
                        print("Nobody Won .The game is a Draw ! ! ! . . .! ! ! ")
                        print("\t")
                        print("Game Over !!! Thank You for playing Tic Tac Toe  ! ! ! . .  Play Again > > >. . . ")
                        player_turn=False
                        restart_game(pattern)
                print("Welcome to the game Tic Tac Toe ::>> ::>> ::>>")
                print("<=====================================================>")
                tic_tac_toe()
              
except ValueError:
        print("Please try to enter the integer value  ! ! !")
        tic_tac_toe()
except TypeError:
        print("list indices must be integers or slices ,not non type....")
except IndexError:
        print("list index out of range ....")
finally:
      print("Nothing went wrong ! ! ! 'try except' is  finished . . . . ")

                        
                                        
                
                


                        
        