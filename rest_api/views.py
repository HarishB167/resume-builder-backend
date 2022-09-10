from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Education, Experience, Language, Person, Project, Skill, Training
from .serializers import EducationSerializer, ExperienceSerializer, LanguageSerializer, PersonProfileSerializer, PersonSerializer, ProjectSerializer, SkillSerializer, TrainingSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


@api_view()
def person_profile(request, id):
    try:
        queryset = Person.objects \
            .prefetch_related('projects', 'educations', 'experiences',
                'trainings','skills', 'languages') \
            .get(pk=id)
        serializer = PersonProfileSerializer(queryset)
        return Response(serializer.data)
    except Person.DoesNotExist:
	    return Response(f"Person with id {id} doesn't exist", status=status.HTTP_404_NOT_FOUND)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(person_id=self.kwargs['person_pk'])


class EducationViewSet(ModelViewSet):
    serializer_class = EducationSerializer

    def get_queryset(self):
        return Education.objects.filter(person_id=self.kwargs['person_pk'])


class ExperienceViewSet(ModelViewSet):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(person_id=self.kwargs['person_pk'])


class TrainingViewSet(ModelViewSet):
    serializer_class = TrainingSerializer

    def get_queryset(self):
        return Training.objects.filter(person_id=self.kwargs['person_pk'])


class SkillViewSet(ModelViewSet):
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.filter(person_id=self.kwargs['person_pk'])


class LanguageViewSet(ModelViewSet):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return Language.objects.filter(person_id=self.kwargs['person_pk'])


