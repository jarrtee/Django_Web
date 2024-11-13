import base64
import json

import pymssql
import pymysql
from django.core import serializers
from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Dj_Api, User_Data, User_Photo
from .serializers import Dj_ApiSerializer
import mysql.connector
from django.http import JsonResponse, HttpResponse


class Dj_ApiViewSet(viewsets.ModelViewSet):
    queryset = Dj_Api.objects.all().order_by('-posttime')
    serializer_class = Dj_ApiSerializer


#获取基本信息
def User_Data_ViewSet(request):
    Alldata = []
    if request.method == "POST":
        UserNum = request.GET['UserNum']
        ALL_Data = User_Data.objects.filter(UserNum=UserNum)
        ALLData = serializers.serialize('json', ALL_Data)  #转化成JSON格式输出
        Alldata.append(ALLData)
    return HttpResponse(Alldata)


#获取头像
def User_Photo_ViewSet(request):
    blob_list = []
    if request.method == "POST":
        UserNum = request.GET['UserNum']
        query = "select Photo from user_basic_photo where UserNum=%s"
        cursor.execute(query, (UserNum,))
        blob_data = cursor.fetchone()[0]
        blob_list.append(blob_data)
    return HttpResponse(blob_list[0])


#修改基本信息
def update_data_view(request):
    if request.method == "POST":
        UserNum = request.GET['UserNum']
        UserName = request.GET['UserName']
        query = "update user_basic_inf set UserName=%s where UserNum=%s"
        cursor.execute(query, (UserName, UserNum))
        db.commit()  #提交事务
    return HttpResponse('Update fine')


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="django_connect"

)
#create cursor object
cursor = db.cursor()

dbmssql = pymssql.connect(
    host="10.100.50.211",
    user="sa",
    password="ABCabc123#@!",
    database="Points",
    port="1433",
    tds_version="7.0",
    as_dict=True,  #数据库内容以字典格式输出,带字段名
    charset='GBK',  #解决中文乱码
)
cursorWX = dbmssql.cursor()
cursorWX1 = dbmssql.cursor()


def WX_Login(request):
    result_list = []
    if request.method == "POST":
        UserNum = request.GET['UserNum']
        if str(UserNum) == '':
            return JsonResponse({'code': 1001, 'msg': 'id can\'t be empty'})
        query = "select hr_code from v_employee where hr_code=%s"
        cursorWX.execute(query, UserNum)
        result = cursorWX.fetchall()
        for i in result:
            result_list.append(i)
    return HttpResponse(result_list)


def WX_Basic_inf(request):
    result_list = []
    if request.method == "GET":
        query = "select * from gifts_file"
        cursorWX1.execute(query)
        #desc = cursorWX1.description  #获取字段的描述
        result = cursorWX1.fetchall()
        for res in result:
            result_list.append(res)
        #result_list.append({f"g_id:{i[0]},g_no:{i[1]},g_gfname:{i[2]},g_note:{i[3]},g_mark:{i[4]},g_sort:{i[5]},g_date:{i[6]},g_subname:{i[7]},g_img:{i[8]},g_filename:{i[9]},g_qty:{i[10]}"})
    return HttpResponse(result_list)


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
