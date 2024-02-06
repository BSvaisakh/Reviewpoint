from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Anime)
admin.site.register(MovieReview)
admin.site.register(SeriesReview)
admin.site.register(AnimeReview)