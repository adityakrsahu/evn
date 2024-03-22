from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return render(request,'home.html')


# def home(request,pk):
#     id=pk   #**2
#     return render(request,'home.html',{'key':id})


# def home(request,name):
#     id=name   #**2
#     return render(request,'home.html',{'key':id})



# def home(request,id):
#     id=id   #**2
#     return render(request,'home.html',{'key':id})



def combination(request,pk,name,id):
    data={
        'data1':pk,
        'data2':name,
        'data3':id
    }
    return render(request,'home.html',{'key':data})


