from django import forms

class AssignerForm(forms.Form):
    names = forms.CharField(widget=forms.Textarea, help_text='Enter each name on a separate line.')
    emails = forms.CharField(widget=forms.Textarea, help_text='Enter each email, in the same order as the names, on a separate line.')
    inclusions = forms.CharField(widget=forms.Textarea, help_text='Enter the name of the person who must send, then a comma, then the name of the person who must receive from that sender. The format should look like: SENDER_NAME,RECEIVER_NAME. One sender-receiver pair per line.', required=False)
    exclusions = forms.CharField(widget=forms.Textarea, help_text='Enter the name of the person who shall not send, then a comma, then the name of the person who must not receive from that sender. The format should look like: SENDER_NAME,RECEIVER_NAME. One sender-receiver pair per line.', required=False)
