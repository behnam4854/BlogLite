from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_safe
from django.views import View

import datetime
@require_safe
def homeview(request):
    """the first version of home view using simple functions"""
    # return HttpResponse("<h1>Page was found</h1>")
    return render(request,'base.html')
async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
class HomeClassBasedView(View):
    """this is for home view using generic class based view"""
    def get(self, request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)