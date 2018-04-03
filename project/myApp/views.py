from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpRequest


def index(request):
  return HttpResponse("HELLOWORD")



def tests(request):
  return render(request, 'myApp/hell.html', {"sname": "hellow"})


from .models import Students, Grades
def students(request):
  studentsList = Students.stuObj2.all()
  return render(request, 'myApp/students.html', {"students": studentsList})

### 列表分页
def students1(request, page):
  page = int(page)
  num = 2
  studentsList = Students.stuObj2.all()[(page-1) * num:page * num]
  return render(request, 'myApp/students.html', {"students": studentsList})


def addstudent(request):
  grade = Grades.objects.get(pk=1)
  stu = Students.createStudent("周星驰", 55, True, "我是导演", grade, "2017-09-09", "2016-07-07")
  stu.save()
  return HttpResponse("添加成功！")

def addstudent1(request):
  grade = Grades.objects.get(pk=2)
  stu = Students.stuObj2.createStudent("曾褒义", 35, False, "我是明星", grade, "2011-11-29", "2011-07-07")
  stu.save()
  return HttpResponse("添加成功！")

from django.db.models import F, Q

def grades(request):
  f = Grades.objects.filter(ggirlnum__gt=F("gboynum"))
  print(f)
  return HttpResponse("oooooo1")

def grades1(request):
  q = Students.stuObj2.filter(Q(pk__lt=3) | Q(sage__gt=30))
  print(q)
  return HttpResponse("oooooo2")

# http://127.0.0.1:8000/get1?a=100&b=1000&c=10000
def get1(request):
  a = request.GET.get('a')
  b = request.GET.get('b')
  c = request.GET.get('c')
  return HttpResponse(a + " " + b + " " + c)

def attribles(request):
  print(request.POST)
  print(request.GET)
  print(request.path)
  print(request.FILES)
  print(request.COOKIES)
  print(request.session)
  print(request.encoding)
  return HttpResponse("1111")

def reg(request):
  return render(request, "myApp/reg.html")

def regsave(request):
  username = request.POST.get("username")
  password = request.POST.get("password")
  print(username)
  print(password)
  return HttpResponse("post")

def setCookieTest(request):
  res = HttpResponse()
  cookie = res.set_cookie("sunck", "good")
  return res

def getCookieTest(request):
  res = HttpResponse()
  cookie = request.COOKIES
  res.write("<h1>" + cookie["sunck"] + "</h1>")
  return res

def deleteCookieTest(request):
  res = HttpResponse()
  res.delete_cookie('sunck')
  return res

from django.http import HttpResponseRedirect
### 重定向
def redirect1(request):
  return HttpResponseRedirect('/red2')

def redirect2(request):
  return HttpResponse("我是重定向后的视图")

from django.shortcuts import redirect
### 重定向
def redirect3(request):
  return redirect('/red3/')

def redirect4(request):
  return HttpResponse("我是重定向后的视图")


def login(request):
  if 'username' in request.session:
    return redirect('/main/')
  return  render(request, "myApp/login.html")

def actionLogin(request):
  username = request.POST.get("username")
  password = request.POST.get("password")
  request.session["username"] = username
  request.session["password"] = password
  return redirect('/main/')

def main(request):
  username = request.session.get("username", "游客")
  return render(request, "myApp/main.html", {"username":username})

from django.contrib.auth import logout
def logout1(request):
  logout(request)
  return redirect('/main/')