from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Dj_Api
from .serializers import Dj_ApiSerializer
import mysql.connector
from django.http import JsonResponse


class Dj_ApiViewSet(viewsets.ModelViewSet):
    queryset = Dj_Api.objects.all().order_by('-posttime')
    serializer_class = Dj_ApiSerializer





#Create your views here
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="django_connect"

)
#create cursor object
cursor = db.cursor()


def verify_login(Username, password):
    sql = "select * from accountdata where Username = %(Username)s and password = %(password)s"  #%s传递参数
    cursor.execute(sql, {'Username': Username, 'password': password})
    results = cursor.fetchall()
    if len(results) == 0:
        return False
    else:
        return True


def login(request):
    if request.method == "GET":
        User = request.GET.get('Username', '')
        pwd = request.GET.get('password', '')
        if str(User) == '':
            return JsonResponse({'code': 1001, 'msg': 'id can\'t be empty'})
        if str(pwd) == '':
            return JsonResponse({'code': 1001, 'msg': 'password can\'t be empty'})
        else:
            if verify_login(Username=User, password=pwd):
                return JsonResponse({'code': 1002, 'msg': 'OK'})
            else:
                return JsonResponse({'code': 1002, 'msg': 'No'})
    else:
        return JsonResponse({'code': 1003, 'msg': 'invalid request'})