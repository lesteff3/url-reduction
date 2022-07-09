from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import ShortUrl
from .forms import ShorturlForm


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def url_shortener(request):

    template = 'shorturl/shorten_url.html'
    context = {'form': ShorturlForm()}

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        used_form = ShorturlForm(request.POST)
        if used_form.is_valid() and request.user.is_authenticated:
            shortened_object = used_form.save(commit=False)
            shortened_object.author = request.user
            shortened_object.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        else:
            context['no_user'] = "Пожалуйста зарегистрируйтесь или войдите, чтобы использовать данную функцию "
        context['errors'] = used_form.errors

        return render(request, template, context)


def view_shorturl(request, shortened_part):
    """Redirect to the original link from shortened url"""

    try:
        shorturl = ShortUrl.objects.get(short_url=shortened_part)
        shorturl.clicks += 1
        shorturl.save()
        return HttpResponseRedirect(shorturl.long_url)

    except ShortUrl.DoesNotExist:
        raise Http404("Sorry, this link is broken.")


@login_required
def view_urls(request):
    """View all the shortened urls of a logged-in user"""

    author = request.user
    data = ShortUrl.objects.all().filter(author=author)
    path = request.build_absolute_uri('/')
    context = {'data': data, 'path': path}

    return render(request, 'shorturl/view_urls.html', context)
