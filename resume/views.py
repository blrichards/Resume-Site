from django.shortcuts import render

from .models import ResumeSection, AboutMeSection, Project


def index(request):
    resume_list = ResumeSection.objects.order_by('id')
    about_me = AboutMeSection.objects.order_by()
    projects = Project.objects.order_by()

    context = {
        'resume_list': resume_list,
        'about_me': about_me,
        'resume_item_offset': len(resume_list) if len(resume_list) < 3 else 3,
        'projects': projects,
    }
    return render(request, 'index.html', context)
