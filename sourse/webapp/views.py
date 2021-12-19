from django.shortcuts import render

# Create your views here.

def calculete(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')
    else:
        result = 0
        if request.POST.get("sign") == "+":
            result = int(request.POST.get("first")) + int(request.POST.get("second"))
        elif request.POST.get("sign") == "-":
            result = int(request.POST.get("first")) - int(request.POST.get("second"))
        elif request.POST.get("sign") == "*":
            result = int(request.POST.get("first")) * int(request.POST.get("second"))
        elif request.POST.get("sign") == "/" and request.POST.get("second") == "0":
            result = "cannot be divisible by 0"
        elif request.POST.get("sign") == "/":
            result = int(request.POST.get("first")) / int(request.POST.get("second"))
        context = {
            "first": request.POST.get("first"),
            "second": request.POST.get("second"),
            "sign": request.POST.get("sign"),
            "result": result
        }
        return render(request, 'calculator.html', context)
