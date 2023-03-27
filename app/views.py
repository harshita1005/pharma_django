from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact,Medicines,ProductItem,MyOrders

# Create your views here.
def home(request):
    return render(request,'home.html')

def medicines(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login to Order !")
        return redirect('/login')
    mymed=Medicines.objects.all()
    context={"mymed": mymed}
    print(context)
    return render(request,'medicines.html',context)


def contact(request):
    if request.method=="POST":
        fname=request.POST.get("username")
        femail=request.POST.get("email")
        fphone=request.POST.get("phone")
        fdesc=request.POST.get("desc")
        query=Contact(name=fname, email=femail,phonenumber=fphone ,desc=fdesc)
        query.save()
        messages.info(request,"Thank you for Contacting us! We will get back to you soon...")
        return redirect('/contact')
    return render(request,'contact.html')


def aboutus(request):
    return render(request,'aboutus.html')


def search(request):
    query=request.GET['search']
    if len(query)>100 :
        mymed=Medicines.objects.none()
    else:
        mymedtitle=Medicines.objects.filter(title__icontains=query)
        mymed=mymedtitle
    if mymed.count()==0:
        messages.warning(request,"No search result")
    params={'mymed':mymed,'query':query}

    return render(request,'search.html',params)


def products(request):
    myprod=ProductItem.objects.all()
    context={"myprod":myprod}
    # print(context)
    return render(request,"products.html",context)



def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")

        if password != confirmpassword:
            messages.warning(request,"Password is incorrect")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=uname):
                messages.info(request,"Username is taken")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is taken")
                return redirect('/signup')
        except:
            pass
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Sign Up Successful! Please Login")
        return redirect('/login')
    return render(request,'signup.html')






def handlelogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        password=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.info(request,"Login Successful!")
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('/login')

    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successful!")
    return redirect('/login')

def myorders(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login to place the Order....")
        return redirect("/login")
    mymed=Medicines.objects.all()
    myprod=ProductItem.objects.all()

    #logic to get user details
    current_user=request.user.username
    print(current_user)
    items=MyOrders.objects.filter(email=current_user)
    print(items)

    context={"myprod":myprod,"mymed":mymed,"items":items}

    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        item=request.POST.get("items")
        quan=request.POST.get("quantity")
        address=request.POST.get("address")
        phone=request.POST.get("num")
        print(name,email,item,quan,address,phone)
        

        price=""
        for i in mymed:
            if item==i.title:
                price=i.price

            pass
        for i in myprod:
            if item==i.prod_name:
                price=i.prod_price

            pass

        newPrice=int(price)*int(quan)
        myquery=MyOrders(name=name,email=email,items=item,address=address,quantity=quan,price=newPrice,phone_num=phone)
        myquery.save()
        messages.info(request,f"Order is Successfull")
        return redirect("/orders")

    
    return render(request,"orders.html",context)





def deleteOrder(request,id):
    print(id)
    query=MyOrders.objects.get(id=id)
    query.delete()
    messages.success(request,"Order Cancelled Successfully..")
    return redirect("/orders")