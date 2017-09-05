import codecs

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='colorz',
    version='1.0.3',
    description='Color scheme generator.',
    long_description=long_description,
    url='https://github.com/metakirby5/colorz',
    author='Ethan Chan',
    author_email='metakirby5@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='colorz color scheme theme generator',
    py_modules=['colorz'],
    install_requires=[
        'Pillow',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'colorz=colorz:main',
        ],
    },
)
