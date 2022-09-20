from django.shortcuts import render
from django.http import HttpResponse
from django.views import  View
from django.views.decorators.csrf import csrf_exempt


class IndexClass(View):
    def get(self, request):
        return HttpResponse("Hello world")
    def post(self, request):
        if request.FILES.has_key('data'):
            file = request.Files['data']
            data = file.read()
        return HttpResponse(data)

@csrf_exempt
def save_events_json(request):
    s = ' nothing'
    if request.is_ajax():
        s = 'this is ajax'
        if request.method == 'POST':
            return HttpResponse('Raw Data: "%s"' % request.body)
    return HttpResponse('null' + s)