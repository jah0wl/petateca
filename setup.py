import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

setup(
    name="petateca",
    version='0.1dev',
    author="",
    author_email="",
    packages=['petateca',],
    url='',
    license=open('LICENSE').read(),
    description='Web de petateca',
    long_description=open('README.md').read(),
    install_requires=[
        'Django',
        'FormEncode',
        'IMDbPY',
        'PIL',
        'SQLAlchemy',
        'SQLObject',
        'South>=0.7.3',
        'Tempita',
        'Whoosh',
        'decorator',
        'distribute',
        'django-avatar',
        'django-compress',
        'django-haystack',
        'django-indexer',
        'django-localeurl',
        'django-modeltranslation',
        'django-paging',
        'django-ratings',
        'django-registration',
        'django-rosetta',
        'django-sentry',
        'django-taggit',
        'django-templatetag-sugar',
        'django-voting',
        'docutils',
        'indexer',
        'ipython',
        'lxml',
        'simplejson',
        'sorl-thumbnail>=11.01',
        'sqlalchemy-migrate',
        'tvdb-api',
        'twitter',
        'uuid',
        'wsgiref',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
    ],
    dependency_links = [
        #XXX: For django-modeltranslation
        "http://code.google.com/p/django-modeltranslation/wiki/InstallationAndUsage",
    ],
)
