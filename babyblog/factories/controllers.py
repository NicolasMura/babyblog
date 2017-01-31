# from .user import UserFactory
from __future__ import unicode_literals

from django.contrib.auth.models import User
from zn_auth.models import Profile
from babyblog.models import Post
from .post import PostFactory
from .user import UserFactory
import urllib
from random import randint


def create_set_of_fake_data(
        user_count=10,
        post_count_max_per_user=1,
        post_comments_max_per_post=2):
    """
    Main function to create a whole set of data for populate demo site
    """

    for user in range(user_count):
        new_user = create_user(user_count)

        # For this new user, create some posts
        nb_posts = randint(1, post_count_max_per_user)
        for post in range(nb_posts):
            create_post(
                user=new_user,
                post_count_max_per_user=post_count_max_per_user
            )

    # For each created user, create some comments
    # Hence, a post may have no comments
    new_users = User.objects.all()
    new_posts = Post.objects.all()
    for user in new_users:
        post = new_posts[randint(0, len(new_posts) - 1)]
        create_comments(
            user=user,
            related_post=post,
            post_comments_max_per_post=post_comments_max_per_post
        )


def create_user(user_count):
    new_user = UserFactory.create()
    new_profile = Profile.objects.get(user=new_user)
    # Get image from lorempixel.com and save it to upload folder
    urllib.urlretrieve(
        'http://lorempixel.com/50/50/',
        'media/upload/avatars/fake-avatar-' + str(new_profile.id) + '.jpg')
    # Set saved avatar for new profile
    new_profile.avatar = 'upload/avatars/fake-avatar-' + str(
        new_profile.id) + '.jpg'
    new_profile.save()

    # Get user object
    user_id = new_user.id
    new_user = User.objects.get(pk=user_id)

    return new_user


def create_post(user, post_count_max_per_user):
    new_post = PostFactory.create(user=user)

    # Get post object
    post_id = new_post.id
    new_post = Post.objects.get(pk=post_id)

    return new_post


def create_comments(user, related_post, post_comments_max_per_post):
    nb_comments = randint(1, post_comments_max_per_post)
    for comment in range(nb_comments):
        PostFactory.create(
            user=user,
            parent=related_post,
            image=None
        )
