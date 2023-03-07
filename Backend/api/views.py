from django.http import JsonResponse
import json
import pprint

def api_home(request):
    # Django convert request into Http request 
    body = request.body # Httprequest attribute  https://docs.djangoproject.com/en/4.1/ref/request-response/
    data = {}
    try:
        data = json.loads(body) # byte string of JSON data to python dict
    except:
        pass
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = request.GET
    print(request.GET) # url query params
    # pprint.pprint(request.META) # META attribute of Httprequest class
    return JsonResponse(data)