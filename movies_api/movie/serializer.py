from rest_framework import serializers
from movie.models import MovieList,MovieCollection




class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ['title','description','genres','uuid']


class MovieCollectionSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True)

    class Meta:
        model = MovieCollection
        fields = ['title','description','movies']


    def create(self, validated_data):
        movies = validated_data.pop('movies')
        user = self.context.get('user')
        collection = MovieCollection.objects.create(user=user, **validated_data)
        for movie in movies:
            MovieList.objects.create(collection=collection, **movie)
        return collection

    def update(self, instance, validated_data):
        movies = validated_data.pop('movies')
        collection = MovieCollection.objects.filter(uuid=instance.uuid).update(**validated_data)
        if movies:
            for movie in movies:
                MovieList.objects.update_or_create(collection=instance, **movie)
        return instance


class CollectionSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = MovieCollection
        fields = ['title','description','movies']
