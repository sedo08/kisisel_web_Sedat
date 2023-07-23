from django.contrib import admin
from sample.models import sample

# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    list_display=['title1', 'price']
    list_filter= ['title1', 'title2']
    list_display_links = ['title1']

    class Meta:

        model = sample


admin.site.register(sample, SampleAdmin)
