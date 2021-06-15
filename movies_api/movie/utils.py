import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response

def get_movies(page):
    try:
        url = 'https://demo.credy.in/api/v1/maya/movies/'
        if page :
            url = url + '?page='+ str(page)
        get_result = False
        count = 0
        while not get_result :

            count += count
            response = requests.get(url, auth=HTTPBasicAuth(settings.MOVIE_LIST_API_CLIENT_ID,
                                                                settings.MOVIE_LIST_API_CLIENT_SECRET))
            if response.status_code == 200:
                get_result=True
                return response.json()
            if count == 5:
                return Response({
                    'error': 'Please check your internet connection',
                    'success': False
                })

    except :
        return Response({
            'error': 'Please check your internet connection',
            'success': False
        })



