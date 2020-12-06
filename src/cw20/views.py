from django.shortcuts import render, HttpResponse
from .forms import WriteLinesForms


def form(request):
    context = {
        'form': WriteLinesForms()
    }

    if request.method == 'GET':
        return render(request, 'template_for_forms.html', context)

    elif request.method == 'POST':
        form = WriteLinesForms(request.POST)

        if not form.is_valid():
            errors = form.errors
            return HttpResponse(f'errors {errors}')

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        age = data.get('age')

        with open('cw20/file_for_data.txt', 'a') as some_file:
            some_file.write(f'{first_name}, {last_name}, {age}\n')

        with open('cw20/file_for_data.txt', 'r') as some_file:
            text = some_file.readlines()
            context['text'] = text

        return render(request, 'template_for_forms.html', context)


def erase(request):
    with open('cw20/file_for_data.txt', 'w') as some_file:
        some_file.write('')
    return render(request, 'erase_template.html')
