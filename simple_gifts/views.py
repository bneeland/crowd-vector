from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from . import forms

from . import methods

class AssignerView(FormView):
    template_name = 'simple_gifts/assigner_view.html'
    form_class = forms.AssignerForm
    success_url = reverse_lazy('assigner_view')

    def form_valid(self, form):
        data = form.cleaned_data
        names = data['names'].split("\r\n")
        emails = data['emails'].split("\r\n")
        people = [[name, email] for name, email in zip(names, emails)]
        print(people)
        people_list, people_dict = methods.randomize_people(people)
        print(people_list)
        print(people_dict)
        inclusions = []
        exclusions = []
        vectors = methods.get_vectors(people_list, people_dict, inclusions, exclusions)
        print(vectors)
        return super().form_valid(form)
