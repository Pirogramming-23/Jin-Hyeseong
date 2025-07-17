from django.shortcuts import render, redirect, get_object_or_404
from .models import DevTool
from .forms import DevToolForm
from apps.ideas.models import Idea
from django.core.paginator import Paginator

# Create your views here.

def devtool_list(request):
    queryset = DevTool.objects.all()
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    devtools = paginator.get_page(page_number)

    context = {
        'devtools': devtools,
        'page_range': paginator.page_range
    }
    return render(request, 'tool_list.html', context)

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, id=pk)
    ideas = Idea.objects.filter(devtool=devtool)

    context = {
        'devtool':devtool,
        'ideas':ideas,
    }
    return render(request, "tool_detail.html", context)

def devtool_create(request):
    if request.method == "POST":
        form = DevToolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('devtools:devtool_list')
    else:
        form = DevToolForm()
    return render(request, 'tool_create.html', {'form': form})

def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, id=pk)
    if request.method =="POST":
        form = DevToolForm(request.POST, request.FILES, instance=devtool)
        if form.is_valid():
            form.save()
        return redirect('devtools:devtool_detail', pk=pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'tool_update.html', {'form': form})

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, id=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtools:devtool_list')