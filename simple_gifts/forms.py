from django import forms

class AssignerForm(forms.Form):
    names = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Jane\nDave\nAlice\nBob\nMary',}
        ),
        help_text='* Required&mdash;Enter each name on a separate line.',
    )
    emails = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'jane@example.com\ndave@example.com\nalice@example.com\nbob@example.com\nmary@example.com',}
        ),
        help_text='* Required&mdash;Enter each email, in the same order as the names, on a separate line.',
    )
    inclusions = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Jane,Dave\nDave,Jane',}
        ),
        help_text='(Optional) Enter the names of the people who must be assigned to a specific person, then a comma, then the name of the person to whom this person must be assigned. The format should look like: Giver,Receiver (e.g. Jane,Dave). Names should be spelled exactly as they are entered under the Names field, above. Enter one giver-receiver pair per line (i.e. If you want Jane to give to Dave, then enter Jane,Dave. If you want Jane and Dave to give to each other, enter Jane,Dave and Dave,Jane.).',
        required=False,
    )
    exclusions = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Bob,Mary\nMary,Bob',}
        ),
        help_text='(Optional) Enter the names of the people who must not be assigned to a specific person, then a comma, then the name of the person to whom this person must not be assigned. The format should look like: Giver,Receiver (e.g. Bob,Mary). Names should be spelled exactly as they are entered under the Names field, above. Enter one giver-receiver pair per line (i.e. If you want Bob not to give to Mary, then enter Bob,Mary. If you want Bob and Mary not to give to each other, enter Bob,Mary and Mary,Bob.).',
        required=False,
    )
