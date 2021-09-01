from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'bouquet_tips/bouquet_tips.html')
