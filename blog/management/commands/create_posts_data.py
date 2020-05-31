import datetime
import random
from django.core.management.base import BaseCommand
from blog.models import Post, Category, Comment
from users.models import UserProfile
from django.contrib.auth.models import User

short_contents = [
    "Two Down, One to Go - Two things have been completed, but there is one more that has yet to be finished.",
    "Ugly Duckling - One who may seem plain at first in appearance or capability.",
    "Let Her Rip - Permission to start, or it could mean 'go faster!'",
    "Poke Fun At - Making fun of something or someone; ridicule.",
    "Under the Weather - Not feeling well, in health or mood.",
    "Fit as a Fiddle - Being fit as a fiddle means to be in perfect health.",
    "Every Cloud Has a Silver Lining - To be optimistic, even in difficullt times.",
    "It's Not All It's Cracked Up To Be - Failing to meet expectations; not being as good as people say.",
    "Tug of War - It can refer to the popular rope pulling game or it can mean a struggle for authority.",
    "When the Rubber Hits the Road - When something is about to begin, get serious, or put to the test.",
    "Keep On Truckin' - To keep going, pressing forward; never stopping.",
    "Read 'Em and Weep - Often said by the winner in poker, as the others 'weep' over the loss.",
    "Hit Below The Belt - A boxing term. Also often used to refer to inappropriate words.",
    "Quality Time - Spending time with another to strengthen the relationship.",
    "Wild Goose Chase - Futilely pursuing something that will never be attainable.",
    "Shot In the Dark - An attempt that has little chance for success.",
    "Wouldn't Harm a Fly - Nonviolent; someone who is mild or gentle.",
    "Break The Ice - Breaking down a social stiffness.",
    "Quick On the Draw - Performing an action with the greatest of haste.",
    "Down To The Wire - A tense situation where the outcome is decided only in the last few seconds.",
    "No Ifs, Ands, or Buts - Finishing a task without making any excuses.",
]

contents = [
    'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
    'Even with the snow falling outside, she felt it appropriate to wear her bikini.',
    'The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.',
    'The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup.',
    "It doesn't sound like that will ever be on my travel list.",
    'The lyrics of the song sounded like fingernails on a chalkboard.',
    'I would have gotten the promotion, but my attendance wasn’t good enough.',
    'Italy is my favorite country; in fact, I plan to spend two weeks there next year.',
    'As he looked out the window, he saw a clown walk by.',
    'Courage and stupidity were all he had.',
    'I love bacon, beer, birds, and baboons.',
    'We have young kids who often walk into our room at night for various reasons including clowns in the closet.',
    'He found the chocolate covered roaches quite tasty.',
    'His ultimate dream fantasy consisted of being content and sleeping eight hours in a row.',
    'He had concluded that pigs must be able to fly in Hog Heaven.',
    "I may struggle with geography, but I'm sure I'm somewhere around here.",
    'I am happy to take your donation; any amount will be greatly appreciated.',
    "You can't compare apples and oranges, but what about bananas and plantains?",
    'She cried diamonds.',
    'Lucifer was surprised at the amount of life at Death Valley.',
    'Be careful with that butter knife.',
    'I think I will buy the red car, or I will lease the blue one.',
    'She saw no irony asking me to change but wanting me to accept her for who she is.',
    "It's difficult to understand the lengths he'd go to remain short.",
    "They're playing the piano while flying in the plane.",
    'I often see the time 11:11 or 12:34 on clocks.'
]

categories = [
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

comments = [
    'Tnx',
    'Good sotry',
    'Nice',
    'Woow',
    'Cool',
    'Good example',
    'Ok',
    'Beer',
    'Adio',
]

authors = [a.username for a in User.objects.all()]


def generate_short_content():
    index = random.randint(0, 20)
    return short_contents[index]

def generate_content():
    index = random.randint(0, 25)
    return contents[index]

def generate_post_date():
    year = random.randint(2015, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

def generate_author_name():
    index = random.randint(0, 50)
    return authors[index]

def generate_category_name():
    index = random.randint(0, 13)
    return categories[index]

def generate_comment():
    index = random.randint(0, 8)
    return comments[index]

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the posts titles.')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                gen_title = row
                gen_short_content = generate_short_content()
                gen_content = generate_content()
                gen_category_name = generate_category_name()
                gen_post_date = generate_post_date()
                gen_author = generate_author_name()

                autor_of_post = User.objects.filter(username=gen_author).first()

                post = Post(
                    title=gen_title,
                    short_content=gen_short_content,
                    content = gen_content,
                    date_posted=gen_post_date,
                    author=autor_of_post,
                )

                post.save()

                category = Category.objects.get_or_create(title=gen_category_name)
                post.categories.add(Category.objects.get(title=gen_category_name))

                gen_user = generate_author_name()
                gen_comment = generate_comment()
                autor_of_comment = User.objects.filter(username=gen_user).first()

                comment = Comment(
                    user = autor_of_comment,
                    content = gen_comment,
                    post = post,
                )

                comment.save()

                gen_user2 = generate_author_name()
                gen_comment2 = generate_comment()
                autor_of_comment2 = User.objects.filter(username=gen_user2).first()

                comment2 = Comment(
                    user = autor_of_comment2,
                    content = gen_comment2,
                    post = post,
                )

                comment2.save()

                gen_user3 = generate_author_name()
                gen_comment3 = generate_comment()
                autor_of_replay = User.objects.filter(username=gen_user3).first()

                replay = Comment(
                    user = autor_of_replay,
                    content = gen_comment3,
                    post = post,
                    parent = comment
                )

                replay.save()

        self.stdout.write(self.style.SUCCESS('Posts Data imported successfully'))