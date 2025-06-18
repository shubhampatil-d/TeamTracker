from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm, LoginForm, ProjectForm, TaskForm
from .models import Project, Task
from django.contrib.auth.forms import AuthenticationForm


def home_redirect_view(request):
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            from .models import Organization
            default_org = Organization.objects.first()
            user.organization = default_org
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        next_url = request.POST.get('next', '')

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # ✅ Redirect safely to next or dashboard
            if next_url:
                return redirect(next_url)
            return redirect('dashboard')
    else:
        form = AuthenticationForm(request)

    return render(request, 'core/login.html', {'form': form, 'next': next_url})


@login_required
def dashboard_view(request):
    user= request.user
    if user.role == 'ADMIN':
        projects = Project.objects.filter(organization=user.organization)
    elif user.role == 'MANAGER':
        projects = Project.objects.filter(created_by=user)
    else:
        projects = Project.objects.filter(tasks__assigned_to=user).distinct()

    return render(request, 'core/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def is_admin_or_manager(user):
    return user.role in ["ADMIN","MANAGER"]

def project_list(req):
    projects= Project.objects.filter(organization= req.user.organization)
    return render(req, 'core/project_list.html', {'projects': projects})

@login_required
@user_passes_test(is_admin_or_manager)
def project_create(req):
    if req.method== 'POST':
        form = ProjectForm(req.POST)
        if form.is_valid():
            project= form.save(commit=False)
            project.organization= req.user.organization
            project.created_by= req.user
            project.save()
            return redirect('project_list')
    else:
        form= ProjectForm()
    return render(req, 'core/project_form.html',  {'form': form})

@login_required
def task_list(req, project_id):
    project = Project.objects.get(id= project_id)
    tasks= Task.objects.filter(project=project)
    return render(req, 'core/task_list.html',{'project':project, 'tasks':tasks})


def task_create(req, project_id):
    project= Project.objects.get(id=project_id)
    if req.method=="POST":
        form = TaskForm(req.POST)
        if form.is_valid():
            task= form.save(commit=False)
            task.project= project
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form= TaskForm(initial={'project':project})
    return render(req, 'core/task_form.html', {'form': form, 'project':project})
