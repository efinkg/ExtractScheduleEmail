from distutils.core import setup

setup(
    # Application name:
    name="ExtractSchedule",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Ethan Glassman",
    author_email="ethan.glassman@gmail.com",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "beautifulsoup","icalendar","urllib3"
    ],
)
