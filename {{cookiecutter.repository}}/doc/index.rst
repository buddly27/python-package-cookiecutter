.. _main:

{{ "#" * cookiecutter.project|length }}
{{ cookiecutter.project }}
{{ "#" * cookiecutter.project|length }}

{{ cookiecutter.description }}

.. toctree::
    :maxdepth: 1

    introduction
    installing
    tutorial
    {%- if cookiecutter.command_line_interface == 'yes' %}
    command_line{% endif %}
    api_reference/index
    release/index
    glossary

******************
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
