from django.shortcuts import redirect
# from django.contrib import messages


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("________________")
            # messages.warning(request, 'You must login  first')
            return redirect('login_view')
        else:
            return fn(request, *args, **kwargs)
    return wrapper
        
