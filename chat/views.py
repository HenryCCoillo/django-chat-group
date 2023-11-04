from django.contrib.auth import login,logout,authenticate

from chat.models import Room
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm,LoginForm

def register_view(request):

    login_form = LoginForm()
    registro_form = RegisterForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, request.POST)
            if login_form.is_valid():
                
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('chat:index_view')
        
        elif 'register' in request.POST:
            registro_form = RegisterForm(request.POST)
            if registro_form.is_valid():
                user = registro_form.save()

                login(request, user)
                return redirect('chat:index_view')

    return render(request, 'chat/register.html', {'login_form': login_form, 'registro_form': registro_form})


def SignOff(request):
    logout(request)
    return redirect('chat:register_view')


@login_required
def index_view(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        room_name = request.POST.get('room-name')
        if room_name:
            chat_room, created = Room.objects.get_or_create(name=room_name)
            return redirect("chat:room_view",chat_room.slug)
    return render(request, 'chat/index_view.html', {'rooms': rooms})

@login_required
def room_view(request, room_name):
    obj = get_object_or_404(Room,slug=room_name)
    return render(request,'chat/room_view.html',{
        'name':obj.name,
        'slug':obj.slug,
        'data':obj.data,
    })