from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm


def home_page(request):
    return render(request, "home.html")


@login_required(login_url="/login/")
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(email=data.get("email"), password=data.get("password"))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    print("sorry")
        return render(request, "login.html", {"form": form})

