from django.shortcuts import render,redirect
from .models import Book,Writer,Users


# Create your views here.

def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if Users.objects.filter(user_name=name,password=password).exists():
            return render(request, 'book/index.html') 

           
   
    return render(request,'login.html')


def user(request):
    context={'users':Users.objects.all()}
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        
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
    context={'writers':Writer.objects.all()}
    if request.method == 'POST':
    
        writer_id = request.POST['writer_id']
        book_name = request.POST['name']
        
        if Book.objects.filter(name=book_name).exists():
            context['error'] ='This book name is taken'
                
            
            
        
            return render(request, 'bookApp/addBook.html',context)

        book = Book(name=book_name,writer=Writer.objects.get(id=writer_id))    
        book.save()
        return redirect('bookList')  

    return render(request, 'bookApp/addBook.html',context)


def updatebook(request,id):
        
        book = Book.objects.get(id = id)
        context={'writers':Writer.objects.all(),'book':book}
        if request.method == 'POST':
            
                writer_id = request.POST['writer_id']
                name = request.POST['name']
            
                book.name = name
                book.writer = Writer.objects.get(id=writer_id)

                book.save()
                return redirect('bookList')
                    
        return render(request, 'bookApp/updatBook.html',context)  


def writer(request):
    
    writers=Writer.objects.all()
    context = {'writers':writers}
    return render(request, "writer/writerList.html",context)


def addwriter(request):
    
    # writer = Writer.objects.get(id = id)
    if request.method == 'POST':
    
        
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        print(first_name,last_name)
        
        # if Writer.objects.filter(name=book_name).exists():
        #     context ={
        #         'error':'This writer name is taken'
        #     }
        
        #     return render(request, 'writer/writerList.html',context)

        Writer.objects.create(firstName=first_name,lastName=last_name)
        return redirect('writerList')  

    return render(request, 'writer/add_writer.html')

def deletewriter(request,id):

    writer=Writer.objects.get(id=id)
    writer.delete()
    return redirect('writerList')  


