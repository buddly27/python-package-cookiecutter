###########################
Python Package Cookiecutter
###########################

Cookiecutter_ template for Python projects.

*************
Documentation
*************

* Repository https://github.com/buddly27/python-package-cookiecutter.git

Features
========

* Command line interface using click_ if required.
* Testing setup using pytest_ and `python setup.py test`
* Documentation using Sphinx_ and the ReadTheDocs_ template.
* Release notes using Lowdown_.
* Update Tag with `Semantic Versioning`_ using Versup_.

Quickstart
==========

* Ensure you have Cookiecutter_ installed::

    > pip install cookiecutter
    > cookiecutter -h

* Then generate a new project in the current directory using this template::

    > cookiecutter git@github.com:buddly27/python-package-cookiecutter.git

* Switch to the created directory and initialise as a Git_ repository::

    > git init

* Create project on https://github.com/ under chosen *group* and push to it.

Contribute
==========

Not quite what you need? Feel free to create merge requests for changes or fork
for your own needs.

.. _Cookiecutter: http://cookiecutter.readthedocs.io
.. _Sphinx: http://sphinx-doc.org/
.. _Lowdown: http://lowdown.rtd.ftrack.com/en/stable/
.. _ReadTheDocs: https://readthedocs.org/
.. _pytest: http://pytest.org
.. _Git: https://git-scm.com/
.. _Virtualenv: https://virtualenv.pypa.io
.. _Versup: https://versup.readthedocs.io/en/latest/
.. _Semantic Versioning: https://semver.org/
.. _click: https://click.palletsprojects.com/en/7.x/
