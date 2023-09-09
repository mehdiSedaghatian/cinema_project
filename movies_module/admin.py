from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from . import models


# Register your models here.
class MovieAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Country)
admin.site.register(models.Director)
admin.site.register(models.MovieGallery)
admin.site.register(models.MovieComments)
admin.site.register(models.Like)
admin.site.register(models.Dislike)
admin.site.register(models.MovieReview)
