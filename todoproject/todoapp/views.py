from django.shortcuts import render,HttpResponse,redirect
from.models import Task
from.forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
# class Tasklistview(ListView):
#     model = Task
#     template_name = 'home.html'
#     context_object_name = 'product'
#
# class Taskdetailview(DetailView):
#     model = Task
#     template_name = 'detail.html'
#     context_object_name = 'i'
#
# class Taskupdateview(UpdateView):
#     model = Task
#     template_name = 'edit.html'
#     context_object_name = 'form'
#     fields = ('name','priority','date')
#     def get_success_url(self):
#         return reverse_lazy('csvdetail',kwargs={'pk':self.object.id})
# class Taskdeleteview(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('csvtask')

def demo(request):
    product1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date= request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
        return render(request, "home.html", {'product': product1})
    return render(request, 'home.html')

def delete(request,id):
    task1 = Task.objects.get(id=id)
    if request.method == "POST":
        task1.delete()
        return redirect('/')
    return render(request,'delete.html',{'task1':task1})
# def details(request):

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})