import random

people = [
    ['Caroline', 'caroline@example.com'],
    ['Michael', 'michael@example.com'],
    ['Elise', 'elise@example.com'],
    ['Laura', 'laura@example.com'],
    ['Brian', 'brian@example.com'],
    ['Emilie-Anne', 'emilieanne@example.com'],
]

random.shuffle(people)

print(people)

print(len(people))

# people = {person[0]:person[1] for person in people}

inclusions = [
    ['Laura', 'Elise'],
]

exclusions = [
    ['Brian', 'Michael'],
]

vectors = []

matched = False

for i, person1 in enumerate(people):
    if i == len(people)-1:
        person2 = people[0]
    else:
        person2 = people[i+1]
    print(person1[0], person2[0])
