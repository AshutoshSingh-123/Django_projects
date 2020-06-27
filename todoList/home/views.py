from django.shortcuts import render, HttpResponse
from home.models import task

# Create your views here.
def home(request):
 context={'success':False}
 if request.method=='POST':
  title=request.POST['title']
  desc=request.POST['desc']
  ins=task(title=title, desc=desc)
  ins.save()
  context={'success':True}

 
 return render(request,'index.html',context)
 # models
 

def about(request):
 allTasks=task.objects.all()
 context={'tasks':allTasks,'suc':False}
 # for search bar
 if request.method=='POST':
  
  search=request.POST['search']
 
  s=task.objects.filter(title = search)
  if len(s)>0:
   l=len(s)
   context={'tasks':allTasks,'suc':True,'length':l}

 
 
 return render(request,'about.html',context)

      