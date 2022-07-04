from django.shortcuts import render

# Create your views here.
from .models import Users

obj = Users.objects.get(id=3)


def user_detail(request):
    template_name = 'user_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)
