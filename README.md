Geolocation finder is a location finder application in django.

we have two django apps here named frontend and backend.

*backend app
-the backend app is implemented using django rest framework 3.10.2.
-the backend api has two major end points
 END POINT 1: "http://localhost:3000/"
	This end point returns ip, type, continent_code, continent_name, country_code, country_name, region_code, region_name, city, zip, latitude, longitude, 
    	capital, language of all the data in the data base in a json format.

END POINT 2: "http://localhost:3000/IP_ADDREESS"
	-This end point returns This end point returns ip, type, continent_code, continent_name, country_code, country_name, region_code, region_name, city, zip, latitude, longitude, 
    	capital, language of a particlar ip address.
	-if the data can't be found in the database, a request is made to 'https://api.ipstack.com/134.201.250.155? access_key = YOUR_ACCESS_KEY' to get the data from ipstack and save in a memcache
	-when next another user searches for that same ip address, a query is carried out on the database,  but if the ip  address is not found on the database them the memcache is being queried. if the query exist in the memcache, then the json data is returned.

*frontend app
-the frontend app consumes the backend api end points.
	"http://localhost:8000/" display all the data in the database
	"http://localhost:8000/134.201.250.155" displays the data of the ip address '134.201.250.155' in the database

please ensure you run the front end and backend on different server.

how to run the app.
step 1. open this project in two windows
step 2. run the backend using the following commands
	-cd geolocation 
	-python manage.py runserver # by default this will be launched on  http://127.0.0.1:8000/
step 3. open the second instance(frontend) of this project and run the following commands
	-cd geolocation 
	-python manage.py runserver 8080 # this will be launched on  http://127.0.0.1:8080/
	-the consume the api using the backend server address 'http://127.0.0.1:8000/'

read the requirements.txt for the neccesary installations needed.


