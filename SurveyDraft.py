import json

f = open("answers.json", "r")
x = json.load(f)
f.close()
print(x)
print(type(x))

sum_ages = 0
lst_ages = []
for i in x:
    temp= i["How old are you? "]
    if temp.isnumeric():
        age = int(temp)
        sum_ages += age
        lst_ages.append(age)
avg = sum_ages / len(x)


for s in x:
    templace = s["What state do you live in? "]
