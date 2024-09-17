from django.urls import reverse_lazy
from django.shortcuts import redirect

def is_employee_or_superuser(function):
    def wrap(request, *args, **kwargs):
        def test_func(user):
            return user.is_authenticated and (user.is_superuser or user.is_employee)
        
        if not test_func(request.user):
            return redirect(reverse_lazy('home'))
        
        return function(request, *args, **kwargs)
    
    return wrap

def is_auth(user):
    return not user.is_authenticated