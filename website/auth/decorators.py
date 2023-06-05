from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse


def ajax_error_response(error):
    return JsonResponse({"error":"Error occured", "description": error}, status = 200)


def supplier_required_ajax(function=None):
    return supplier_required(function, login_url=ajax_error_response('not supplier'))


def customer_required_ajax(function=None):
    return customer_required(function, login_url=ajax_error_response('not customer'))


def supplier_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='supplier_login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_supplier,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def customer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='customer_login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_customer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
