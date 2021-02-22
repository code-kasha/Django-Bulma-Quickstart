from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from django.contrib import messages

from apps.accounts.forms import UserForm


class IndexView(TemplateView):
    template_name = "index.html"


def edit_user_details(request):
    user = request.user
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            messages.success(request, f"{user} saved succesfully!")
            return redirect("profile")

    form = UserForm(instance=user)
    return render(request, "account/edit_user.html", {"form": form})


def my_profile(request):
    return render(request, "accounts/my_profile.html")
