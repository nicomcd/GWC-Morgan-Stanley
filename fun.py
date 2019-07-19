import random

# emptydictionary={}
# sum_age = 0
# avg_age = 0
#
# for i in range(3):
#      tempuser = input("What is your username? ")
#      tempage = input("What is your age? ")
#      tempage = int(tempage)
#      sum_age += tempage
#      emptydictionary[f"{tempuser}"] = tempage
#      avg_age = sum_age/3
# print(avg_age)
# print(emptydictionary)

prayer_leader = []
while True:
    print("\nPlease enter only one name... To stop entering names say 'stop'!")
    print(f"This is the list so far: {prayer_leader}\n")
    availablity = input("Who can come? ")
    if "stop" in availablity:
        break
    else:
        prayer_leader.append(availablity)
        continue

print("Okay... randomizing list....")
random.shuffle(prayer_leader)
print(prayer_leader)
