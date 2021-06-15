from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from movie.utils import get_movies
from rest_framework.response import Response
from movie.serializer import MovieCollectionSerializer, CollectionSerializer
from movie.models import MovieCollection,MovieList
from django.db.models import Count
from django.http import Http404


class GetMoviesView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        page = request.query_params.get('page')
        response = get_movies(page)
        return Response(response)


class MovieCollectionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return MovieCollection.objects.get(uuid=pk)
        except:
            return Http404

    def post(self , request ):

        serializer = MovieCollectionSerializer(data = request.data, context={'user': request.user})
        if serializer.is_valid():
            obj= serializer.save()
            return Response({
                'collection_uuid': obj.uuid
            })
        return Response({
            'error': serializer.errors
        })

    def patch(self,request,pk):
        collection = self.get_object(pk)
        serializer = MovieCollectionSerializer(collection,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data
            })
        return Response({
            'error': serializer.errors
        })

    def get(self,request):
        queryset = MovieCollection.objects.filter(user=request.user)
        serializer = CollectionSerializer(queryset,many=True)
        fav_list = MovieList.objects.values('genres').annotate(c=Count('genres')).order_by('-c')[:3]
        return Response({
            'data':serializer.data,
            'favourite_genres': fav_list
        })


    def delete(self,request,pk):
        collection =  self.get_object(pk)
        collection.delete()
        return Response({
            'message': 'movie collection deleted successfully.'
        })


