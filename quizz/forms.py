__author__ = 'arnaud'
from quizz.models import PopeCandidate
from django.forms import ModelForm

class PopeCandidateForm(ModelForm):
    class Meta:
        model = PopeCandidate