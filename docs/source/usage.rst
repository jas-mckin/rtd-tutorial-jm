Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

+--------------------------------------------------------------------------+--------------+
| **Checklist**                                                            | **link**     |
+--------------------------------------------------------------------------+--------------+
| | ENA prokaryotic pathogen minimal sample checklist                      | ERC000028    |
+--------------------------------------------------------------------------+--------------+
| ENA Global Microbial Identifier reporting standard checklist GMI_MDM:1.1 | ERC000029    |
+--------------------------------------------------------------------------+--------------+
| | ENA Influenza virus reporting standard checklist                       | ERC000032    |
+--------------------------------------------------------------------------+--------------+
| | ENA virus pathogen reporting standard checklist                        | ERC000033    |
+--------------------------------------------------------------------------+--------------+
| ENA parasite sample checklist                                            | ERC000039    |
+--------------------------------------------------------------------------+--------------+
| ENA Global Microbial Identifier Proficiency Test (GMI PT) checklist      | ERC000041    |
+--------------------------------------------------------------------------+--------------+



Tweetorial

.. raw:: html

    <embed>
        <blockquote class="twitter-tweet"><p lang="en" dir="ltr">1/8<br><br>The ENA would like to introduce you to our very first TWEETORIAL! For this <a href="https://twitter.com/hashtag/tweetorial?src=hash&amp;ref_src=twsrc%5Etfw">#tweetorial</a>, we will be explaining the ENA Metadata Model. When submitting data to the ENA, you need to register additional metadata so your submission is in accordance with FAIR data principles. <a href="https://t.co/m45ENIrlIM">pic.twitter.com/m45ENIrlIM</a></p>&mdash; European Nucleotide Archive (ENA) (@ENASequence) <a href="https://twitter.com/ENASequence/status/1514229572425994245?ref_src=twsrc%5Etfw">April 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </embed>



test tabs

.. tabs::

   .. tab:: Sphinx

      .. code:: yaml

         # .readthedocs.yaml
         # Read the Docs configuration file
         # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

         # Required
         version: 2

         # Set the version of Python and other tools you might need
         build:
           os: ubuntu-22.04
           tools:
             python: "3.11"
             # You can also specify other tool versions:
             # nodejs: "19"
             # rust: "1.64"
             # golang: "1.19"

         # Build documentation in the docs/ directory with Sphinx
         sphinx:
            configuration: docs/conf.py

         # If using Sphinx, optionally build your docs in additional formats such as PDF
         # formats:
         #    - pdf

         # Optionally declare the Python requirements required to build your docs
         python:
            install:
            - requirements: docs/requirements.txt

   .. tab:: MkDocs

      .. code:: yaml

         # .readthedocs.yaml
         # Read the Docs configuration file
         # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

         # Required
         version: 2

         # Set the version of Python and other tools you might need
         build:
           os: ubuntu-22.04
           tools:
             python: "3.11"

         mkdocs:
           configuration: mkdocs.yml

         # Optionally declare the Python requirements required to build your docs
         python:
            install:
            - requirements: docs/requirements.txt