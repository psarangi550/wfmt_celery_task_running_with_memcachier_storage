from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .tasks import add
# Create your views here.

@cache_page(60)
def index(request):
    add.delay(10,20)
    print(cache.get("result"))
    return render(request,"memcachedcloudceleryApp/index.html",)