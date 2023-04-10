# drf-best-practices
Demonstrates best practices for using DRF

# Tutorial getting started
Largely based off of https://www.django-rest-framework.org/tutorial/quickstart/
Do as follows:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```
Now visit http://localhost:8000/api/v1/, click the "login" button at the top right,
use "admin/[your password]" to authenticate, and see all of the users at
http://localhost:8000/api/v1/users/

# Requests
## Making requests
- This is less about DRF, but if using the python `requests` library, add
the payload to your POST, PATCH, or PUT requests with `json={'your': 'data'}`

https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests

>If you need that header set and you don’t want to encode the dict yourself, 
you can also pass it directly using the json parameter (added in version 2.4.2) and it will be encoded automatically:
```
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
```
>Note, the json parameter is ignored if either data or files is passed.

## Parsing incoming requests:
https://www.django-rest-framework.org/api-guide/requests/#request-parsing
- When getting data from the request body, always use `request.data`.
- When getting query parameters, always use `request.query_params`.

# Authentication
https://www.django-rest-framework.org/api-guide/authentication/#how-authentication-is-determined
>The authentication schemes are always defined as a list of classes. 
REST framework will attempt to authenticate with each class in the list, 
and will set `request.user` and `request.auth` using the return value of the first class that successfully authenticates.
If no class authenticates, `request.user` will be set to an instance of 
`django.contrib.auth.models.AnonymousUser`, and `request.auth` will be set to None.

So you can think of authentication as a logical OR - if _any_ authentication class
succeeds, the request will be authenticated.

- edX tends to do a lot of authentication class declaration on our ViewSets, e.g.
`authentication_classes = [SessionAuthentication, BasicAuthentication]`.  But you can also set defaults
at the settings level:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```
- edX really likes JwtAuthentication, consider making that a default for your project.

# Routers

# ViewSets
- Many, smaller viewsets are preferrable to single, giant viewsets.
- It is ok to have viewsets that only support a single endpoint or action - this
can help you control things like permissions or serialization in a more granular way.
- Many, smaller files are preferrable to a giants `views.py` file.  There is nothing
magic about the name `views.py`.
- It's preferrable to decompose your views into read-only viewsets and viewsets
that add, modify, or delete records.

# Serializers
- Have different viewsets for reads and writes.
- DRF wants to serialize _objects_, not really _dicts_.
- You can serialize objects that are not models.
- Please for the love of all that is good and true, make your serializers
and their methods "small enough" - too much logic in the serializers is a code smell.
You can break down your giant serializer into smaller, more digestable serializers,
just as you can for Viewsets.

# Responses, exceptions, status codes

# Schema
- use drf-spectacular

# Thottling

# Pagination

# Authorization and edx-rbac
- In particular, list-level perms
