from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

class Review(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('SF', 'SF'),
        ('Romance', 'Romance'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
    ] # 첫번째 인자는 DB에 저장되는 값, 두번째 인자는 사용자에게 보여지는 값

    title = models.CharField(max_length=200) # 영화 제목
    director = models.CharField(max_length=200) # 감독
    actor = models.CharField(max_length=200) 
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating = models.DecimalField(
        max_digits=2,           # 전체 자릿수 (예: 4.5 → 총 2자리)
        decimal_places=1,       # 소수점 아래 1자리
        validators=[
            MinValueValidator(Decimal('0.0')),
            MaxValueValidator(Decimal('5.0'))
        ]
    )
    release_year = models.IntegerField()
    running_time = models.IntegerField()           # 러닝타임 (분)
    content = models.TextField()                   # 리뷰 내용
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)
