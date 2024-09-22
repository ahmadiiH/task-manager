from django.shortcuts import render , redirect , get_object_or_404
from .forms import TaskForm , EditForm
from .models import Task
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

 

@login_required 
def home(request):
    tasks = Task.objects.filter(user=request.user)
    form=EditForm()
    if term := request.GET.get("search") : 
        tasks = tasks.filter(title__icontains = term)
    if completed := request.GET.get("completed") : 
       tasks = tasks.filter(completed = bool(int(completed)))
    if date := request.GET.get("date"):
        filter_date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
        start_of_day = timezone.make_aware(timezone.datetime.combine(filter_date, timezone.datetime.min.time()))
        end_of_day = timezone.make_aware(timezone.datetime.combine(filter_date, timezone.datetime.max.time()))
            
        tasks = tasks.filter(due_date__range =(start_of_day, end_of_day ))

    
    
    p = Paginator(tasks, 10)
    page_number = request.GET.get("page")
    page = p.get_page(page_number)
    return render (request, "tasks/main.html" , context={"page" : page , "num" : p.num_pages , "form":form})
@login_required 
def new_Task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            Task.objects.create(
                user=request.user,
                title=validated_data["title"],
                due_date=validated_data["due_date"]
            )
            return redirect("home_page")
    else:
        form = TaskForm()

    return render(request, "tasks/new-task.html", context={"form": form})

@login_required 
def switch_completed(request , id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save() 
    return redirect("home_page")


@login_required 
def delete_task(request , id):
    task = Task.objects.get(id=id)
    if task.user == request.user :
        task.delete()
        return redirect("home_page")


@login_required 
def edit_task(request , id):
     task = get_object_or_404(Task, id=id)
     if task.user == request.user :
        if request.method == 'POST' :
            form = EditForm(request.POST,instance=task)
            if form.is_valid():
                newtask = form.save(commit=False)
                newtask.user = request.user
                newtask.save()
                return redirect("home_page")
        else:
            form = EditForm(instance=task)
            
        
        return render(request , "tasks/edit.html", context={"form" : form })

    


    



