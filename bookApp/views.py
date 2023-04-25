from django.shortcuts import render,redirect
from .models import Book,Writer,Users
from .form import UserForm,WriterForm,BookForm


# Create your views here.

def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if Users.objects.filter(user_name=name,password=password).exists():
            # request.session['user']= name
            response = render(request, 'bookApp/index.html') 
            response.set_cookie('user',name)
            return response
        
        else:
            context ={
                'error':'User_name or Password is wrong Pls try again'
            }

            return render(request,'login.html',context)   


           
   
    return render(request,'login.html')


def logout(request):
    try:
    #    del request.session['user']
         response =redirect('home')
         response.delete_cookie('user')
    except:
        
        response =redirect('home')
        

    return response



def user(request):
    
    try:

        user_name=request.COOKIE['user']
    except:
        return render(request, "login.html",{'login_error':'Login First'})

    context={'users':Users.objects.all()}
    context['form']= UserForm()
   
    if request.method == "POST":
        form=UserForm(request.POST)
        name=form['user_name'].value()
        password=form['password'].value()
        
        
        if Users.objects.filter(user_name=name).exists():
            context['error']='This User is Already exited'
        else:
            Users.objects.create(user_name=name,password=password)
    
    return render(request, 'user/user.html',context)

def userdelete(request,id):
   
    
   user = Users.objects.get(id=id)
   user.delete()

   return redirect('user')


def book(request):

    try:
        user_name=request.session['user']
    except:
        
        return render(request, "login.html",{'login_error':'Login First'})

    mydata = Book.objects.all()
    print(mydata)
    context = {

        'bookList':mydata,
    }
            
    return render(request,'bookApp/book.html',context)


def bookDelete(request,id):

    data = Book.objects.get(id = id)
    data.delete()
    

    return redirect('bookList')


def addForBook(request):
    context={'writers':Writer.objects.all(),'form':BookForm()}
    if request.method == 'POST':
    
        form = BookForm(request.POST)
        # book_name = request.POST['name']
        
        # if Book.objects.filter(name=book_name).exists():
        #     context['error'] ='This book name is taken'

        if form.is_valid:

            form.save()
            return redirect('bookList')
        else :
            
            context['error'] ='This book name is taken'
        
            return render(request, 'bookApp/addBook.html',context)

        # book = Book(name=book_name,writer=Writer.objects.get(id=writer_id))    
        # book.save()
        # return redirect('bookList')  

    return render(request, 'bookApp/addBook.html',context)


def updatebook(request,id):
        
        book = Book.objects.get(id = id)
        context={'writers':Writer.objects.all(),'form':BookForm(instance=book)}
        if request.method == 'POST':
            
                form = BookForm(request.POST,instance=book)

                if form.is_valid:
                    form.save()
                
                return redirect('bookList')
                    
        return render(request, 'bookApp/updatBook.html',context)  


def writer(request):
    
    writers=Writer.objects.all()
    context = {'writers':writers}
    return render(request, "writer/writerList.html",context)


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

def deletewriter(request,id):

    writer=Writer.objects.get(id=id)
    writer.delete()
    return redirect('writerList')  


