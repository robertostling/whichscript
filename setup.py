from setuptools import setup

setup(
        name='whichscript',
        version='0.1',
        description='Unicode script identification',
        url='https://github.com/robertostling/whichscript',
        author='Robert Östling',
        author_email='robert@ling.su.se',
        license='GNU GPLv3',
        packages=['whichscript'],
        package_data={'whichscript': ['data/*.txt', 'data/download.sh']})

