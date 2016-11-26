from django.contrib import admin

from .models import ResumeSection, ResumeSectionItem, Project, AboutMeSection

admin.site.register(ResumeSection)
admin.site.register(ResumeSectionItem)
admin.site.register(Project)
admin.site.register(AboutMeSection)
