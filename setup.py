from setuptools import setup
from querycount import __version__

url = "https://github.com/kaajavi/django-showmequeries/tarball/{0}".format(__version__)

setup(
    name="django-showmequeries",
    version=__version__,
    original_author="Brad Montgomery",
    author="Javier Guignard",
    author_email="kaajavi@gmail.com",
    description=("Middleware that Prints statics of DB queries to the runserver console."),
    install_requires=[],
    license="MIT",
    keywords="django querycount queries database performance",
    url=url,
    packages=[
        "quericount",
    ],
    long_description="this project gives you a middleware that"
    "prints statics of DB queries to the runserver console.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        "Topic :: Utilities",
    ],
)
