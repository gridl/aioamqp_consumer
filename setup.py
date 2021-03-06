import io
import os
import re

from setuptools import setup


def get_version():
    regex = r"__version__\s=\s\'(?P<version>[\d\.]+?)\'"

    path = ('aioamqp_consumer', '__init__.py')

    return re.search(regex, read(*path)).group('version')


def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


setup(
    name='aioamqp_consumer',
    version=get_version(),
    author='wikibusiness',
    author_email='osf@wikibusiness.org',
    url='https://github.com/wikibusiness/aioamqp_consumer',
    description='Consumer/producer like library built over amqp (aioamqp)',
    long_description=read('README.rst'),
    python_requires='>=3.5.0',
    install_requires=[
        'aioamqp>=0.10.0',
        'async_timeout>=1.3.0',
    ],
    packages=['aioamqp_consumer'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['aioamqp', 'amqp', 'asyncio', 'consumer', 'producer'],
)
