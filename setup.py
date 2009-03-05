from setuptools import setup, find_packages

setup(
    name = "django-supermodels",
    version = "1.0",
    packages = find_packages("src"),
    package_dir = {"":"src"},
    
    author = "Guilherme Chapiewski",
    author_email = "guilherme.chapiewski@gmail.com",
    description = "Tunned models for Django.",
    license = "Apache License 2.0",
    keywords = "django models",
    url = "http://guilhermechapiewski.github.com/django-supermodels", # change for lighthouse
    long_description = "Tunned models for Django.",
    download_url = "http://github.com/guilhermechapiewski/django-supermodel",
)
