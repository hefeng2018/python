from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^tests/$', views.tests),
  url(r'^stuList/$', views.students),
  url(r'^stuList1/(\d+)$', views.students1),
  url(r'^addStu/$', views.addstudent),
  url(r'^addStu1/$', views.addstudent1),
  url(r'^f/$', views.grades),
  url(r'^q/$', views.grades1),
  url(r'^attribles/$', views.attribles),
  url(r'^attribles/$', views.attribles),
  url(r'^get1$', views.get1),
  url(r'^reg/', views.reg),
  url(r'^regsave/', views.regsave),
  ### cookie
  url(r'^setcookie/', views.setCookieTest),
  url(r'^getcookie/', views.getCookieTest),
  url(r'^delcookie/', views.deleteCookieTest),
  ### 重定向
  url(r'^red1/', views.redirect1),
  url(r'^red2/', views.redirect2),
  url(r'^red3/', views.redirect3),
  url(r'^red4/', views.redirect4),


  ### 登入功能
  url(r'^login/', views.login),
  url(r'^actionLogin/', views.actionLogin),
  url(r'^main/', views.main),
  url(r'^logout/', views.logout1),

  ### axf
  url(r'^home/', views.home),
  url(r'^mine/', views.mine),
  url(r'^market/', views.market),
  url(r'^cart/', views.cart),
  url(r'^base/', views.base1),
]