from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('new_page')
#         else:
#             messages.info(request, "invalid")
#             return redirect('credentials:login')
#     return render(request, "login.html")
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('schoolapp:new_page')
            else:
                messages.error(request, "Please try again.")
        else:
            messages.error(request, "Invalid form submission. Please check the form.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['password1']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('schoolapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('schoolapp:register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect('schoolapp:login')
        else:
            messages.info(request, "Password not matching")
            return redirect('schoolapp:register')
    return render(request, "register.html")

def department(request):
    department_wikipedia_urls = {
        "Computer Science": "https://en.wikipedia.org/wiki/Computer_science",
        "Commerce": "https://en.wikipedia.org/wiki/Commerce",
        "Social Science": "https://en.wikipedia.org/wiki/Social_science",
        "Music": "https://en.wikipedia.org/wiki/Music",
        "Physical Activity": "https://en.wikipedia.org/wiki/Physical_activity",
    }

    departments = list(department_wikipedia_urls.keys())

    if request.method == 'POST':
        selected_department = request.POST.get('department')
        wikipedia_url = department_wikipedia_urls.get(selected_department)
        if wikipedia_url:
            return redirect(wikipedia_url)
    return render(request, 'department.html', {'departments': departments})

def new_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.getlist('materials_provide')
        messages.success(request, 'Order Confirmed')
        return redirect('schoolapp:new_page')
    return render(request, 'new_page.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

