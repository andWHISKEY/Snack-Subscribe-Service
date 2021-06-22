from django.shortcuts import render
from .models import *
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def recommend(request):
    return render(request,'recommend.html')

def subscribe(request):
    return render(request,'subscribe.html')

def shopping(request):
    return render(request,'shopping.html')

def payment(request):
    return render(request,'payment.html')

def result(request):
    group1=request.POST['group1']
    group2=request.POST['group2']
    group3=request.POST['group3']
    group4=request.POST['group4']
    group5=request.POST['group5']

    with_who=group1
    texture=group2
    flavor=group3
    is_one_time=group4
    situation=group5

    snacks_result1 = Snack.objects.filter(with_who__icontains = group1)
    if len(snacks_result1) > 3:
        random.shuffle(snacks_result1)
        snacks_result1 = snacks_result1[0:3]
    
    snacks_result2 = Snack.objects.filter(texture__icontains = group2)
    if len(snacks_result2) > 3:
        random.shuffle(snacks_result2)
        snacks_result2 = snacks_result2[0:3]

    snacks_result3 = Snack.objects.filter(flavor__icontains = group3)
    if len(snacks_result3) > 3:
        random.shuffle(snacks_result3)
        snacks_result3 = snacks_result3[0:3]

    snacks_result4 = Snack.objects.filter(is_one_time__icontains = group4)
    if len(snacks_result4) > 3:
        random.shuffle(snacks_result4)
        snacks_result4 = snacks_result4[0:3]

    snacks_result5 = Snack.objects.filter(situation__icontains = group5)
    if len(snacks_result5) > 3:
        random.shuffle(snacks_result5)
        snacks_result5 = snacks_result5[0:3]

    return render(request,'result.html', {'snacks_result1':snacks_result1,
                                        'snacks_result2':snacks_result2,
                                        'snacks_result3':snacks_result3,
                                        'snacks_result4':snacks_result4,
                                        'snacks_result5':snacks_result5,
                                        'with_who':with_who,
                                        'texture':texture,
                                        'flavor':flavor,
                                        'is_one_time':is_one_time,
                                        'situation':situation})

def mypage(request):
    return render(request,'mypage.html')
