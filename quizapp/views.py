from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Questions

# Create your views here.
def home(request):
    choices = Questions.CAT_CHOICES
    return render(request,
                  'quizapp/index.html',
                  {'choices': choices})

def questions(request, choice):
    ques = Questions.objects.filter(catagory__exact=choice)
    return render(request,
                  'quizapp/questions.html',
                  {'ques': ques})


def result(request):
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id=q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        eff = (score / total) * 100
    return render(request,
                  'quizapp/result.html',
                  {'score': score,
                   'eff': eff,
                   'total': total})


def about(request):
    return render(request,
                  'quizapp/about.html')
