# CHALLENGE #3 - GAMING SKILL CLASSIFICATION
# PROBLEM:
# 1. Ask the player for their username and daily gaming hours.
# 2. Classify the player using if / elif / else:
#    - 0-2 hours: Casual Gamer
#    - 3-5 hours: Regular Gamer
#    - 6+ hours: Hardcore Gamer
# 3. Display their username, daily hours, and classification.
#
# MY ANSWER (original submitted solution):

name = input("What is your username? ")
daily_gaming = int(input("How many hours do you play daily? "))

if daily_gaming <= 2:
  print ("Casual Gamer")
elif daily_gaming >= 3 and daily_gaming <= 5:
  print ("Regular Gamer")
else: 
  print ("Hardcore Gamer")
