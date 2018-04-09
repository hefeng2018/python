from django.db import models

# Create your models here.

class Grades(models.Model):

  gname = models.CharField(max_length=20)
  gdate = models.DateTimeField()
  ggirlnum = models.IntegerField()
  gboynum = models.IntegerField()
  isDelete = models.BooleanField(default=False)

  class Meta:
    db_table = "grades"

  def __str__(self):
    return self.gname


class StudentsManager(models.Manager):
  def get_queryset(self):
    return super(StudentsManager, self).get_queryset().filter(isDelete=False)

  def createStudent(self, name, age, gender, contend,  grade, lastT, createT, isDel=False):
     # stu = Students()
    stu = self.model()
    stu.sname = name
    stu.sage = age
    stu.sgender = gender
    stu.scontend = contend
    stu.sgrades = grade
    stu.lasttime = lastT
    stu.createtime = createT
    stu.isDelete = isDel
    return stu



class Students(models.Model):

  ## 当自定义模型管理 objects就不存在了  Grades.objects.all() 更改 Grades.stuObj.all()
  stuObj = models.Manager()
  stuObj2 = StudentsManager()


  sname = models.CharField(max_length=20)
  sgender = models.BooleanField(default=True)
  sage = models.IntegerField()
  scontend = models.CharField(max_length=20)
  isDelete = models.BooleanField(default=False)
  ### 关联外键
  sgrades = models.ForeignKey("Grades", on_delete=models.CASCADE)

  def __str__(self):
    return self.sname

  lasttime = models.DateTimeField(auto_now=True)
  createtime = models.DateTimeField(auto_now_add=True)
  class Meta:
    db_table = "students"
    ordering = ['-id']    # 降序

    # ordering = ['+id']  # 升序

  ###  定义一个 类方法创建对象
  @classmethod
  def createStudent(cls, name, age, gender, contend,  grade, lastT, createT, isDel=False):
    stu = cls(sname=name, sage=age, sgender=gender, scontend=contend, sgrades=grade, lasttime=lastT, createtime=createT, isDelete=isDel)
    return stu

class Nav(models.Model):
  img = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  trackid = models.CharField(max_length=100)
  isDelete = models.BooleanField(default=False)
  def __str__(self):
    return self.name
  class Meta:
    db_table = "nav"

class MustBuy(models.Model):
  img = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  trackid = models.CharField(max_length=100)
  isDelete = models.BooleanField(default=False)
  def __str__(self):
    return self.name
  class Meta:
    db_table = "must_buy"

class Wheel(models.Model):
  img = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  trackid = models.CharField(max_length=100)
  isDelete = models.BooleanField(default=False)
  def __str__(self):
    return self.name
  class Meta:
    db_table = "wheel"

class Goods(models.Model):
  productid = models.IntegerField()
  productimg = models.CharField(max_length=255)
  productname = models.CharField(max_length=255)
  productlongname = models.CharField(max_length=255)
  isxf = models.CharField(max_length=255)
  pmdesc = models.CharField(max_length=255)
  specifics = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  marketprice = models.CharField(max_length=255)
  categoryid = models.IntegerField()
  childcid = models.IntegerField()
  childcidname = models.CharField(max_length=255)
  dealerid = models.IntegerField()
  storenums = models.IntegerField()
  productnum = models.IntegerField()
  isDelete = models.BooleanField(default=False)
  def __str__(self):
    return self.productname
  class Meta:
    db_table = "goods"