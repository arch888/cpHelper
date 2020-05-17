from setuptools import setup


setup(
    name = 'cpHelper',
    version = '0.1.0',
    packages = ['cpHelper'],
    entry_points = {
        'console_scripts': [
            'leet = leetCode.__main__:main'
        ]
    })