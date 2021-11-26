import random
import smtplib
import os

def get_vectors(people_list, people_dict, inclusions, exclusions):
    vectors = {}

    for inclusion in inclusions:
        vectors[inclusion[0]] = inclusion[1]

    # print(vectors)

    excluded = False
    matched = False

    n = 0

    for i, person1 in enumerate(people_list):
        # print("-----------")
        # print(person1[0])
        matched = False
        if person1[0] not in vectors:
            if i == len(people_list)-1:
                n = 0
            else:
                n = i+1
            while not matched:
                excluded = False
                person2 = people_list[n]
                # print(person2[0])
                if person2[0] in vectors.values():
                    # print(person2[0] + " is already a vector ending")
                    if n >= len(people_list)-1:
                        n = 0
                    else:
                        n += 1
                else:
                    for exclusion in exclusions:
                        if exclusion[0] == person1[0] and exclusion[1] == person2[0]:
                            excluded = True
                            break
                    if excluded:
                        # print("NO MATCH", person1[0], person2[0])
                        if n >= len(people_list)-1:
                            n = 0
                        else:
                            n += 1
                    else:
                        vectors[person1[0]] = person2[0]
                        # print("MATCH", person1[0], person2[0])
                        matched = True
                        # print(vectors)
        # else:
        #     print(person1[0] + " is already a vector beginning")

    # print(people_dict.keys(), len(people_dict))
    # print(vectors.keys(), len(vectors.keys()))
    # print(vectors.values(), len(vectors.values()))

    return vectors

def send_email(vector_beginning_email, vector_ending):
    GMAIL_ADDRESS = os.environ.get('GMAIL_ADDRESS')
    GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(GMAIL_ADDRESS, GMAIL_PASSWORD)

        subject = "Christmas gift exchange - Here is the name that was draw for you"
        body = f"This email is an automated message from a gift exhange random pairing program. The name it drew for you is {vector_ending}. You will, therefore, give a gift to {vector_ending}. Someone else will have drawn your name, and will give you a gift for Christmas!"
        msg = f'Subject: {subject}\n\n{body}'

        SENDER = 'Crowd Vector'
        RECEIVER = vector_beginning_email

        smtp.sendmail(SENDER, RECEIVER, msg)

people_list = [
    # ['Garth', 'Garth@example.com'],
    # ['Jo', 'Jo@example.com'],
    ['Kris', 'Kris@example.com'],
    ['Denver', 'Denver@example.com'],
    ['Kara', 'Kara@example.com'],
    ['Dana', 'Dana@example.com'],
    ['Brian', 'brian.neeland@gmail.com'],
    ['Kjell', 'Kjell@example.com'],
    ['Renee', 'Renee@example.com'],
]

random.shuffle(people_list)

# Convert list to dictionary
people_dict = {person[0]:person[1] for person in people_list}

# for person_dict in people_dict:
#     print(person_dict)




# Legend: [Person1, Person1]--Person1 must give to Person2
inclusions = []

# Legend: [Person1, Person1]--Person1 must not give to Person2
exclusions = [
    # ['Garth', 'Jo'],
    # ['Jo', 'Garth'],
    ['Denver', 'Kara'],
    ['Kara', 'Denver'],
    ['Dana', 'Brian'],
    ['Brian', 'Dana'],
    ['Kjell', 'Renee'],
    ['Renee', 'Kjell'],
    # ['Brian', 'Kara'],
    # ['Brian', 'Renee'],
    # ['Renee', 'Brian'],
    # ['Renee', 'Kara'],
    # ['Kara', 'Renee'],
    # ['Kara', 'Brian']
]

vectors = get_vectors(people_list, people_dict, inclusions, exclusions)

print(vectors)

for vector in vectors.items():
    print(vector)
    print(vector[0])
    print(vector[1])
    print(people_dict[vector[0]])
    print(people_dict[vector[1]])
    vector_beginning = vector[0]
    vector_ending = vector[1]
    vector_beginning_email = people_dict[vector_beginning]
    vector_ending_email = people_dict[vector_ending]
    send_email(vector_beginning_email, vector_ending)
