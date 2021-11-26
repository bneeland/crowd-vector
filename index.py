import random

people = [
    ['Michael', 'michael@example.com'],
    ['Laura', 'laura@example.com'],
    ['Caroline', 'caroline@example.com'],
    ['Emilie-Anne', 'emilieanne@example.com'],
    ['Dana', 'dana@example.com'],
    ['Brian', 'brian@example.com'],
    ['Elise', 'elise@example.com'],
]

random.shuffle(people)

people_dict = {person[0]:person[1] for person in people}

for person_dict in people_dict:
    print(person_dict)

# [Person1, Person1]: Person1 must give to Person2
inclusions = [
    ['Laura', 'Elise'],
    ['Michael', 'Brian'],
]

# [Person1, Person1]: Person1 must not give to Person2
exclusions = [
    ['Brian', 'Dana'],
    ['Dana', 'Brian'],
    ['Caroline', 'Emilie-Anne'],
    ['Michael', 'Elise'],
    ["Emilie-Anne", "Caroline"]
]

vectors = {}

for inclusion in inclusions:
    vectors[inclusion[0]] = inclusion[1]

print(vectors)

excluded = False
matched = False

n = 0

for i, person1 in enumerate(people):
    print("-----------")
    print(person1[0])
    matched = False
    if person1[0] not in vectors:
        if i == len(people)-1:
            n = 0
        else:
            n = i+1
        while not matched:
            excluded = False
            person2 = people[n]
            print(person2[0])
            if person2[0] in vectors.values():
                print(person2[0] + " is already a vector ending")
                if n >= len(people)-1:
                    n = 0
                else:
                    n += 1
            else:
                for exclusion in exclusions:
                    if exclusion[0] == person1[0] and exclusion[1] == person2[0]:
                        excluded = True
                        break
                if excluded:
                    print("NO MATCH", person1[0], person2[0])
                    if n >= len(people)-1:
                        n = 0
                    else:
                        n += 1
                else:
                    vectors[person1[0]] = person2[0]
                    print("MATCH", person1[0], person2[0])
                    matched = True
                    print(vectors)
    else:
        print(person1[0] + " is already a vector beginning")
