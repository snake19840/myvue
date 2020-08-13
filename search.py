from django.http import HttpResponse
from django.shortcuts import render

# 表单
import testdb


def search_form(request):
    return render(request, 'search_form.html')


def search_form_post(request):
    return render(request, 'postHtml.html')


def search_post(request):
    r = {}
    print(request.POST['q'])
    if request.POST:
        r['rlt'] = request.POST['q']
    return render(request, "postHtml.html", r)


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    print(request.GET)
    print(request.GET['p'])
    if 'p' in request.GET and request.GET['p']:
        name = testdb.testdb3(request.GET['p'])
        message = name
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
