# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from time import ctime
import urllib
from .forms import addform
from .forms import *
import time
from django.contrib.messages import constants as messages
from django.contrib import messages
from one.models import *
from django.contrib.auth.decorators import permission_required
import simplejson
from django.db.models import F
# #from django_bulk_update.helper import bulk_update
# from django_bulk_update.manager import BulkUpdateManager
logger=logging.getLogger('addlog')

#@permission_required('one.修改')
@login_required(login_url="/login/")
def index(request):
    if not request.user.has_perm('one.修改'):
        return HttpResponse('没有权限')
    if request.method == 'POST':
        name = request.POST['state_province']
        print name
        return render(request, 'index.html', locals())
    else:
        return render(request,'index.html',locals())

def che(request):
    if request.method=="POST":
        check_box_list = request.POST.getlist('check_box_list')
        if check_box_list:
            print(check_box_list)
            return HttpResponse("ok")
        else:
            print("fail")
            return HttpResponse("fail")
    else:
        a = [1,2,3,4]
        return render(request,'che.html',{'a':a})

# def test3(request):
#     data = json.loads(json.dumps({"id":"ddd","name":"dd","phone":"dd"}))
#     # data = json.loads(request.body)
#     print data['name']
#     return render_to_response('my_template.html',
#                               context_instance=RequestContext(request))

def django_ajax(request):  # 主要想实现将勾选框获得json数据传给后台，后台解析json，提取参数作为
    # 作为shell的参数
    # received_json_data = simplejson.loads(request.body)
    if request.method == 'POST':
        dict = json.loads(request.POST['data'])  # 传过来的是json字符串，jsonloads解析成字典
        # 然后可以用jsondumps解析成字符串返回
        print dict
        print type(dict)
        print dict[0]["name"]
    # print request.POST.get("data")
    # print request.POST.getlist("data")[0]
    # print request.POST.getlist("data")[0][0]
    # print json.dumps(request.POST.get("data"))[0:][3]
    # print type(json.dumps(request.POST.get("data"))[5:])
    # return HttpResponse(json.loads(json.dumps(request.POST.get("data"))))
    return render(request, 'django_ajax.html', locals())


from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
@login_required(login_url="/login/")
def listing(request):
    if request.method == 'POST':
        #dict = json.loads(request.POST['data'])

        # 传过来的是json字符串，jsonloads解析成字典
        # 然后可以用jsondumps解析成字符串返回
        #print dict
        #print type(dict)
        #print dict[0]["names"]          #接下来是执行删除脚本，删除后再次用form输入的关键字再次检索给
        #print request.POST['one']
        form = addform(request.POST)
        form1=editform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state_province = form.cleaned_data['state_province']
            country = form.cleaned_data['country']
            website = form.cleaned_data['website']
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            kk = {}
            kv_list = []
            kv_dict = {}
            kv_dict["one"]="xuwei"
            kv_list.append(kv_dict)
            kk["one"] = kv_list
            restore.objects.create(date=times, user=request.user.username, option="add", qaid=city, content=kk,)
            a = eval(restore.objects.filter(qaid=city)[0].content)
            print a["one"][0]["one"]
            print name, address, city, state_province, country, website
            messages.success(request, '成功添加 ' + name + ' 的信息')
            # HttpResponseRedirect()
            return HttpResponseRedirect('/listing/')
    else:
        form = addform()
        form1 = editform()

    contact_list=[['xuwei',22,'武汉'],
                  ['xuwei',22,'武汉'],
                  ['dengtuo',22,'武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['dengtuo', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['dengtuo', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['dengtuo', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei', 22, '武汉'],
                  ['xuwei',22,'武汉']]

    print type(contact_list)
    paginator = Paginator(contact_list, 7)
    page = int(request.GET.get('page', '1'))
    try:
        contacts = paginator.page(page)
        print contacts.number
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    # if request.method == 'GET':
    #     print request.GET['data2']
    return render(request, 'list.html', locals())


def form_edit(request):
    form=editform()
    if request.method == 'POST':
        if request.POST['num']==1:
            print "成功"
        print "失败"
        print request.POST['data']
        up_dict=json.loads(request.POST['data'])
        name=up_dict[0]["names"]
        print name
        return render(request, 'index.html', locals())
    else:
        return render(request, 'index.html', locals())


from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('list.html', RequestContext(request))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            # return render_to_response('login.html', RequestContext(request, {'form': form,}))
            return render(request,'login.html',locals())

@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


@login_required(login_url="/login/")
def tools(request):
    # beginID = 1
    # try:
    #     beginID = json.loads(request.POST['the_id'])[0]['id']
    # except:
    #     print "enen"
    #     pass
    # print beginID
    # if request.user.username == 'xuwei':
    #     #contacts = data_table.objects.filter(count__lt = 6 ,id__gte =500).order_by('?')[:100]
    #     contacts = data_table.objects.filter(count__lt=10, id__gte=500).exclude(answer__contains="xuwei")[:100]
    # elif request.user.username == 'roobo1':
    #     contacts = data_table.objects.filter(count__lt = 10 ,id__gte =500).exclude(answer__contains="roobo1")[:100]
    # else:
    #     contacts = data_table.objects.filter(count__lt=10, id__gte=500).exclude(answer__contains="lsj")[:100]
    # paginator = Paginator(contacts, 100)
    # page = int(request.GET.get('page', '1'))
    # try:
    #     contacts = paginator.page(page)
    #     for contact in contacts:
    #         #data_table.objects.filter(id=contact.id).update(count=F('count') + 1)
    #         contact.count +=1
    #         contact.answer = contact.answer + request.user.username
    #     data_table.objects.bulk_update(contacts,update_fields=['count'])
    #     data_table.objects.bulk_update(contacts, update_fields=['answer'])
    #     #print contacts.number
    # except PageNotAnInteger:
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     contacts = paginator.page(paginator.num_pages)
    # if request.method == 'POST':
    #     #print "111"
    #     good_source = json.loads(request.POST['data1'])
    #     bad_source = json.loads(request.POST['data2'])
    #     for i in good_source:
    #         #print i.id
    #         data_table.objects.filter(id = i['id']).update(good_count = F('good_count')+1)
    #         #data_table.objects.filter(id=i['id']).update(count=F('count') + 1)
    #         times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #         # the_log.objects.create(qaid = i['id'],query = i['query'] ,answer = i['answer'] ,user = request.user.username
    #         #                        ,result = 0 ,datetime = times)
    #     for a in bad_source:
    #         #data_table.objects.filter(id = a['id']).update(bad_count = F('bad_count')+1)
    #         data_table.objects.filter(id=a['id']).update(count=F('count') + 1)
    #         times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #         # the_log.objects.create(qaid = a['id'],query = a['query'] ,answer = a['answer'] ,user = request.user.username
    #         #                        ,result = 1 ,datetime = times)
    #     return render(request,'tools.html',locals())
    return render(request, 'tools.html', locals())

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import  os
def upload_file(request):
    if request.method == 'POST':
        print "进来"
        form = UploadFileForm(request.POST, request.FILES)
        myFile =request.FILES.get("file", None)# 获取上传的文件，如果没有文件，则默认为None
        print type(myFile)
        for line in myFile:
            print line
        f = open(os.path.join('C:/Users/roobo/Desktop/es_tool/temp_data',myFile.name), 'wb')
        for chunk in myFile.chunks(chunk_size=1024):
            f.write(chunk)
        print os.getcwd()
        cluster = 'elasticsearch'
        index = "chat_test2"
        types = "chat"
        name = "C:/Users/roobo/Desktop/es_tool/temp_data/yuliao.txt"
        os.chdir('C:/Users/roobo/Desktop/es_tool/run_all/fmt_json')
        print os.getcwd()
        c = os.system('sh test_import2.sh' + cluster +' '+ index +' '+types +' '+ name)
        print c
        os.chdir('C:/Users/roobo/test627/Scripts/test2/Scripts/the1')
        print os.getcwd()
        if not myFile:
            return HttpResponse("no files for upload!")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})

def comments_upload(request):
    if request.method == 'POST':
        contacts = data_table.objects.all()
        print "it's a test"  # 用于测试
        print request.POST['name']  # 测试是否能够接收到前端发来的name字段
        print request.POST['password']  # 用途同上
        data = "heeh"
        #return HttpResponse("表单测试成功")  # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了
        return HttpResponse(contacts)
    else:
        #contacts = data_table.objects.all()
        return render(request,'test.html',locals())

def soft_submit(request):
    if request.is_ajax():
        id=request.POST.get('type_id')
    return HttpResponse("success")


def soft_filter(request):
    ajax_release_version=[]
    release_version=[]
    decode_data = DecodeBase.objects.all()
    paginator = Paginator(decode_data, 11)
    npage = int(request.GET.get('page', '1'))
    try:
        contactss = paginator.page(npage)
    except PageNotAnInteger:
        contactss = paginator.page(1)
    except EmptyPage:
        contactss = paginator.page(paginator.num_pages)
    pros = ProductionIntervene.objects.all().order_by('production_id')
    word =  request.POST.get('word')
    tag =  request.POST.get('tag')
    thenum = [1,2,3,4,5]
    for i in request.POST.getlist('chk_value[]'):
        if int(i) == 0 :
            if request.POST.get('operation') == "add":
                try:
                    ProductionIntervene.objects.filter(word__contains=word, production_id=0, tag__contains=tag,
                                                       opertion_id=2).delete()
                except:
                    pass
                try:
                    ProductionIntervene.objects.create(word=word, production_id=0, tag=tag, opertion_id=1)
                except:
                    pass
                for tn in thenum:
                    try:
                        ProductionIntervene.objects.filter(word__contains=word, production_id=tn, tag__contains=tag,
                                                       opertion_id=2).delete()
                    except:
                        pass
                    try:
                        ProductionIntervene.objects.filter(word=word,production_id=tn,tag=tag,opertion_id=1).delete()
                    except:
                        pass
            elif request.POST.get('operation') == "delete":
                try:
                    ProductionIntervene.objects.filter(word__contains=word, production_id=0, tag__contains=tag,
                                                       opertion_id=1).delete()
                except:
                    pass
                try:
                    ProductionIntervene.objects.create(word=word, production_id=0, tag=tag, opertion_id=2)
                except:
                    pass
                for tn in thenum:
                    try:
                        ProductionIntervene.objects.filter(word__contains=word, production_id=tn, tag__contains=tag,
                                                       opertion_id=1).delete()
                    except:
                        pass
                    try:
                        ProductionIntervene.objects.filter(word=word,production_id=tn,tag=tag,opertion_id=2).delete()
                    except:
                        pass
        if  request.POST.get('operation') == "add":
            try:
                ProductionIntervene.objects.filter(word__contains=word,production_id=0,tag__contains=tag).delete()
            except:
                pass
            try:
                ProductionIntervene.objects.filter(word__contains=word,production_id=i,tag__contains=tag,opertion_id=2).delete()
            except:
                pass
            try:
                ProductionIntervene.objects.create(word=word,production_id=i,tag=tag,opertion_id=1)
            except:
                pass
        elif request.POST.get('operation') == "delete":
            try:
                ProductionIntervene.objects.filter(word__contains=word,production_id=0,tag__contains=tag).delete()
            except:
                pass
            try:
                ProductionIntervene.objects.filter(word__contains=word,production_id=i,tag__contains=tag,opertion_id=1).delete()
            except:
                pass
            try:
                ProductionIntervene.objects.create(word=word,production_id=i,tag=tag,opertion_id=2)
            except:
                pass
    if request.method == 'POST':
        try:
            num = request.POST.get('name')
            answer = request.POST.get('password')
            print num,answer
            filter_data=DecodeBase.objects.filter(word__contains = num,tag__contains=answer)
            #geshu = DecodeBase.objects.filter(word__contains = num,tag__contains=answer).count()
        except:
            print "意外"
            filter_data = DecodeBase.objects.all()

        for i in filter_data:
            release_json = {}
            release_json["word"]=i.word
            release_json["tag"]=i.tag
            ajax_release_version.append(release_json)
        return HttpResponse(json.dumps(ajax_release_version), content_type='application/json')
    else:
        contact_list = DecodeBase.objects.all()
        geshu = DecodeBase.objects.all().count()
        paginator = Paginator(contact_list, 7)
        page = int(request.GET.get('page', '1'))
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request,'test.html',locals())