# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from babyblog.factories.controllers import create_set_of_fake_data


class Command(BaseCommand):
    help = 'Create a set of fake data'

    def handle(self, *args, **options):
        create_set_of_fake_data()
