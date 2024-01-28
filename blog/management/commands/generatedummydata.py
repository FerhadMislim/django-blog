from django.core.management.base import BaseCommand
from blog.models import Category, Post, Comment
from faker import Faker

class Command(BaseCommand):
    help = "Creates dummy data for testing"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help="Indicates the number of dummy posts to create")

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']
        for i in range(total):
            category = Category.objects.create(name=f"Category {i}")
            post = Post.objects.create(
                title=f"Post {i}",
                body=fake.paragraph(nb_sentences=10)  # Use Faker to generate random paragraphs
            )
            post.categories.add(category)
            Comment.objects.create(
                author=fake.name(),
                body=fake.paragraphs(nb=3),  # Use Faker to generate random paragraphs
                post=post
            )
        self.stdout.write(self.style.SUCCESS(f"Successfully created {total} posts"))

# to create 10 dummy posts, run the following command:
# python manage.py generatedummydata 10