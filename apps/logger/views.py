from django.shortcuts import render
from django.contrib.auth import authenticate

from logger.models import RequestStore
from logger.forms import LoginForm


def logger_view(request):
    requests = RequestStore.objects.order_by('date_time')[:10]
    return render(request, 'logger/requests_list.html', {'requests': requests})
    
def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                message = 'Account inactive'
                return render(request, 'logger/auth.html', {'message': message})
        else:
            message = 'Invalid login'
            return render(request, 'logger/auth.html', {'message': message, 'form': form})
    else:
        return render(request, 'logger/auth.html', {'form': form})


