from setuptools import setup


setup(
    name = 'cpHelper',
    version = '0.1.0',
    packages = ['leetCode', 'cpHelper', 'codeChef', 'codeForces'],
    entry_points = {
        'console_scripts': [
        	'cpHelper = cpHelper.__main__:main',
            'leet = leetCode.__main__:main',
            'chef = codeChef.__main__:main',
            'forces = codeForces.__main__:main'
        ]
    })