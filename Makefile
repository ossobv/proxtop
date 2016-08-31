.PHONY: default dist install isclean

DATAFILES = LICENSE.txt README.rst
PYFILES = proxtop

default:

dist: isclean $(PYFILES) $(DATAFILES)
	python setup.py sdist
	##python setup.py register # only needed once
	#python setup.py sdist upload
	# clean up
	$(RM) MANIFEST

install:
	python setup.py install

isclean:
	# Check that there are no leftover unversioned python files.
	# If there are, you should clean it up.
	# (We check this, because the setup.py will include every .py it finds
	# due to its find_package_module() function.)
	! (git status | sed -e '1,/^# Untracked/d;/^#\t.*\.py$$/!d;s/^#\t/Untracked: /' | grep .)
