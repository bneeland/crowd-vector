from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from . import forms

from . import methods

class AssignerView(FormView):
    template_name = 'simple_gifts/assigner_view.html'
    form_class = forms.AssignerForm
    success_url = reverse_lazy('assigner_view')

    def form_valid(self, form):
        data = form.cleaned_data
        names = data['names'].split('\r\n')
        emails = data['emails'].split('\r\n')
        people = [[name, email] for name, email in zip(names, emails)]
        print(people)
        people_list, people_dict = methods.randomize_people(people)
        print(people_list)
        print(people_dict)
        inclusions = data['inclusions'].split('\r\n')
        exclusions = data['exclusions'].split('\r\n')
        print(inclusions)
        print(exclusions)
        inclusions = [inclusion.split(',') for inclusion in inclusions]
        if inclusions == [['']]:
            inclusions = []
        exclusions = [exclusion.split(',') for exclusion in exclusions]
        if exclusions == [['']]:
            exclusions = []
        print(inclusions)
        print(exclusions)
        # try:
        vectors = methods.get_vectors(people_list, people_dict, inclusions, exclusions)
        print(vectors)

        for vector in vectors.items():
            vector_a = vector[0]
            vector_b = vector[1]
            # try:
            send_mail(
                subject="Christmas 2021 gift exchange - Your randomly-assigned giftee",
                message=f"--------------------------------\nTO: {vector_a}\nFROM: Gift exhange random assignment program\nRE: Christmas 2021 gift exchange - Your randomly-assigned giftee\n--------------------------------\n\nDear {vector_a},\n\nThis email is an automated message from a gift exhange random assignment program. The program has assigned names for your Christmas 2021 gift exchange.\n\nThe name it 'drew' for you is:\n\n{vector_b}\n\nYou will, therefore, give a gift to {vector_b}. Someone else will have 'drawn' your name, and will give you a gift for Christmas!\n\nMerry Christmas!",
                from_email='Simple Gifts App <hello@simplegiftsapp.com>',
                recipient_list=[people_dict[vector_a]],
                fail_silently=True,
                html_message=f"--------------------------------<br>TO: {vector_a}\nFROM: Gift exhange random assignment program\nRE: Christmas 2021 gift exchange - Your randomly-assigned giftee<br>--------------------------------<br><br>Dear {vector_a},\n\nThis email is an automated message from a gift exhange random assignment program. The program has assigned names for your Christmas 2021 gift exchange.\n\nThe name it 'drew' for you is:<br><br><b>{vector_b}</b><br><br>You will, therefore, give a gift to {vector_b}. Someone else will have 'drawn' your name, and will give you a gift for Christmas!\n\nMerry Christmas!",
            )
            # except:
            #     print(f"Failed sending email to: {vector_a}")

        # except:
        #     print("get_vectors failed")



        return super().form_valid(form)
