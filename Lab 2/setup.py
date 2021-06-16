from setuptools import setup

setup(
    name='serializers',
    version='1.0',
    description='LR2',
    packages=['serializers'],
    author='Anton Moskalev',
    author_email='moskanton@mail.ru',
    entry_points={
        'console_scripts': [
            'run = serializers.main:main'
        ]})
