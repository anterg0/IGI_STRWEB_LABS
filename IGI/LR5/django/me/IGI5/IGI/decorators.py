from django.contrib.auth.decorators import user_passes_test

def is_employee_or_superuser(function):
    def wrap(request, *args, **kwargs):
        def test_func(user):
            return user.is_authenticated and (user.is_superuser or user.client.is_employee)
        
        actual_decorator = user_passes_test(test_func)
        return actual_decorator(function)(request, *args, **kwargs)
    
    return wrap