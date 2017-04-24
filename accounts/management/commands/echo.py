from django.core.management.base import BaseCommand
import sys
import random

from accounts.models import User

from publications.models import Publication

# at this will be generation of publicationd
class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all().values_list("id", flat=True)
        rand_user = random.choice(users)
        # print(rand_user)

        for index in range(1000):
            Publication.objects.create(title="title",
                                       body="body",
                                       image="publication/21407321-769a-45b1-97e0-62d11a9777f9.jpg",
                                       author=User.objects.get(pk=rand_user))
