# Django EduCenter

- [EduCenter](http://demo.themefisher.com/educenter/) is an educational website template with affluent, contemporary, modern and trendy features for your majestic presence in web with a simple user interface. It’s a multipage website template consists the must-have features like home, about, courses, events, blogs and contacts that will add enormous value in your website and take it to a new height.

- However, you can use EduCenter as an online teaching platform, school and university websites without any complication as the appearance of the website is very user-friendly.

- EduCenter have store, so let's summarize each one:

1. USER - Built in Django user model,  insrtance created for each customer who registers.

2. CUSTOMER (UserProfile) - Along with a User model, each customer will contain a Customer model that holds a one to one relationship to each user. (OneToOneFied)

3. PRODUCT (Course) - The product model represents products we have in store.

4. ORDER - The order model will represent a transaction that is placed or pending. The model will hold information such as the transaction ID, data completed and order status. This model will be a child or the customer model but a parent to Order Items.

5. ORDERITEM - An order Item is one item with an order. For example, a shopping cart may consist of many items but is all part of one order. Therfore the OrderItem model will be a child of the PRODUCT model AND the ORDER Model.

6. SHIPPING - Not every order will need shipping information. For orders containing physical products that need to be shipping we will need to create an instance of the shipping model to know where to send the order. Shipping will simply be a child of the order model when necessary.

--

## To run locally, do the usual:

### 1. Create a Python virtualenv

- Installing virtualenv
```sh
$ python3 -m pip install --user virtualenv
```

- Creating a virtual environment
```sh
$ virtualenv -p python3 venv
```

- Activating a virtual environment
```sh
$ source venv/bin/activate
```

### 2. Install dependencies:
```sh
$ pip install -r requirements/common.txt
```

### 3. Perform database migration:
1)
```sh
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

2) delete the `db.sqlite3`

3)
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser:
```sh
$ ./manage.py createsuperuser
```

### 5. Run Development Server
```sh
$ python manage.py runserver
```

## Advice

### GIT

- For new feature

```sh
$ git checkout -b feature
```

```sh
git branch

git checkout master
git pull origin master
git merge feature
git push origin master

git branch -d feature
```

### SECRET_KEY 

#### published

#### Load key from environment variable
- Instead of publishing your secret key, you can use an environment variable to set your secret key.

```py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

#### Load secret key from file
- Alternatively, you can read the secret key from a file.
```py
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
new_key = get_random_string(50, chars)

with open("./secret_key.txt", "w+") as f:
    f.write(new_key)
    f.seek(0)
    SECRET_KEY = f.read().strip()

#or

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
```



## More


### Renders a graphical overview of your project or specified apps

```sh
$ python manage.py graph_models -a -o edu.png
```

### A short Query Reminder

```sh
$ python manage.py shell

>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> User.objects.first()
>>> User.objects.filter(username='TestUser')
>>> User.objects.filter(username='TestUser').first()
>>> user = User.objects.filter(username='TestUser').first()
>>> user
>>> user.id
>>> user.pk
>>> user = User.objects.get(id=1)

>>> Post.objects.all()
>>> post_1 = Post(title='Blog 1', content='First post', author=user)
>>> Post.objects.all()
>>> post_1.save()
>>> Post.objects.all()

>>> User.objects.all()
>>> post.content
>>> post.date_posted

>>> user
>>> user.post_set.all()
>>> user.post_set.create(title='Blog 3', content='Thrid post')
>>> exit() 
```

### Save Requirements
```sh
$ pip3 freeze --local > requirements.txt
```

### Deployment

- Set the `STATIC_ROOT` setting to the directory from which you’d like to serve these files, for example:
```sh
$ STATIC_ROOT = "/var/www/example.com/static/"
```

- Run the `collectstatic` management command:
```sh
$ python manage.py collectstatic
```
This will copy all files from your static folders into the `STATIC_ROOT` directory.

- In root create `passenger_wsgi.py` and put
```py
from project_name.wsgi import application
```

### References/Recommendation to read

- [GIT - CoreyMSchafer](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog)
- [Stories about Python, Django and Web Development](https://simpleisbetterthancomplex.com)
- [GIT - Blog about Python, Django and Web development](https://github.com/sibtc)
- [Add inline model to django admin site](https://stackoverflow.com/questions/33748059/add-inline-model-to-django-admin-site)
- [Run the test suite](https://github.com/django/django/tree/master/tests)
- [Django's ManyToMany Relationship with Additional Fields](https://stackoverflow.com/questions/4443190/djangos-manytomany-relationship-with-additional-fields)
- [Extra fields on many-to-many relationships](https://docs.djangoproject.com/en/2.1/topics/db/models/#extra-fields-on-many-to-many-relationships)
- [How to fetch the top two products for each product type?](https://stackoverflow.com/questions/1357478/how-to-fetch-the-top-two-products-for-each-product-type?rq=1)
- [How to display a query set in the django admin?](https://stackoverflow.com/questions/17204640/how-to-display-a-query-set-in-the-django-admin)
- [JustDjango](https://github.com/justdjango)
- [Django Admin filter on Foreign Key property](https://stackoverflow.com/questions/2379702/django-admin-filter-on-foreign-key-property)
- [Creating Custom Filters for list_filter in Django Admin](https://stackoverflow.com/questions/12102697/creating-custom-filters-for-list-filter-in-django-admin)
- [filter foreignkey field in django admin](https://stackoverflow.com/questions/10179129/filter-foreignkey-field-in-django-admin)
- [How to add multiple objects to ManyToMany relationship at once in Django ?](https://stackoverflow.com/questions/4959499/how-to-add-multiple-objects-to-manytomany-relationship-at-once-in-django)
- [ManyRelatedManager](https://stackoverflow.com/questions/8095813/attributeerror-manyrelatedmanager-object-has-no-attribute-add-i-do-like-in)
- [Using Django's m2m_changed to modify what is being saved pre_add](https://stackoverflow.com/questions/26493254/using-djangos-m2m-changed-to-modify-what-is-being-saved-pre-add)
- [How to create an object for a Django model with a many to many field?](https://stackoverflow.com/questions/6996176/how-to-create-an-object-for-a-django-model-with-a-many-to-many-field)
- [An example of using many-to-many "through" to augment m2m relationships](https://gist.github.com/jacobian/827937)
- [How to express a One-To-Many relationship in Django](https://stackoverflow.com/questions/6928692/how-to-express-a-one-to-many-relationship-in-django)
- [Search Engine Optimisation (SEO) for Django sites](https://djangopackages.org/grids/g/seo/)
- [Django ManyToMany filter()](https://stackoverflow.com/questions/2218327/django-manytomany-filter)
- [Create a card token](https://stripe.com/docs/api/tokens/create_card)
- [Change slug in django use slugify](https://stackoverflow.com/questions/29293096/change-slug-in-django-use-slugify)
- [How to create a unique slug in Django](https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django)
- [Django Unique Slug by id](https://stackoverflow.com/questions/11978035/django-unique-slug-by-id)
- [Django post_save() signal implementation](https://stackoverflow.com/questions/13014411/django-post-save-signal-implementation)
- [Django Projects](https://www.codingforentrepreneurs.com)
- [Django & Chart js integration ](https://pyplane.com/blog/how-to-create-charts-in-django-with-chart-js/)
- [Learn how to integrate Chart.js with Django](https://github.com/codingforentrepreneurs/Django-Chart.js)
- [eCommerce](https://github.com/codingforentrepreneurs/eCommerce)
- [Examples of model relationship API usage](https://docs.djangoproject.com/en/3.0/topics/db/examples/)
- [Themify icons](http://thetheme.io/theadmin/content/icons-themify.html)
