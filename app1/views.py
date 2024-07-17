from django import forms
from django.shortcuts import render, redirect
from .models import Department, User, PrettyNum

# Create your views here.
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


def add_department(request):
    if request.method == 'GET':
        return render(request, "add_department.html")
    # POST => new dep
    new_department = request.POST['new_department']
    Department.objects.create(title=new_department)
    return redirect('/department/')

def delete_department(request, id):
    Department.objects.get(id=id).delete()
    return redirect('/department/')

def edit_department(request, id):
    department = Department.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit_department.html', {'department': department})
    department.title = request.POST['department_title']
    department.save()
    return redirect('/department/')

# ModelForm

class UserMf(forms.ModelForm):
    password = forms.CharField(min_length=8, label='PSW')
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'department', 'gender')
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'username': forms.TextInput(),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # widget on template
            # name => field defined name
            # field => record
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

def user_list(request):
    form = UserMf()
    users = User.objects.all()
    return render(request, 'user_list.html', {'form': form, 'users': users})

def add_user(request):
    if request.method == 'GET':
        form = UserMf()
        return render(request, "add_user.html", {'form': form})
    # create records / traditional method
    # username = request.POST['username']
    # email = request.POST['email']
    # password = request.POST['password']
    # department = request.POST['department']
    # gender = request.POST['gender']
    # User.objects.create(username=username, email=email, password=password, department_id=department, gender=gender)

    #modelform
    form = UserMf(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/")
    else:
        return render(request, 'add_user.html', {'form': form})

def edit_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'GET':
        user_record = UserMf(instance=user)
        return render(request, 'edit_user.html', {'form': user_record})

    form = UserMf(data=request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/user/")

def delete_user(request, id):
    # user = User.objects.get(id=id)
    # user.delete()
    User.objects.get(id=id).delete()
    return redirect("/user/")

#PrettyNum################################################################################

class PrettyNumMf(forms.ModelForm):
    class Meta:
        model = PrettyNum
        fields = ('mobile', 'price', 'level', 'state')
        # overwrite by __ini__
        # widgets = {
        #     "price": forms.NumberInput(attrs={'step': 'any'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # widget on template
            # name => field defined name
            # field => record
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
            if name == 'price':
                field.widget.attrs.update({'step':'any'})

def prettynum_list(request):
    prettynummf = PrettyNumMf()
    prettynum_queryset = PrettyNum.objects.all().order_by('id')
    print(prettynum_queryset)
    return render(request, "prettynum_list.html", {'form': prettynummf, 'prettynum_list': prettynum_queryset})

def add_prettynum(request):
    prettynummf = PrettyNumMf()
    if request.method == 'GET':
        return render(request, 'add_prettynum.html', {'form': prettynummf})
    form = PrettyNumMf(data=request.POST)
    # form is html code with post data
    if form.is_valid():
        form.save()
        return redirect("/prettynum/")