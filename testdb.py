from django.http import HttpRequest, HttpResponse

from TestModel.models import Test


def testdb(request):
    a=['张22','张33','张44','张55','张66']
    for i in a:
        test1=Test(name=i)
        test1.save()
    return HttpResponse("<p>数据添加成功</p>")


def testdb3(n):
    response2 = Test.objects.filter(id=n)
    for i in response2:
        response1=i.name
    a=response1
    return a



def testdb2(request):
    response = ""
    response1 = ""


    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    listAll = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=5)

    for i in response2:
        response1=i.name
    response=response1

    # 获取单个对象
    response3 = Test.objects.get(id=1)



    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in listAll:
        response1 += var.name + " "
    # response = response1

    return HttpResponse("<p>" + response + "</p>")
    # 更新数据
