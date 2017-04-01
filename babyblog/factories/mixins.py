# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.utils.timezone import get_current_timezone
import os
import errno


def make_auto_now_date_factory_mixin(
        kwargs_date_names=("created", "updated")):

    class AutoNowDateFactoryMixin(factory.django.DjangoModelFactory):
        class Meta:
            pass

        @factory.post_generation
        def override_dates(self, create, extracted, **kwargs):
            if not create:
                print("Warning: date can't be overrode with a build.")
                return

            date_faker = factory.Faker('date_time_this_decade', locale='fr_FR')

            kwargs = {}
            for kwarg in kwargs_date_names:
                kwargs.update({
                    kwarg: get_current_timezone().localize(
                        date_faker.generate({}), is_dst=False),
                })

            self.__class__.objects.filter(pk=self.pk).update(**kwargs)
            self.refresh_from_db()
            return self

    return AutoNowDateFactoryMixin


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
