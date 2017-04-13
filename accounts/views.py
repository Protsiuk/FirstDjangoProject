from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from accounts.forms import LoginForm


def home_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(email=data.get("email"), password=data.get("password"))
            if user:
                login(request, user)
            else:
                print("sorry")
    #
    #         print("valid")
    # # logic auth
    #     else:
    #         print("NOT VALID")
    # # logic error
    return render(request, "home_page.html", {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
