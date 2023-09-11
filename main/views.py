from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Six of Crows',
        'description': 'Young adult fantasy series',
        'amount': '5'
    }

    return render(request, "main.html", context)