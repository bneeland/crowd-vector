import random
import smtplib
import os

def randomize_people(people_list):
    random.shuffle(people_list)
    random.shuffle(people_list)
    random.shuffle(people_list)
    random.shuffle(people_list)

    # Convert list to dictionary
    people_dict = {person[0]:person[1] for person in people_list}

    return people_list, people_dict

def get_vectors(people_list, people_dict, inclusions, exclusions):
    vectors = {}

    for inclusion in inclusions:
        vectors[inclusion[0]] = inclusion[1]

    excluded = False
    matched = False
    iterations = 0

    n = 0

    for i, person1 in enumerate(people_list):
        matched = False
        iterations = 0
        if person1[0] not in vectors:
            if i == len(people_list)-1:
                n = 0
            else:
                n = i+1
            while not matched:
                if iterations < len(people_list)*2:
                    excluded = False
                    person2 = people_list[n]
                    if person2 == person1:
                        if n >= len(people_list)-1:
                            n = 0
                        else:
                            n += 1
                        iterations += 1
                    elif person2[0] in vectors.values():
                        if n >= len(people_list)-1:
                            n = 0
                        else:
                            n += 1
                        iterations += 1
                    else:
                        for exclusion in exclusions:
                            if exclusion[0] == person1[0] and exclusion[1] == person2[0]:
                                excluded = True
                                break
                        if excluded:
                            if n >= len(people_list)-1:
                                n = 0
                            else:
                                n += 1
                            iterations += 1
                        else:
                            vectors[person1[0]] = person2[0]
                            matched = True
                else:
                    people_list, people_dict = randomize_people(people_list)
                    vectors = get_vectors(people_list, people_dict, inclusions, exclusions)
                    return vectors
    return vectors


def print_list(list):
    print(list)
