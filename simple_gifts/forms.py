from django import forms

class AssignerForm(forms.Form):
    names = forms.CharField(widget=forms.Textarea, help_text='Enter each name on a separate line.')
    emails = forms.CharField(widget=forms.Textarea, help_text='Enter each email, in the same order as the names, on a separate line.')
    inclusions = forms.CharField(widget=forms.Textarea, help_text='Enter the name of the person who must send, then a comma, then the name of the person who must receive from that sender. The format should look like: Sender,Receiver (e.g. Jane,Dave). Names should be spelled exactly as they are entered under the Names field, above. Enter one sender-receiver pair per line (i.e. If you want Jane to give to Dave, then enter Jane,Dave. If you want Jane and Dave to give to each other, enter Jane,Dave and Dave,Jane.).', required=False)
    exclusions = forms.CharField(widget=forms.Textarea, help_text='Enter the name of the person who shall not send, then a comma, then the name of the person who must not receive from that sender. The format should look like: Sender,Receiver (e.g. John,Mary). Names should be spelled exactly as they are entered under the Names field, above. Enter one sender-receiver pair per line (i.e. if you want John not to give to Mary, then enter John,Mary. If you want John and Mary not to give to each other, enter John,Mary and Mary,John.', required=False)
