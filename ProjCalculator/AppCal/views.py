from django.shortcuts import render

def indexpage_view(request):
    return render(request,'index.html')

def calculate(request):
    if request.method=='POST':
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        opt= request.POST.get('Operation')
        
        if opt=='add':
            n=n1+n2
        elif opt=='subtract':
            n=n1-n2  
        elif opt=='multiply':
            n=n1*n2  
        elif opt=='divide':
            n=n1/n2
        else:
            print("ivalid input")
            
    return render(request,'index.html',{'result':n})
