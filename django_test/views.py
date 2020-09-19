from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    # return HttpResponse("<h3>It's working!</h3>")
    return render(request, "django_test/home_page.html")


def contact(request):
    # return HttpResponse("<h3>It's working!</h3>")
    return render(request, "django_test/contact_page.html", {
        'values': ['эти данные переданы из view \'contact\'', 'Наши контакты', 'Тел: 123456789', 'Skype: test_django']
    })
