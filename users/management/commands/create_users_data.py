import datetime
import random
from django.core.management.base import BaseCommand
from users.models import UserProfile, Role, Field, Category, Interests
from django.contrib.auth.models import User

fields = [
    'Algorithms',
    'Database',
    'Parallel computing',
    'Software engineering',
    'Data management',
    'Data mining',
    'Information management',
    'Information system',
    'Information technology',
    'Numerical analysis',
    'Computational finance ',
    'Humanistic informatics',
    'Community informatics',
    'Computer security',
]

categories = [
    'Sport',
    'Lifestyle',
    'Music',
    'Coding',
    'Travelling',
    'Communication',
    'Leadership',
    'Management',
    'Training',
    'Retail',
    'Sales ',
    'Marketing',
    'Teaching',
    'Media',
]

interests = [
    'interests type 1',
    'interests type 2',
    'interests type 3',
]

roles = [
    'user',
    'teacher',
    'admin',
]

def generate_field_name():
    index = random.randint(0, 13)
    return fields[index]

def generate_category_name():
    index = random.randint(0, 13)
    return categories[index]

def generate_interest_name():
    index = random.randint(0, 2)
    return interests[index]

def generate_role_name():
    index = random.randint(0, 2)
    return roles[index]


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains random first and last name.')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                gen_name = row
                gen_first_name = gen_name.split(' ')[0]
                gen_last_name = gen_name.split(' ')[1]
                gen_username = ".".join(gen_name.split())
                gen_email = gen_username+"@gmail.com"
                gen_password = 'EduCenter2020'
                gen_field = generate_field_name()
                gen_category = generate_category_name()
                gen_interest = generate_interest_name()
                gen_role = generate_role_name()

                field = Field.objects.get_or_create(field_name=gen_field)
                category = Category.objects.get_or_create(category_name=gen_category)

                user = User.objects.create_user(gen_username, gen_email, gen_password)
                user.first_name = gen_first_name
                user.last_name = gen_last_name
                user.is_superuser = False
                user.is_staff = False
                user.save()

                user.userprofile.name = gen_name
                user.userprofile.fields = Field.objects.get(field_name=gen_field)
                user.userprofile.category = Category.objects.get(category_name=gen_category)
                user.userprofile.description = 'description'
                user.userprofile.phone = 'phone'
                user.userprofile.facebook = 'facebook'
                user.userprofile.twitter = 'twitter'
                user.userprofile.skype = 'skype'
                user.userprofile.site = 'site'
                user.userprofile.address = 'address'

                interests = Interests.objects.get_or_create(interest=gen_interest)
                user.userprofile.interests.add(Interests.objects.get(interest=gen_interest))

                user.userprofile.biography = 'biography'
                role = Role.objects.get_or_create(name=gen_role)

                user.userprofile.role.add(Role.objects.get(name=gen_role))
                user.userprofile.save()
        self.stdout.write(self.style.SUCCESS('User and UserProfile Data imported successfully'))
