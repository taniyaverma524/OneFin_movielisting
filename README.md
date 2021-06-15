API Documentation

This Endpoint takes username and password and registers and gives the access token
POST /user/register/
 application/json - {
    "username": "username:,
    "password": "password",
}
response
{
   "access_token": "access token"
}   
POST /user/login/
 application/json - {
    "username": "username:,
    "password": "password",
}
response
{
   "access_token": "access token"
}
    
For all the requests we would use this access token for authentication and permission in headers request
   Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIzNzMxNTc3LCJqdGkiOiI4OGJjNzYwZDM4Yzg0MmZhOTJmNTU4MmVhNzliMmM4NiIsInVzZXJfaWQiOjF9.zCdm7lBuR6y72yMD23E9WZfGeTzp559e4HFGuL6CEsE
    
This Endpoint gives the list of movies from third party API with pagination support
GET movie/movies/
response
 application/json - {
 “count”: <total number of movies>,
 “next”: <link for next page, if present>,
 “previous”: <link for previous page>,
 “data”: [
 {
 “title”: <title of the movie>,
 “description”: <a description of the movie>,
 “genres”: <a comma separated list of genres, if
present>,
 “uuid”: <a unique uuid for the movie>
 },
 ...
 ]
}
This Endpoint takes movie collection and stores them and also returns top 3 genres
POST movie/collection/
 application/json - {
 “title”: “<Title of the collection>”,
 “description”: “<Description of the collection>”,
 “movies”: [
 {
 “title”: <title of the movie>,
 “description”: <description of the movie>,
 “genres”: <generes>,
 “uuid”: <uuid>
 }, ...
 ]
}
response
{
 “collection_uuid”: <uuid of the collection item>
}   
PATCH movie/collection/<collection_uuid>/
 application/json - {
 “title”: <Optional updated title>,
 “description”: <Optional updated description>,
 “movies”: <Optional movie list to be updated>,
}
response
{
 “title”: <Title of the collection>,
 “description”: <Description of the collection>,
 “movies”: <Details of movies in my collection>
5
}
    
DELETE movie/collection/<collection_uuid>/
response
{"message": "Collection deleted successfully!"}
    
GET movie/collection
response
 application/json - {
 “is_success”: True,
 “data”: {
 “collections”: [
 {
 “title”: “<Title of my collection>”,
 “uuid”: “<uuid of the collection name>”
 “description”: “My description of the collection.”
 },
 ...
 ],
 “favourite_genres”: “<My top 3 favorite genres based on the
movies I have added in my collections>.”
 }
}
This Endpoint return the number of requests which have been served by the server and resets it
GET /request-count/
 application/json - {
 “requests”: <number of requests served by this server till now>.
}
response
{
   "access_token": "access token"
}   
POST /request-count/reset/
response
{
 “message”: “request count reset successfully”
}