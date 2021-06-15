from django.contrib import admin

from movie.models import MovieList,MovieCollection

class MovieListAdmin(admin.TabularInline):
    model = MovieList
    extra=0
    fields = ['title','description','genres','uuid']

class MovieCollectionAdmin(admin.ModelAdmin):
    model = MovieCollection
    readonly_fields = ['uuid']
    fields = ['user','uuid','title','description',]
    inlines = [MovieListAdmin]

admin.site.register(MovieCollection,MovieCollectionAdmin)