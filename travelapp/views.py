# from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import place1


def fun(request):
    # obj=place()
    # obj.name="kerala"
    # obj.descp="Gods own country"
    # obj.price=100
    obj = place.objects.all()
    return render(request, "index.html", {'result': obj})


def fun1(request):
    obj1 = place1.objects.all()
    return render(request, "index.html", {'results': obj1})

#
# def addition(request):
#     num1 = int(request.POST["num1"])
#     num2 = int(request.POST["num2"])
#     num3 = num1+num2
#     return render(request, "result.html", {'add': num3})

# Create your views here.
