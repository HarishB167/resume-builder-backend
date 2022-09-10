from rest_framework import serializers
from .models import Education, Experience, Language, Person, Project, Skill, Training


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', "first_name", "last_name", "email", "phone",
            'address', 'profile_statement', 'profile_link']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'subtitle', 'person', 'description', 'git_link', 'test_link']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'qualification', 'institute', 'score', 'person']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title', 'subtitle', 'person', 'start', 'end', 'responsibilities']


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'title', 'subtitle', 'person', 'description']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'person']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'person']


class PersonProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', "first_name", "last_name", "email", "phone",
            'address', 'profile_statement', 'profile_link',
            'projects', 'educations', 'experiences', 'skills',
            'languages', 'trainings']
    
    projects = ProjectSerializer(many=True)
    educations = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    skills = SkillSerializer(many=True)
    languages = LanguageSerializer(many=True)
    trainings = TrainingSerializer(many=True)

