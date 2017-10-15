from django.contrib import admin

from health.models import Patient,Disease,Ques,Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'cr_date')
    list_filter = ['cr_date']
    search_fields = ['subject', 'message']
admin.site.register(Notice, NoticeAdmin)

class QuesAdmin(admin.ModelAdmin):
    list_display = ('question',)
    list_filter = ['user', 'notice']
    search_fields = ['question', 'answer']
admin.site.register(Ques, QuesAdmin)


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Disease, DiseaseAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'disease')
    list_filter = ['disease']
    search_fields = ['name']
admin.site.register(Patient, PatientAdmin)