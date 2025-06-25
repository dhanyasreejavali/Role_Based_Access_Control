from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserUpdateForm
from .models import Team, Member


# Dashboard view (redirect based on role)
@login_required
def dashboard(request):
    user = request.user  # this is already an instance of CustomUser
    return render(request, 'accounts/dashboard.html', {'user': user})

# Admin-only view
@login_required
def admin_only_view(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("403 Forbidden: Admins only.")
    return render(request, 'accounts/admin.html')

# Manager-only view
@login_required
def manager_only_view(request):
    if request.user.role != 'manager':
        return HttpResponseForbidden("403 Forbidden: Managers only.")
    return render(request, 'accounts/manager.html')

# User-only view
@login_required
def user_only_view(request):
    if request.user.role != 'user':
        return HttpResponseForbidden("403 Forbidden: Users only.")
    return render(request, 'accounts/user.html')


@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on role
            if user.role == 'admin':
                return redirect('admin_only')
            elif user.role == 'manager':
                return redirect('manager_only')
            elif user.role == 'user':
                return redirect('user_only')
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


def home(request):
    return render(request, 'home.html')
# views.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import Team, Member

@login_required
def team_data_view(request):
    user = request.user

    if user.role == 'admin':
        # Admin can view all teams and all members
        teams = Team.objects.all()
        members = Member.objects.all()
    elif user.role == 'manager':
        # Manager can only view their own teams and members
        teams = Team.objects.filter(manager=user)
        members = Member.objects.filter(team__manager=user)
    else:
        # Regular users are not allowed to view this
        return HttpResponseForbidden("Access denied. Only admins or managers allowed.")

    return render(request, 'accounts/admin_data.html', {
        'teams': teams,
        'members': members
    })

@login_required
def admin_data_view(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("403 Forbidden: Admins only.")

    users = CustomUser.objects.all()
    teams = Team.objects.all()
    members = Member.objects.all()

    return render(request, 'accounts/admin_data.html', {
        'users': users,
        'teams': teams,
        'members': members
    })