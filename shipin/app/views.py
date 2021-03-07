from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
import time,random,os
from app.models import *
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
def error(request):
       return  HttpResponse(str("别瞎研究，你看不懂"))
def index(request):
        quanbu=len(os.listdir("/static/media"))
        dy=random.randint(2,quanbu)
        dy=str(dy)
        try:
          a=request.GET['syg']
          syg=str(int(a)-1)
          if int(a) in range(2,quanbu+1):
                return render(request,'index.html',{'dy':syg,'quanbu':quanbu})
          else:
                return render(request,'index.html',{'dy':1,'quanbu':quanbu})
        except Exception as f :
          try:
              a=request.GET['xyg']
              xyg=str(int(a)+1)
              if int(xyg) in range(1,quanbu+1):
                   return render(request,'index.html',{'dy':xyg,'quanbu':quanbu})
              else:
                   return render(request,'index.html',{'dy':quanbu,'quanbu':quanbu})
          except Exception as f:
              return render(request,'index.html',{'dy':dy,'quanbu':quanbu})

# Create your views here.:
