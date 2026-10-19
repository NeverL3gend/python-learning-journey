# CHALLENGE #2 - GAMING HOURS CALCULATOR
# PROBLEM:
# 1. Ask the player for their gaming username.
# 2. Ask how many hours they play each day.
# 3. Calculate weekly gaming hours (daily hours * 7).
# 4. Calculate yearly gaming hours (daily hours * 365).
# 5. Display their username, daily, weekly, and yearly hours.
#
# MY ANSWER:

name = input("What is your gaming username?:")
time_played = int(input("How many hours do you play daily?:"))
weekly_hours = time_played * 7
yearly_hours = time_played * 365

print("Username:", name)
print("Daily Hours:", time_played)
print("Weekly Hours:", weekly_hours)
print("Yearly Hours: ", yearly_hours)
