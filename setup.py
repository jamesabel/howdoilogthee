from setuptools import setup, find_packages

description='How Do I Log Thee'

# example:
# https://github.com/pypa/sampleproject/blob/master/setup.py
setup(
    name='howdoilogthee',
    version='0.0.0',
    description=description,
    long_description=description,
    url='https://github.com/jamesabel/howdoilogthee',
    author='James Abel',
    author_email='j@abel.co',
    packages=find_packages(exclude=['test_howdoilogthee']),
    install_requires=[''],
)
