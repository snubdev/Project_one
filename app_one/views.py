from django.shortcuts import render
from .forms import UsuarioForm


def form(request):
    if request.method == 'POST':
        new_form = UsuarioForm(request.POST)
        if new_form.is_valid():
            new_form.save()
    else:
        new_form = UsuarioForm()

    return render(request, 'form.html', {'new_form': new_form})
