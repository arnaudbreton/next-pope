# Create your views here.
import json
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from quizz.forms import PopeCandidateForm
from quizz.models import PopeCandidate

def home(request):
    if request.method == 'GET':
        return render_to_response('quizz.html', {'form': PopeCandidateForm()}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        form = PopeCandidateForm(request.POST)

        if form.is_valid():
            form.save()
            score = (form.instance.get_score()/PopeCandidate.MAX_SCORE)*100
            return HttpResponse(content=json.dumps({'message':'', 'score': score}))
        else:
            return HttpResponseServerError()
