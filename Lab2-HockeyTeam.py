# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
  # YOUR CODE STARTS HERE, each line must be indented (one tab)
  HokeyTeamName=input("Please enter hockey team name:")
  Wins=int(input("Please enter number of times team won:"))
  Losses=int(input("Please enter number of times team lost:"))
  ratio=(Wins/Losses)
  percentage=float((Wins/(Wins+Losses))*100)
  Rounded=round(percentage,4)
  print("The " + HokeyTeamName+" win-loss ratio is " + str(Rounded) + " and win percentage is " + str(Rounded)+"%")


    # YOUR CODE ENDS HERE

main()