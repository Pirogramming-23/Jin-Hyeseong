from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Review

# Create your views here.

def convert_minutes_to_hour_min(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}시간 {mins}분"


def reviews_list (request) :
    sort = request.GET.get('sort', '')  # 기본은 정렬 없음

    if sort == 'title':
        reviews = Review.objects.order_by('title')
    elif sort == 'rating':
        reviews = Review.objects.order_by('-rating')
    elif sort == 'running_time':
        reviews = Review.objects.order_by('-running_time')
    elif sort == 'created_at':
        reviews = Review.objects.order_by('-created_at')
    else:
        reviews = Review.objects.all()

    for review in reviews:
        review.running_time_display = convert_minutes_to_hour_min(review.running_time)
    content = {
        'reviews': reviews,
    }
    return render(request, "reviews_list.html", content)

def reviews_detail(request, pk):
    review = get_object_or_404(Review, pk=pk) 
    review.running_time_display = convert_minutes_to_hour_min(review.running_time)
    return render(request, 'reviews_detail.html', {'review': review})

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/review/")

def reviews_edit(request, pk):
    review = Review.objects.get(id=pk)

    if request.method == "POST":
        review.title = request.POST['title']
        review.director = request.POST['director']
        review.actor = request.POST['actor']
        review.genre = request.POST['genre']
        review.rating = request.POST['rating']
        review.release_year = request.POST['release_year']
        review.running_time = request.POST['running_time']
        review.content = request.POST['content']
        review.image_url = request.POST['image_url']
        review.save()
        return redirect(f"/review/{pk}")
    
    context = {
        "review": review
    }
    return render(request, "reviews_update.html",context)

def reviews_create(request):
    if request.method == "POST":
        new_review= Review.objects.create(
            title = request.POST['title'],
            director = request.POST['director'],
            actor = request.POST['actor'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            release_year = request.POST['release_year'],
            running_time = request.POST['running_time'],
            content = request.POST['content'],
            image_url = request.POST['image_url'],
        )
        return redirect('reviews_list')
    return render(request, "reviews_update.html")