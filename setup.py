#!/usr/bin/env python

from distutils.core import setup   #only for basic projects
#from setuptools import setup      #this is distutils, which is a currently
                                   #remerging fork of setuptools....

setup(
    name                = 'cirosantilli',
    version             = '0.0.1',
    author              = 'Ciro Duran Santilli',
    author_email        = 'ciro.santilli@gmail.com',
    url                 = 'https://github.com/cirosantilli/',
    license             = 'license.md', #GPL, BSD, or MIT. firefox http://www.codinghorror.com/blog/2007/04/pick-a-license-any-license.html 
    description         = 'my simple python scripts and modules',
    long_description    = open('readme.md').read(),

    ##packages

    # Whatever package (dir with ``__init__.py`` and everything under)is listed
    # here will be put in your your pythonpath: #(`/usr/local/lib/python2.7/dist-packages/` for ubuntu):

    packages = [
        'cirosantilli',
        'setup_test_dir',
    ],

    # Only Python files are copyied.

    # If you want to add data files your package, use [package data].

    # Data needed for a single package:
    package_data = {
        #'setup_test_dir': ['*.txt']
        #'setup_test_dir': ['*.dat']
    },

    ##package_dir

    # Specifies where packages will be put

    # All packages are under ``./lib/``:

        #package_dir = {'': 'lib'},

    #pac package is under ``./lib/``:

        #package_dir = {
            #'pac': 'lib'
        #},

    ##py_modules

    #specify individual modules (``.py`` or a dir with ``__init__.py``, but not all of its contents! )
    py_modules = [
        #'setup_test',
        #'setup_test_dir.setup_test2',
    ],

    ##scripts

    # Whatever is listed here will be put in your bin path (`/usr/local/bin` on current ubuntu):
    scripts = [
        #'bin/move_regex.py',
    ],

    ##data_files

    #system independent data files.

    #this data can be used across packages

    #relative paths go under `sys.prefix`, which equals `/usr/` in current Ubuntu for example.

    #basenames cannot be changed

    data_files = [
        #('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),   #files will go under `sys.prefix + bitmaps`
        #('/etc/init.d', ['init-script'])           #files will go under `/etc/init.d/`
    ],

    ##install_requires

    # Not in `distutils`, must use `distribute`

    # Whatever is listed here will be installed if not already:
    install_requires = [
        "distribute",
        "ipython",
        "Sphinx",
        #"matplotlib",  #** see note below
        #"numpy",       #**
        "numpydoc",     #used for numpy and matplotlib docs
        "pygments",
        #"scipy",
        "srtmerge",
        "sympy",        #computer algebra system
        "termcolor",    #output ansi color escape codes
        "unidecode",    #convert unicode to ascii. Ex: à -> a, 中-> zhong
        "virtualenv",
        # View what packages are installed.
        #TODO vs pip freeze. I think this looks under installation not managed by pip
        "yolk",
    ],
    #** Fails to install on Unbuntu 12.04.
)
