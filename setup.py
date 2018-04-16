from setuptools import find_packages, setup

setup(
    name='cloudcontrollers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.1.3',
        'click==6.7',
        'colorlog==3.1.2',
        'python-dateutil==2.7.2',
        'kubernetes==6.0.0',
        'uvloop==0.9.1',
    ],
    entry_points='''
        [console_scripts]
        cloudcontrollers = cloudcontrollers.cli:cli
    '''
)
