from allauth.account.views import SignupView, LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import AccountSignupForm, SupplierSignupForm



class AccountSignupView(SignupView):
    form_class = AccountSignupForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('order')


class AccountLoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = reverse_lazy('order')


def account_logout_view(request):
    logout(request)
    return redirect("index")


account_signup_view = AccountSignupView.as_view()
account_login_view = AccountLoginView.as_view()


#https://stackoverflow.com/questions/44505242/multiple-user-type-sign-up-with-django-allauth

# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
# https://github.com/sibtc/django-multiple-user-types-example/tree/c1aaa062d91bbe70f408a07026570bf2b2349d6a

class SupplierSignupView(SignupView):
    form_class = SupplierSignupForm
    template_name = 'auth/supplier_signup.html'
    success_url = reverse_lazy('supplier_profile')


class SupplierLoginView(LoginView):
    template_name = 'auth/supplier_login.html'
    success_url = reverse_lazy('supplier_profile')


def supplier_logout_view(request):
    logout(request)
    return redirect("index")


supplier_signup_view = SupplierSignupView.as_view()
supplier_login_view = SupplierLoginView.as_view()
