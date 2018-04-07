
from __future__ import with_statement
import os

from setuptools import setup, find_packages

install_requires = [
    "mezzanine >= 4.0",
    "diff-match-patch",
    "django-reversion-compare"
]

try:
    setup(
        name="versionedpages",
        version=0.2,
        author="Peter Murphy",
        author_email="peterkmurphy@gmail.com",
        description="Permits page versioning for Mezzanine CMS.",
        long_description=open("README.rst").read(),
        license="BSD",
        #url="http://mezzanine.jupo.org/",
        zip_safe=False,
        include_package_data=True,
        packages=['versionedpages'],
        package_data={
            'versionedpages': ['templates/*.html', 'templates/**/*.html'],
        },
        install_requires=install_requires,
        entry_points="""
            [console_scripts]
        """,
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Environment :: Web Environment",
            "Framework :: Django",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Software Development :: Libraries :: "
                                                "Application Frameworks",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],)
except:
    pass
