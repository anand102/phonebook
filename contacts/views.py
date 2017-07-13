
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from .models import Person,Contact


def index(request):
    if 'username' in request.session:
        u=request.session['username']
        try:
            user_obj=Person.objects.get(username=u)
        except Person.DoesNotExist:
            user_obj=None 
        if user_obj:
            all_contact=Contact.objects.filter(person=user_obj)
            return render(request,'contacts/allcontact.html',{'allcontact':all_contact})   
    return redirect('/contacts/login/')        
def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        try:
            user = Person.objects.get(username=username, password=password)
        except Person.DoesNotExist:
            return redirect('/contacts/login/?error=user does not exist')     

        request.session['username']=username
        return redirect('/contacts/')
                  
    return render(request,'contacts/login.html')
        
def Signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password= request.POST.get('password')
        confirmpassword= request.POST.get('confirmpassword')
        if not username or not password or not confirmpassword:
            return redirect('/contacts/signup/?error= Plz fill all fields')
        if Person.objects.filter(username=username).exists():
            return redirect('/contacts/signup/?error= already exist')
        if not password==confirmpassword:
            return redirect('/contacts/signup/?error= password mismatch')    
        user = Person.objects.create(username=username, password=password)    
        request.session['username']=username
        return redirect('/contacts/')
               
    return render(request,'contacts/signup.html')

def Logout(request):
    request.session.pop('username', None)
    return redirect('/contacts/login')

# def Home(request):
#     if 'username' in request.session:
#         return render(request,'contacts/home.html')
#     else:
#         return render(request,'contacts/admin.html')    
def Add_contact(request):
    if 'username' in request.session:
        if request.method=='POST':
            name=request.POST.get('name')
            number=request.POST.get('number')
            if not name or not number :
                return redirect('/contacts/addcontact/?error= Plz fill all fields')
            username=request.session['username']
            person= Person.objects.get(username=username)
            user=Contact.objects.create(name=name,number=number,person=person)
            return redirect('/contacts/?message=added contact successfuly')
        
        return render(request,'contacts/addcontact.html')
    else:
        return redirect('/contacts/login/')    

def Edit_contact(request,id):
    if 'username' in request.session:
        co=Contact.objects.get(id=id)

        if request.method=='POST':
            name=request.POST.get('name')
            number=request.POST.get('number')
            if not name or not number:
                return redirect('/edit/%s/?error= Plz fill name and number' %(id))
            co.name=name
            co.number=number
            co.save()
            return redirect('/contacts/?message=Edit successfuly')    
                    
        return render(request,'contacts/addcontact.html',{'co':co})         

    else:
        return redirect('/contacts/login/')            

def Delete_contact(request,id):
    if 'username' in request.session:
        co=Contact.objects.get(id=id)
        co.delete()
        return redirect('/contacts/?message=Contact deleted')
    return redirect('/contacts/login/')    