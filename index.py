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

def send_email(vector_a, vector_b):
    EXCHANGE_VECTOR_APP_ACCOUNT = os.environ.get('EXCHANGE_VECTOR_APP_ACCOUNT')
    EXCHANGE_VECTOR_APP_PASSWORD = os.environ.get('EXCHANGE_VECTOR_APP_PASSWORD')

    vector_a_email = people_dict[vector_a]

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EXCHANGE_VECTOR_APP_ACCOUNT, EXCHANGE_VECTOR_APP_PASSWORD)

        subject = "Christmas 2021 gift exchange - Your randomly-assigned giftee"
        body = f"--------------------------------\nTO: {vector_a}\nFROM: Gift exhange random assignment program\nRE: Christmas 2021 gift exchange - Your randomly-assigned giftee\n--------------------------------\n\nDear {vector_a},\n\nThis email is an automated message from a gift exhange random assignment program. The program has assigned names for your Christmas 2021 gift exchange.\n\nThe name it 'drew' for you is:\n\n{vector_b}\n\nYou will, therefore, give a gift to {vector_b}. Someone else will have 'drawn' your name, and will give you a gift for Christmas!\n\nMerry Christmas!"
        msg = f'Subject: {subject}\n\n{body}'

        SENDER = EXCHANGE_VECTOR_APP_ACCOUNT
        RECEIVER = vector_a_email

        smtp.sendmail(SENDER, RECEIVER, msg)

people_list = [
    ['Kris', 'petterson0202@gmail.com'],
    ['Denver', 'denverpetterson@gmail.com'],
    ['Kara', 'karasautner@gmail.com'],
    ['Dana', 'petterson.dana@gmail.com'],
    ['Brian', 'brian.neeland@gmail.com'],
    ['Kjell', 'kpetters@ualberta.ca'],
    ['Renee', 'resimpson92@gmail.com'],
]

# Legend: [Person1, Person1]--Person1 must give to Person2
inclusions = []

# Legend: [Person1, Person1]--Person1 must not give to Person2
exclusions = [
    ['Denver', 'Kara'],
    ['Kara', 'Denver'],
    ['Dana', 'Brian'],
    ['Brian', 'Dana'],
    ['Kjell', 'Renee'],
    ['Renee', 'Kjell'],
]

people_list, people_dict = randomize_people(people_list)

vectors = get_vectors(people_list, people_dict, inclusions, exclusions)

for vector in vectors.items():
    vector_a = vector[0]
    vector_b = vector[1]
    try:
        send_email(vector_a, vector_b)
    except:
        print(f"Sending email failed to {vector_a}")
