from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'person']


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['qualification', 'institute', 'person']


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'person']


@admin.register(models.Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'person']


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'person']

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'person']



