from django.contrib import admin

from products.models import number, prod,mobile,acc,all,noacc,noall,nomob

# Register your models here[]
admin.site.register(prod)
admin.site.register(number)
admin.site.register(mobile)
admin.site.register(acc)
admin.site.register(all)
admin.site.register(noacc)
admin.site.register(nomob)
admin.site.register(noall)