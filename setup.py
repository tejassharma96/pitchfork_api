import setuptools


with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pitchfork_api',
    version='0.0.5',
    author='Tejas Sharma',
    author_email='tejas.s1996@gmail.com',
    packages=setuptools.find_packages(),
    scripts=[],
    url='https://github.com/tejassharma96/pitchfork_api/',
    license='LICENSE.txt',
    description='Unofficial API for pitchfork.com reviews, maintained version of pitchfork',
    long_description=long_description,
    install_requires=['beautifulsoup4'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
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
