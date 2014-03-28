TODO this is currently broken!

`distutils`, `setuptools`, `distribute` information and template.

This should be repository should be installable itself.

- add bin
- add modules

You *need* the files

- `MANIFEST.txt`
- `CHANGES.txt`

Or it won't work!

#Gemfile equivalent

To allow users who have downloaded the source to develop it, use a `requirements.txt` by selecting required output lines from:

    pip freeze

And tell users to install with:

    sudo pip install -r requirements.txt

#Which tool to use to distribute?

Python distribution is currently messy.

See:

- <http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2>
- <http://python-notes.boredomandlaziness.org/en/latest/pep_ideas/core_packaging_api.html>

Current best course of action for python only projects:

- use the non-stdlib `distribute` module to create packages.

	Note that the `distribute` base module is called `setuptools` because `distribute` is a fork of `setuptools`.

- host the packages on pypi: <https://pypi.python.org/pypi>

- end users can now use `pip` to install packages from PyPi very easily.

The best you can do with the stdlib is `distutils`, but this is worse than `distribute`.

#Distutils

The setup function will parse command line arguments which allow you to do tons of things from the command line.

##setup.cfg

You can set default options for the commands via the `setup.cfg` script

Example: `bdist_rpm` is a subcommand, that is you call it as:

	python setup.py bdist_rpm

`release`, `packager` and `doc_files` are options:

	python setup.py bdist_rpm --release r --packager p --doc_files a b c
	python setup.py bdist_rpm --help

To set all the values add the following to `setup.cfg`:

	[bdist_rpm]
	release = 1
	packager = Greg Ward <gward@python.net>
	doc_files = CHANGES.txt
				README.txt
				USAGE.txt
				doc/
				examples/

##Install and uninstall

Basic install:

	sudo python setup.py install

This:

- moves files to the correct install location
- overwrites any existing files updating them.
- creates a build dir in current dir which you should ignore in your gitignore

	It puts everythin in the right place inside this build dir:

	- python files are copyied
	- C/C++ extension `.o` and `.so` are put in there

**however** there is no automatic way to uninstall!!.... <http://stackoverflow.com/questions/402359/how-do-you-uninstall-a-python-package-that-was-installed-using-distutils>

You should use a package manger like `pip` for that TODO how:

The best you can currently do without a package manger is:

	sudo python setup.py install --record record.txt

So that `record.txt` will contain the installed files, so to uninstall you can:

	cat record.txt | xargs sudo rm -rf

Clearly a hack =)

##sdist

Create a source distribution: pack all the source code into a compressed file to give to someone else for them to build

	python setup.py sdist

Not very useful since people should just use `git` or `hg`...

`MANIFST.in` files will also be included

##build_ext

Only build c/c++ [extensions](http://docs.python.org/2/extending/):

###inplace

This will place the compiled C/C++ outputs side by side with the python code in the repo, exactly where they need to be, without touching anything outside the repo:

	python setup.py build_ext --inplace

Great for testing projects that contain C/C++ extensions without having to install every time before a test so that you can modify the python files directly.

#Distribute specific

##bdist

Built distribution:

- c/c++ extensions will be compiled
- could create distro specific distributions like `rpm`

##upload

Uploads to PyPi!

##develop

	sudo python setup.py develop

Only installs executables in path, but keeps python modules in place so that you can edit them where they are for tests.

##test

TODO

##pkc_resource

Allows to get information about packages installed with distribute, and therefore if it was installed with pip this will work too.

Get package version:

	import pkg_resources
	pkg_resources.get_distribution("srtmerge").version

#egg

TODO what is
