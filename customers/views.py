from django.shortcuts import render

# Create your views here.
def accountview(request):
    return render(request, 'account.html')