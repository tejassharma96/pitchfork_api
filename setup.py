try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pytchfork_api',
    version='v0.0.1',
    author='Tejas Sharma',
    author_email='tejas.s1996@gmail.com',
    packages=['pitchfork', 'tests'],
    scripts=[],
    url='http://pypi.python.org/pypi/pitchfork/',
    license='LICENSE.txt',
    description='Unofficial API for pitchfork.com reviews, maintained version of pitchfork',
    long_description=open('README').read(),
    install_requires=['beautifulsoup4'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
    ],
)
