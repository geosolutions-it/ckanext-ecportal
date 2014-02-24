from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-ecportal',
    version=version,
    description="CKAN extension for the European Union Open Data Portal",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Tobia Di Pisa',
    author_email='tobia.dipisa@geo-solutions.it',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.ecportal'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        ecportal=ckanext.ecportal.plugin:ECPortalPlugin
    ''',
)
