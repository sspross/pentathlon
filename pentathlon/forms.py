from django import forms

from event.models import Participation

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ('player', 'giant_slalom_equipment', 'jump_equipment',)

    def __init__(self, team, *args, **kwargs):
        super(ParticipationForm, self).__init__(*args, **kwargs)
        self.instance.team = team
