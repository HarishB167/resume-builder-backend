from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('people', views.PersonViewSet)

people_router = routers.NestedDefaultRouter(router, 'people', lookup='person')
people_router.register('projects', views.ProjectViewSet, basename='person-projects')
people_router.register('educations', views.EducationViewSet, basename='person-educations')
people_router.register('experiences', views.ExperienceViewSet, basename='person-experiences')
people_router.register('trainings', views.TrainingViewSet, basename='person-trainings')
people_router.register('skills', views.SkillViewSet, basename='person-skills')
people_router.register('languages', views.LanguageViewSet, basename='person-languages')

urlpatterns = router.urls + people_router.urls

urlpatterns += [path('profile/<id>', views.person_profile)]



