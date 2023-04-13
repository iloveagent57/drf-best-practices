# drf-best-practices
Demonstrates best practices for using DRF

# Takeaways circa April 13, 2023
- drf-spectacular has a lot of potential value for us and a fairly low cost to use.  We should formally adopt it as a best practice via an OEP.
- edx-rbac's `PermissionRequiredForListingMixin` is not meeting our needs - it's too complex and non-obvious.  We should create a decorator that can meet this need at the view function level.
- Viewsets and routing are sometimes fighting against us - we'd often be better off writing class-based views and explicitly declaring our routes one-by-one.  This will make the routes easier to discover and understand from a developer's perspective, and also make it easier to implement nested routes so we can be more obviously-RESTful.
- drf-simplejwt is a nice library and we should consider adopting it in Open edX (drf-jwt is not exactly actively maintained - the arch team is starting to look into this).
- drf-nested-routers are sort of ok, but maybe not worth the cost of adopting and fighting against yet-another-drf-author's opinions.  We can make our routes more explicit (as mentioned above) to get the same effect.
- Other DRF packages (e.g. drf-extensions, dynamic-rest, etc.) have their hearts in the right place, but seem to get further and further away from explicitness, which makes our systems harder and harder to comprehend.

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
that add, modify, or delete records.  But then you have to route manually, which might be ok.

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


# Using with Postman
Add a pre-request script to a collection:
```
// Refresh the OAuth token if necessary
var tokenDate = new Date(2010,1,1);
var tokenTimestamp = pm.environment.get("OAuth_Timestamp");
if(tokenTimestamp){
  tokenDate = Date.parse(tokenTimestamp);
}
var expiresInTime = pm.environment.get("ExpiresInTime");
if(!expiresInTime){
    expiresInTime = 300000; // Set default expiration time to 5 minutes
}
if((new Date() - tokenDate) >= expiresInTime) 
{
   pm.sendRequest({
      url:  pm.variables.get("Auth_Url"), 
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: {
          mode: 'raw',
          raw: JSON.stringify({
              'username': pm.variables.get("Auth_Username"),
              'password': pm.variables.get("Auth_Password"),
          }),
      },
  }, function (err, res) {
      console.log(err);
      console.log(res.json());
        pm.environment.set("OAuth_Token", res.json().access);
        pm.environment.set("OAuth_Timestamp", new Date());
        
        // Set the ExpiresInTime variable to the time given in the response if it exists
        if(res.json().expires_in){
            expiresInTime = res.json().expires_in * 1000;
        }
        pm.environment.set("ExpiresInTime", expiresInTime);
  });
}
```
Add (static) collection variables for
- Auth_Url: http://localhost:8000/api/token/
- Auth_Username: admin
- Auth_Password: [your-admin-password]

Add (dynamic) environment variables as below, they don't need values, the script
will populate them:
- OAuth_Timestamp
- ExpiresInTime
- OAuth_Token

Thanks to https://callenheltondev.medium.com/how-to-automate-oauth2-token-renewal-in-postman-864420d381a0
for this recipe.
