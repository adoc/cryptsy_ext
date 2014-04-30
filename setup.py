import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = '' #open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pusher',
    'redis'
    ]

setup(name='cryptsy_ext',
      version='0.1',
      author='adoc',
      author_email='adoc@code.webmob.net',
      url='https://code.webmob.net/cryptsy_ext',
      download_url='https://github.com/adoc/cryptsy_ext',
      license='http://opensource.org/licenses/MIT',
      description='Cryptsy Push API Extension',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python :: 2.7",
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English"
        ],
      keywords='',
      packages=('cryptsy_ext', 'pusherclient', 'thredis'),
      # scripts=(''),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="tests",
      )