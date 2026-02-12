from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date, datetime

from .forms import RegisterForm, ExpenseForm, LoginForm
from .models import Expense, User


# ---------- HOME ----------
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

# ---------- REGISTER ----------
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user) # Automatically log in the user after registration
        return redirect('dashboard')

    return render(request,'register.html',{'form':form})


# ---------- LOGIN ----------
def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        # Find user by email
        user_obj = User.objects.filter(email=email).first()
        
        if user_obj:
            user = authenticate(username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        
        # If login fails
        form.add_error(None, "Invalid email or password")
    
    return render(request, 'login.html', {'form': form})


# ---------- LOGOUT ----------
def user_logout(request):
    logout(request)
    return redirect('login')


# ---------- DASHBOARD ----------
@login_required
def dashboard(request):

    expenses = Expense.objects.filter(user=request.user)

    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    today = expenses.filter(date=date.today()).aggregate(Sum('amount'))['amount__sum'] or 0
    month = datetime.now().month
    monthly = expenses.filter(date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0

    category_data = expenses.values('category').annotate(total=Sum('amount'))
    
    # Prepare data for charts (e.g. Chart.js)
    chart_labels = [item['category'] for item in category_data]
    chart_data = [float(item['total']) for item in category_data]
    
    recent = expenses.order_by('-id')[:5]

    return render(request,'dashboard.html',{
        'total':total,
        'today':today,
        'monthly':monthly,
        'category_data':category_data,
        'recent':recent,
        'chart_labels': chart_labels,
        'chart_data': chart_data
    })


# ---------- ADD ----------
@login_required
def add_expense(request):
    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('dashboard')

    return render(request,'add.html',{'form':form})


# ---------- UPDATE ----------
@login_required
def update_expense(request,id):
    obj = get_object_or_404(Expense, id=id, user=request.user)
    form = ExpenseForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request,'add.html',{'form':form})


# ---------- DELETE ----------
@login_required
def delete_expense(request,id):
    obj = get_object_or_404(Expense, id=id, user=request.user)
    obj.delete()
    return redirect('dashboard')
