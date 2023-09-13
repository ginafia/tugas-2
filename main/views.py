from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'myname': 'Gina Afia',
        'myclass': 'PBP B',
        'name': 'Six of Crows',
        'description': 'Young adult fantasy series',
        'amount': '5'
    }

    return render(request, "main.html", context)