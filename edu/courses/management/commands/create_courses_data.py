import datetime
import random
from django.core.management.base import BaseCommand
from courses.models import Course, Category, Requirements, Apply, FeesAndFunding
from users.models import UserProfile, Role

category = [
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

requirements = [
    'requirements abc',
    'requirements xzy',
    'requirements wow',
    'requirements cool',
    'requirements ok',
    'requirements by',
]

apply = [
    'apply abc',
    'apply xzy',
    'apply wow',
    'apply cool',
    'apply ok',
    'apply by',
]

fees_and_funding = [
    'Fees and funding abc',
    'Fees and funding xzy',
    'Fees and funding wow',
    'Fees and funding cool',
    'Fees and funding ok',
    'Fees and funding by',
]
short_content = [
    'Short content abc',
    'Short content xzy',
    'Short content wow',
    'Short content cool',
    'Short content ok',
    'Short content by',
]

abouts = [
    'about abc',
    'about xzy',
    'about wow',
    'about cool',
    'about ok',
    'about by',
]



teachers = [teacher.name for teacher in UserProfile.objects.filter(role__in=[Role.objects.get(name='teacher')])]


def generate_category_name():
    index = random.randint(0, 13)
    return category[index]

def generate_requirements():
    index = random.randint(0, 5)
    return requirements[index]

def generate_apply():
    index = random.randint(0, 5)
    return apply[index]

def generate_fees_and_funding():
    index = random.randint(0, 5)
    return fees_and_funding[index]

def generate_short_content():
    index = random.randint(0, 5)
    return short_content[index]

def generate_course_date():
    year = random.randint(2021, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

def generate_duration():
    return random.randint(20, 200)

def generate_price():
    return random.randint(70, 900)

def generate_about():
    index = random.randint(0, 5)
    return abouts[index]

def generate_teacher_name():
    index = random.randint(0, 10)
    return teachers[index]

def generate_discount_price():
    return random.randint(20, 50)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the courses titles.')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                gen_short_content = generate_short_content()
                gen_category_name = generate_category_name()
                gen_course_date = generate_course_date()
                gen_duration = generate_duration()
                gen_price = generate_price()
                gen_title = generate_about()
                gen_content = generate_about()
                gen_requirements = generate_requirements()
                gen_apply = generate_apply()
                gen_fees_and_funding = generate_fees_and_funding()
                gen_teacher = generate_teacher_name()
                gen_discount_price = generate_discount_price()

                category = Category.objects.get_or_create(category_name=gen_category_name)

                course = Course(
                    title=title,
                    short_content=gen_short_content,
                    category=Category.objects.get(category_name=gen_category_name),
                    course_date=gen_course_date,
                    duration=gen_duration,
                    price=gen_price,
                    about_title=gen_title,
                    content=gen_content,
                    discount_price=gen_discount_price
                )

                course.save()

                requirements = Requirements.objects.get_or_create(requirement=gen_requirements)
                course.requirements.add(Requirements.objects.get(requirement=gen_requirements))

                apply = Apply.objects.get_or_create(apply=gen_apply)
                course.apply.add(Apply.objects.get(apply=gen_apply))

                fees_and_funding = FeesAndFunding.objects.get_or_create(fees_and_funding=gen_fees_and_funding)
                course.fees_and_funding.add(FeesAndFunding.objects.get(fees_and_funding=gen_fees_and_funding))

                course.teacher.add(UserProfile.objects.get(name=gen_teacher))

        self.stdout.write(self.style.SUCCESS('Courses Data imported successfully'))
