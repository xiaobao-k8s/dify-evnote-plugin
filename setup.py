import os
from setuptools import setup, find_packages


# Load version number from Thrift-Compiler-generated .py file
constants_path = os.path.join(os.path.dirname(__file__), "tools","lib", "evernote",
                              "edam", "userstore", "constants.py")

with open(constants_path) as constants_file:
    constants = constants_file.read().split("\n")
    for x in [x for x in constants if x.startswith('EDAM_VERSION')]:
        exec(x)


def read_from_same_directory(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as open_file:
        content = open_file.read()
    return content


setup(
    name='evernote3',
    version="{major}.{minor}.0".format(major=EDAM_VERSION_MAJOR,
                                       minor=EDAM_VERSION_MINOR),
    author='Evernote Mgr',
    description='Evernote Mgr',
    #long_description=read_from_same_directory('README.md'),
    packages=find_packages('tools/lib'),
    package_dir={'': 'tools/lib'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'
    ],
    license='BSD',
    install_requires=[
        'oauthlib',
        'requests_oauthlib'
    ],
)
