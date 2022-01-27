from django.contrib import admin

# Register your models here.
from .models import Question, Company, Choice, Statistics, Member, CouponMaster, CouponPublish, UpdateFromDB

admin.site.register(Question)
admin.site.register(Company)
admin.site.register(Choice)
admin.site.register(Statistics)
admin.site.register(Member)
admin.site.register(CouponMaster)
admin.site.register(CouponPublish)
admin.site.register(UpdateFromDB)

