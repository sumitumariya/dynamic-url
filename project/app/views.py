from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html'),

def integer(request ,pk):
    data=pk
    return render (request,'home.html',{'key':data})           
def string(request ,pk):
    data=pk
    return render (request,'home.html',{'key':data}) 
def slug123(request ,pk):
    data=pk
    return render (request,'home.html',{'key':data}) 
def path123(request ,pk):
    data=pk
    return render (request,'home.html',{'key':data}) 

def combination(request,pk,id,pkid,idpk):
    data={
        'data1':pk,
        'data2':id,
        'data3':pkid,
        'data4':idpk
    }

    return render(request,'home.html',{'key':data})