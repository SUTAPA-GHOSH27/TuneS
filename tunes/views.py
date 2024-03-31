from django.shortcuts import render
from tunes.models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import Watchlater
from .forms import CustomUserCreationForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth import logout,login



def index(request):
    song=Song.objects.all()
    return render(request, 'index.html',{'song':song})

def search(request):
    query=request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(name=query)

    return render(request, 'tunes/search.html',{"songs":qs})



def watchlater(request):
    return render(request, 'tunes/watchlater.html')

def songs(request):
    song=Song.objects.all()
    return render(request, 'tunes/songs.html',{'song':song})

def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request, 'tunes/songpost.html',{'song':song})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')  # Redirect to the index page after logout

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after signup
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to the index page after signup and login
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})




def add_to_watchlater(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        user = request.user
        try:
            Watchlater.objects.create(user=user, song_id=song_id)
            # Optionally, you can add a success message here
        except Exception as e:
            # Handle the exception
            pass
        return redirect('songpost', id=song_id)
    else:
        pass

def remove_from_watchlater(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        user = request.user
        try:
            watch_later_item = Watchlater.objects.get(user=user, song_id=song_id)
            watch_later_item.delete()
            # Optionally, you can add a success message here
        except Watchlater.DoesNotExist:
            # Handle case where the song is not in the watch later list
            pass
        except Exception as e:
            # Handle other exceptions
            pass
        return redirect('songpost', id=song_id)
    else:
        pass

def recorder_view(request):
    return render(request, 'tunes/recorder.html')