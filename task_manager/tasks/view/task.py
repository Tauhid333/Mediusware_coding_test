from tasks.forms import *
from django.http import HttpResponseRedirect
from tasks.views import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def task_list(request): 
    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['created_by_id'] = request.user.id
        created_by = request.user
        print('a',created_by)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.created_by = request.user
            task.save()
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else :
            for field in form:
                for error in field.errors:
                    print("%s : %s" % (field.name.capitalize(), error))
    template_name   = "tasks/task.html"
    object_list     = TaskDetails.objects.order_by('id')
    action_url      = reverse_lazy('task_list')
    action_name     = "Add TaskDetails"
    form            = TaskForm()
    context         = { 'action_name':action_name, 'form':form, 'action_url':action_url, 'object_list':object_list }
    return render(request, template_name, context)


@login_required
def task_update(request, id):
    try:
        instance = get_object_or_404(TaskDetails, id=id)
        if request.method == "POST":
            form = TaskForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        template_name   = "tasks/task.html"
        action_name     = "Update TaskDetails"
        action_url      = reverse_lazy('task_update', kwargs={'id':id})
        object_list     = TaskDetails.objects.order_by('id')
        form            = TaskForm(instance=instance)

        context = { 'action_name':action_name, 'form':form, 'action_url':action_url, 'object_list':object_list, 'instance':instance }
        return render(request, template_name, context)
    except : return redirect(reverse_lazy('task_list'))

@login_required
def task_delete(request, id):
    instance = get_object_or_404(TaskDetails, id=id)
    instance.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))