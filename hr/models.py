from django.db import models
from django.db.models import Model


# 民族信息表
class Nation(Model):
    name = models.CharField('名称', max_length=32)


# 用户信息
class UserInfo(Model):
    sex_c = ((1, '男'), (0, '女'))
    marriage_c = ((0, '未婚'), (1, '已婚'))
    health_c = ((0, '良好'), (1, '好'))
    name = models.CharField('姓名', max_length=32)
    age = models.IntegerField('年龄')
    sex = models.IntegerField('性别', choices=sex_c)
    native_place = models.CharField('籍贯', max_length=64)
    marriage = models.IntegerField('婚姻状况', choices=marriage_c)
    height = models.IntegerField('身高')
    weight = models.IntegerField('体重')
    health = models.IntegerField('健康状况', choices=marriage_c)
    qq = models.CharField('QQ', max_length=12)
    phone = models.CharField('手机号', max_length=11)
    nation = models.ForeignKey('Nation', verbose_name='民族')
    address = models.CharField('地址', max_length=200)
    idcard = models.CharField('身份证', max_length=18)
    email = models.EmailField('邮箱', max_length=128)
    max_education = models.CharField('最高学历', max_length=18)
    max_degree = models.CharField('最高学位', max_length=18)
    graduate_data = models.DateField('毕业时间')
    earliest_data = models.CharField('最早到岗时间', max_length=10)
    min_salary = models.IntegerField('最低薪资', )


# 家庭信息
class Family(Model):
    relationship_c = ((0, '配偶'), (1, '父母'),)
    user = models.ForeignKey('UserInfo')
    name = models.CharField('姓名', max_length=32)
    relationship = models.IntegerField('关系', choices=relationship_c)
    company = models.CharField('工作单位', max_length=128)
    position = models.CharField('职位', max_length=128)


# 学习经历
class Learn_Experience(Model):
    user = models.ForeignKey('UserInfo')
    school = models.CharField('学习名称', max_length=48)
    major = models.CharField('专业', max_length=25)
    entrance_data = models.DateField('入学时间')
    graduate_data = models.DateField('毕业时间')
    witness = models.CharField('证明人', max_length=25)
    student_id = models.CharField('学号', max_length=25)


# 工作经历
class Work_History(Model):
    user = models.ForeignKey('UserInfo')
    company = models.CharField('工作单位', max_length=48)
    position = models.CharField('职位', max_length=128)
    salary = models.IntegerField('薪资')
    start = models.DateField('入职时间')
    end = models.DateField('离职时间')

class UserOther(Model):
    user = models.ForeignKey('UserInfo')
    opinion = models.TextField('职位看法')
    showme = models.TextField('自我描述')

# 技能
class Skill(Model):
    name = models.CharField('名称',max_length=32)
    user = models.ManyToManyField('UserInfo')