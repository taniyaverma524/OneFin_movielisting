from django.db import models
from user.models import User
import uuid

class MovieCollection(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_collection')
    uuid =models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False,unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    modifield_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MovieList(models.Model):
    collection = models.ForeignKey(MovieCollection,related_name='movies',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250,blank=True)
    genres = models.CharField(max_length=150,blank=True)
    uuid = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# from movie.serializer import MovieCollectionSerializer
# from movie.models import MovieList,MovieCollection
# from user.models import User
# user=User.objects.get(username='taniya')
#
# ob=MovieCollection.objects.create(title="Movielist1",description="i have many adds",user=user)
# MovieList.objects.create(title="Queerama",description="50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",uuid= "57baf4f4-c9ef-4197-9e4f-acf04eae5b4d",collection=ob)
