from django.contrib import admin

from .models import Grades, Students, Wheel, Nav

# Register your models here.
class StudentInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    ### 列表属性
    inlines = [StudentInfo]
    list_display = ['pk', 'gname', 'gdate', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 1

    ### 添加/修改属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    fieldsets = [
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("bast", {"fields": ['gname', 'gdate', 'isDelete']})
                 ]


class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"
    # def sname1(self):
    #     return self.sname
    # sname1.short_description = "姓名"

    list_display = ["pk", "sname", "sage", gender, "scontend", "sgrades", "isDelete"]
    fields = ["sname", "sage", "sgender", "scontend", "isDelete", "sgrades"]


class WheelAdmin(admin.ModelAdmin):
    list_display = ["pk", "img", "name", "trackid", "isDelete"]
    fields = ["img", "name", "trackid", "isDelete"]
class NavAdmin(admin.ModelAdmin):
    list_display = ["pk", "img", "name", "trackid", "isDelete"]
    fields = ["img", "name", "trackid", "isDelete"]


admin.site.register(Grades, GradesAdmin)
admin.site.register(Students, StudentAdmin)
admin.site.register(Wheel, WheelAdmin)
admin.site.register(Nav, NavAdmin)




