from django.db import models

# Create your models here.







class UserTest(models.Model):
    username = models.CharField(
        max_length=32,
        null=True ,#允许为空
        db_column='user', # 自定义列名
        db_index=True, #只做加速索引
        verbose_name='用户名'

    )
    email = models.EmailField(max_length=32,
                              null=False,
                              verbose_name='邮箱')


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)


