from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
# Create your views here.

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def dispatch(self, request,  *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quote_site:index")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            # username = form.cleaned_data["username"]
            messages.success(request, f"Your account was successfully created!")
            return redirect(to="users:login")

        return render(request, self.template_name, {"form": self.form_class()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('users:logout')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quote_site:index')

    return render(request, 'users/login.html', context={"form": LoginForm()})