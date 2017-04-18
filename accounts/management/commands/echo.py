from django.core.management.base import  BaseCommand

# at this will be generation of publicationd
class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Hello')
