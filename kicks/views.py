from django.shortcuts import render
from .models import User
from django.shortcuts import render , redirect
from .forms import MemberForm
from .models import Member

from django.contrib import admin
from .models import Member
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'kicks/index.html', {'users': users})

def addmembers(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('membersList')  # Redirect to a success page after submission
    else:
        form = MemberForm()
    
    return render(request, 'kicks/addMember.html', {'form': form})

# View to display the list of members
def members_list(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'kicks/membersList.html', {'members': members})

def memberslist(request):
    members = Member.objects.all()
    return render(request, 'kicks/memberslist.html', {'members': members})
