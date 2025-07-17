from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Idea
from .forms import IdeaForm
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.

def idea_list(request):
    sort = request.GET.get('sort', 'latest')

    sort_mapping = {
        'latest' : '-created_at',
        'interest' : '-interest',
        'title' : 'title',
    }

    ordering = sort_mapping.get(sort, '-created_at')
    queryset = Idea.objects.all().order_by(ordering)

    # Paginator: 한 페이지당 4개씩
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    ideas = paginator.get_page(page_number)

    context = {
        'ideas' : ideas,
        'sort' : sort,
        'page_range' : paginator.page_range
    }

    return render(request, "idea_list.html", context)

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_list')
    else:
        form = IdeaForm()
    return render(request, 'idea_create.html', {'form': form})


def toggle_star(request):
    idea_id = request.GET.get('id')
    idea = Idea.objects.get(id=idea_id)
    idea.is_star = not idea.is_star
    idea.save()
    return JsonResponse({'is_star': idea.is_star})

def adjust_interest(request):
    idea_id = request.GET.get('id')
    direction = request.GET.get('direction')

    idea = Idea.objects.get(id=idea_id)
    if direction == 'up':
        idea.interest += 1
    elif direction == 'down':
        idea.interest = max(0, idea.interest - 1)

    idea.save()
    return JsonResponse({'interest': idea.interest})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, id=pk)

    context = {
        'idea': idea,
    }
    return render(request, 'idea_detail.html', context)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_detail', pk=pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'idea_update.html', {'form': form})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('ideas:idea_list')

