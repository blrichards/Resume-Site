from django.db import models


class ResumeSection(models.Model):
    title = models.CharField(max_length=200)
    icon_name = models.CharField(max_length=20, default='book')
    inline = models.BooleanField(default=False);

    def __str__(self):
        return self.title


class ResumeSectionItem(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE)
    first = models.BooleanField('first', blank=True, default=False)
    prefix = models.CharField('prefix', blank=True, null=True, max_length=50)
    start_date = models.DateField('start', blank=True, null=True)
    end_date = models.DateField('end', blank=True, null=True)
    header = models.CharField(max_length=100, default='HEADER')
    description = models.CharField('description', blank=True, null=True, max_length=500)

    def __str__(self):
        return self.header


class AboutMeSection(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)

    def __str__(self):
        return self.title + ": " + self.body


class Project(models.Model):
    name = models.CharField(blank=False, max_length=50)
    category = models.CharField(blank=False, max_length=200)
    img_name = models.CharField(blank=False, max_length=20)
    link = models.CharField(blank=True, max_length=2000)

    def __str__(self):
        return self.name
