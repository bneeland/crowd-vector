import random

people = [
    ['Garth', 'Garth@example.com'],
    ['Jo', 'Jo@example.com'],
    ['Kris', 'Kris@example.com'],
    ['Denver', 'Denver@example.com'],
    ['Kara', 'Kara@example.com'],
    ['Dana', 'Dana@example.com'],
    ['Brian', 'Brian@example.com'],
    ['Kjell', 'Kjell@example.com'],
    ['Renee', 'Renee@example.com'],
]

random.shuffle(people)

people_dict = {person[0]:person[1] for person in people}

# Just converting list to dictionary
for person_dict in people_dict:
    print(person_dict)

# Legend: [Person1, Person1]--Person1 must give to Person2
inclusions = []

# Legend: [Person1, Person1]--Person1 must not give to Person2
exclusions = [
    ['Garth', 'Jo'],
    ['Jo', 'Garth'],
    ['Denver', 'Kara'],
    ['Kara', 'Denver'],
    ['Dana', 'Brian'],
    ['Brian', 'Dana'],
    ['Kjell', 'Renee'],
    ['Renee', 'Kjell'],
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

print(people_dict.keys(), len(people_dict))
print(vectors.keys(), len(vectors.keys()))
print(vectors.values(), len(vectors.values()))
