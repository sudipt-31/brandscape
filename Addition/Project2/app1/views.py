from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        result = num1 + num2
        return render(request, 'app1/addition.html', {'result': result})
    else:
        return render(request, 'app1/addition.html')
   