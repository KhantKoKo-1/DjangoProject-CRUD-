from django.shortcuts import render,redirect
from .models import Book,Writer,Users,FavBookCollection
from .form import UserForm,WriterForm,BookForm,FavBookForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# def loginPage(request):
    
#     if request.method == 'POST':
#         name = request.POST['name']
#         password = request.POST['password']

#         user = authenticate(request,user_name=name,password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('user')
        
       

#         if Users.objects.filter(user_name=name,password=password).exists():
#             request.session['user']= name
#             response = render(request, 'bookApp/index.html') 
#             response.set_cookie('user',name)
#             return response
        
#         else:
#             context ={
#                 'error':'User_name or Password is wrong Pls try again'
#             }

#             return render(request,'login.html',context)   


           
   
#     return render(request,'login.html')

def loginPage(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(request,username=name,password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('user')
    return render(request, "login.html")

def logoutPage(request):
    logout(request)

    # try:
    #      del request.session['user']
    #      response =redirect('loginPage')
    #      response.delete_cookie('user')
    # except:
        
    #     response =redirect('loginPage')
        

    return redirect('loginPage')


# @login_required(login_url='loginPage')
def user(request):
    
    # try:

    #     user_name=request.COOKIE['user']
    # except:
    #     return render(request, "login.html",{'login_error':'Login First'})

    context={'usersForm':User.objects.all()}
    
    context['form']= UserCreationForm()
   
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        print(form)
        
        if form.is_valid():
           form.save()
           messages.success(request, 'Account created successfully') 
           

        else:
           messages.warning(request,'Error loggin in....')
           return render(request, 'user/user.html',{'usersForm':User.objects.all(),'form':form})  
            
            
        # name=form['user_name'].value()
        # password=form['password'].value()
        
        
        # if Users.objects.filter(user_name=name).exists():
        #     context['error']='This User is Already exited'
        # else:
        #     Users.objects.create(user_name=name,password=password)
    
    return render(request, 'user/user.html',context)

@login_required(login_url='loginPage')
def userdelete(request,id):
   
    
   user = User.objects.get(id=id)
   user.delete()

   return redirect('user')

# Python program to view
# for displaying images


@login_required(login_url='loginPage')
def book(request):

    # try:
    #     user_name=request.session['user']
    # except:
        
    #     return render(request, "login.html",{'login_error':'Login First'})
    
    mydata = Book.objects.all()
    
    context = {

        'bookList':mydata,
    }
            
    return render(request,'bookApp/book.html',context)

@login_required(login_url='loginPage')
def bookDelete(request,id):

    data = Book.objects.get(id = id)
    data.delete()

    return redirect('bookList')

@login_required(login_url='loginPage')
def addForBook(request):
    context={'writers':Writer.objects.all(),'form':BookForm()}
    if request.method =='POST':
    
        form = BookForm(request.POST, request.FILES)
        
        # book_name = request.POST['name']
        # writer_id =request.POST['writer']
        # upload = request.FILES['image']
        
        # if Book.objects.filter(name=book_name).exists():
        #     context['error'] ='This book name is taken'

        # else:    
        #     date =datetime.datetime.now()
            
            # fss = FileSystemStorage()
            # file = fss.save(upload)
            # file_url = fss.url(file


            # book = Book(name=book_name,writer=Writer.objects.get(id=writer_id),date=date) 
            

            # book.save()
            # return redirect('bookList') 
        
        if form.is_valid():
            
            form.save()
              
            # img_object= form.instance  

            # context['bookList']=img_object
            
            return redirect('bookList')
        else :
            
            context['error'] ='This book name is taken'
        
            return render(request, 'bookApp/addBook.html',context)
         

    return render(request, 'bookApp/addBook.html',context)

@login_required(login_url='loginPage')
def updatebook(request,id):
        
        book = Book.objects.get(id = id)
        context={'writers':Writer.objects.all(),'form':BookForm(instance=book)}
        if request.method == 'POST':
            
                form = BookForm(request.POST,instance=book)

                if form.is_valid():
                    form.save()
                
                return redirect('bookList')
                    
        return render(request, 'bookApp/updatBook.html',context)  

@login_required(login_url='loginPage')
def writer(request):
    
    writers=Writer.objects.all()
    context = {'writers':writers}
    return render(request, "writer/writerList.html",context)

@login_required(login_url='loginPage')
def addwriter(request):
    context = {
        'form':WriterForm()
    }
    # writer = Writer.objects.get(id = id)
    if request.method == 'POST':
    
        
        form = WriterForm(request.POST)
          
        if form.is_valid():
           form.save() 
           return redirect('writerList')
        else:
            context['error']='name is taken'
        
                # # if Writer.objects.filter(name=book_name).exists():
        # #     context ={
        # #         'error':'This writer name is taken'
        # #     }
        
        # #     return render(request, 'writer/writerList.html',context)

        # Writer.objects.create(firstName=first_name,lastName=last_name)
        # return redirect('writerList')  

    return render(request, 'writer/add_writer.html',context)

@login_required(login_url='loginPage')
def deletewriter(request,id):

    writer=Writer.objects.get(id=id)
    writer.delete()
    return redirect('writerList')  


@login_required(login_url='loginPage')
def favBook(request):

    context = {'favlist':FavBookCollection.objects.all()}

    context['form'] = FavBookForm()

    if request.method == 'POST':

        form = FavBookForm(request.POST) 


        if form.is_valid:
             
            form.save() 
            

    return render(request,'bookApp/favBook.html',context)

@login_required(login_url='loginPage')
def fav_book_delete(request,id):
    print('deletecd')
    fav_=FavBookCollection.objects.get(id=id)
    fav_.delete()
    
    return  redirect ('favBook')

