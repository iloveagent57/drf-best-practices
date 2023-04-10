# drf-best-practices
Demonstrates best practices for using DRF

# Requests
# Making requests
- This is less about DRF, but if using the python `requests` library, add
the payload to your POST, PATCH, or PUT requests with `json={'your': 'data'}`
https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests
>If you need that header set and you don’t want to encode the dict yourself,
>you can also pass it directly using the json parameter (added in version 2.4.2) and it will be encoded automatically:
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
Note, the json parameter is ignored if either data or files is passed.

## Parsing incoming requests:
https://www.django-rest-framework.org/api-guide/requests/#request-parsing
- When getting data from the request body, always use `request.data`.
- When getting query parameters, always use `request.query_params`.

# Authentication

# Routers

# ViewSets

# Serializers

# Responses, exceptions, status codes

# Schema
- use drf-spectacular

# Thottling

# Pagination

# Authorization and edx-rbac
- In particular, list-level perms
