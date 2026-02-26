
from django.contrib import admin
from django.urls import path, include
import os
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root, name='api-root'),
    # Dynamically build the API root URL using the $CODESPACE_NAME environment variable
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    codespace_url = f"https://{codespace_name}-8000.app.github.dev"

    path('api/', include([
        path('activities/', include('octofit_tracker.activities.urls')),
        path('users/', include('octofit_tracker.users.urls')),
        path('teams/', include('octofit_tracker.teams.urls')),
        path('leaderboard/', include('octofit_tracker.leaderboard.urls')),
        path('workouts/', include('octofit_tracker.workouts.urls')),
    ])),
]

# Note: The API endpoints are accessible at:
#   {codespace_url}/api/[component]/
# Example: {codespace_url}/api/activities/
# This uses the $CODESPACE_NAME environment variable for codespace compatibility.
# For local development, use http://localhost:8000/api/[component]/
