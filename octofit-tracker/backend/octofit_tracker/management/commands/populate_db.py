from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Black Widow'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        User.objects.create(email='cap@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        User.objects.create(email='thor@marvel.com', name='Thor', team='Marvel', is_superhero=True)
        User.objects.create(email='blackwidow@marvel.com', name='Black Widow', team='Marvel', is_superhero=True)
        User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)
        User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True)
        User.objects.create(email='flash@dc.com', name='Flash', team='DC', is_superhero=True)

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30, date=date.today())
        Activity.objects.create(user='Batman', activity_type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user='Wonder Woman', activity_type='Swimming', duration=60, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for superheroes.', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
