from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306214510',
        'name': 'Abdul Zacky',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)