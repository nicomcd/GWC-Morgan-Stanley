###survey using list of dictionaries
import json
#
# filter = "JSON File (*.json)|*.json|All Files (*.*)|*.*||"
# filename = rs.SaveFileName("Save JSON file as", filter)

answers = []

questions = ["What's your full name? ", "Do you use social media? ", "What's your major? ", "What state do you live in? ", "How old are you? ", "What is one menthod of contact to reach you? ", "What's your social security? ", "What's your favorite food? "]

for i in range(3):
    answer = {}
    for q in questions:
        answer[q] = input(q).lower() ###adding input to answers dictionary

    print(answer)
    answers.append(answer)
    print(answers)
    print("")
    print("thanks for taking my survey, nothing to see here...")
    print("")
    user_continue = input("Continue? Y/N ").lower()
    if "n" in user_continue:
        break
    else:
        continue

# if filename:
#     # Writing JSON data
#     with open(filename, 'w') as f:
#         json.dump(datastore, f)

f = open('answers.json', 'w')
f.write(json.dumps(answers))
f.close()
