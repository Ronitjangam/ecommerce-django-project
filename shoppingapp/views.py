from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm,MyImageForm

from .models import Cataegory,Product,Cart,Order,MyImage
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
cl=Cataegory.objects.all() 
p=Product.objects.all()       
def index(request):
    p=Product.objects.all() 
    d={"catlist":cl,"plist":p}
    
    return render(request,"index.html",d)

def addUser(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        form.save()
        return redirect("/")
    else:    
        form=UserForm
        d={"form":form,"catlist":cl,"p":p}
        return render(request,"form.html",d)


def Login(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        passw=request.POST.get("passw")
        usr=authenticate(username=uname,password=passw)
        if usr is not None:
            request.session['userName']=uname
            login(request,usr)
            return redirect("/")
        else:
            return HttpResponse("invalid username or password")
    else:

        d={"catlist":cl,"p":p}
        return render(request,"Login.html",d)

def Logout(request):
    logout(request)
    return redirect("/")


def getProduct(request):
    id=request.GET.get("id")
    pl=Product.objects.filter(category_id=id)
    d={'catlist':cl,'plist':pl}
    return render(request,'index.html',d)

def searchProduct(request):
    if request.method=="POST":
        pname=request.POST.get("sp")
        pl=Product.objects.filter(pname__icontains=pname)
        d={"clist":cl,"plist":pl}
        return render(request,"searchproduct.html",d)

    else:
        pl=Product.objects.all()
        d={"clist":cl,"plist":pl}
        return render(request,"searchproduct.html",d)

def productList(request):
    pl=Product.objects.all()
    paginator = Paginator(pl, 3)
    
    pagenumber=request.GET.get("page")



    page_obj=paginator.get_page(pagenumber)

    d={"clist":cl,"page_obj":page_obj}
    return render(request,"Productlist.html",d)

def addToCart(request):
    pid=request.GET.get('pid')
    prd=Product.objects.get(id=pid)
    print("---------------------> ",prd.pname,prd.price,prd.description)
    userName=request.session.get('userName')
    usr=User.objects.get(username=userName)
    print("--------------------->",usr.username,usr.first_name,usr.last_name,usr.email)
    c=Cart()
    c.product=prd
    c.user=usr
    c.save()
    return redirect("/")

def cartList(request):
    userName=request.session.get('userName')
    usr=User.objects.get(username=userName)
    if request.method=="POST":
        totalbill=request.POST.get("bill")
        order=Order()
        order.totalbill=totalbill
        order.user=usr
        order.save()
        
        cartlist=Cart.objects.filter(user_id=usr.id)
        for i in cartlist:
            i.delete()
        return redirect("/myorder")


    else:
        cartlist=Cart.objects.filter(user_id=usr.id)
        totalbill=0
        for i in cartlist:
            totalbill=totalbill+i.product.price

        d={'catlist':cl,'cartlist':cartlist,'totalbill':totalbill}
        return render(request,"cartList.html",d)


def editProfile(request):
    userName=request.session.get("userName")
    usr=User.objects.get(username=userName)
    if request.method=="POST":
        f=UserForm(request.POST,instance=usr)
        f.save()
        return redirect("/")
    else:
        f=UserForm(instance=usr)
        d={'catlist':cl,"form":f}
        return render(request,"form.html",d)

def myorder(request):
    o=Order.objects.all()
    d={"catlist":cl,"orderlist":o}
    return render(request,"myorder.html",d)

def imagedata(request):
    if request.method=="POST":
        f=MyImageForm(request.POST,request.FILES)
        f.save()
        imagelist=MyImage.objects.all()
        f=MyImageForm
        return render(request,"imageacces.html",{'imagelist':imagelist,"form":f})

    else:
        f=MyImageForm
        imagelist=MyImage.objects.all()
        d={"imagelist":imagelist,"form":f}
        return render(request,"imageacces.html",d)


