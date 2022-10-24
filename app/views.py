
from django.shortcuts import render
from app.forms import HelloForm


# Create your views here.

def root(request):
    print(request.POST)
    return render(request, 'root.html')


def hey_views(request):
    form = HelloForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        return render(request, "hello.html", {"name": name})
    else:
        return render(request, "hello.html")


def age_in_views(request, end, birth):
    return render(request, f"{end - birth}")


def order_views(request, burgers, fries, drinks):
    return render(request, f"{(burgers * 4.5) + (fries * 1.5) + drinks}")
