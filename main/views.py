from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'myname': 'Gina Afia',
        'myclass': 'PBP B',
        'name1': 'Six of Crows',
        'description1': 'Young adult fantasy series',
        'amount1': 5,
        'name2': 'The Lord of The Rings: The Return of The King',
        'description2': 'Young adult fantasy series',
        'amount2': 3
    }

    return render(request, "main.html", context)