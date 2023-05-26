General Pathogen Submissions Guide
===================

.. image:: images/ENA_logo_tagline.png
   :align: center

Introduction
-----------

This guide provides general information and help for submitting pathogen sequence data to the `European Nucleotide Archive <https://www.ebi.ac.uk/ena/browser/home>`_
(ENA). All public `INSDC <https://www.insdc.org/>`_ pathogen data will be made available to browse using the Pathogens Portal.

Please see below for a specific guide for submitting pathogen related data. The guide frequently refers to the
`ENA Training Modules <https://ena-docs.readthedocs.io/en/latest/index.html>`_,
our general ENA submissions guide. If you have any queries or require assistance with your submission please contact
us at ena-path-collabs@ebi.ac.uk.

.. tip::

  **Looking for something else?**
  For pathogen specific submissions guidance, please refer to these guides:

  -`ENA SARS-CoV-2 submissions guide <https://ena-covid19-docs.readthedocs.io/en/latest/index.html>`_
  -`Monkeypox virus ENA submissions Guidance <https://docs.google.com/viewer?url=https://github.com/enasequence/ena-content-dataflow/raw/master/docs/Monkeypox%20virus%20ENA%20Submission%20Guidance.pdf>`_

  For small-scale SARS-CoV-2 viral data submissions, with no prior knowledge of ENA submission routes, we have developed a
  drag and drop submissions tool. Please complete the `form <https://www.covid19dataportal.org/submit-data/viral-sequence-form>`_
  if you would like to submit your data using this route.


.. contents::
   :local:
   :depth: 3


Getting Started
~~~~~~~
Register a submission account
``````````````
Before you can submit data to the ENA you must `register a Webin submission account <https://ena-docs.readthedocs.io/en/latest/submit/general-guide/registration.html>`_.

Please navigate to the `Webin Portal <https://www.ebi.ac.uk/ena/submit/webin/login>`_ and click the ‘Register’
button and complete the registration form.


The ENA Metadata Model
``````````````
Before submitting data to ENA, it is important to familiarise yourself with the `ENA metadata model <https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html#the-ena-metadata-model>`_
and what parts of your research project can be represented by which metadata objects. This will determine what you need to submit.


.. raw:: html
   :align: center

    <embed>
        <blockquote class="twitter-tweet"><p lang="en" dir="ltr">1/8<br><br>The ENA would like to introduce you to our very first TWEETORIAL! For this <a href="https://twitter.com/hashtag/tweetorial?src=hash&amp;ref_src=twsrc%5Etfw">#tweetorial</a>, we will be explaining the ENA Metadata Model. When submitting data to the ENA, you need to register additional metadata so your submission is in accordance with FAIR data principles. <a href="https://t.co/m45ENIrlIM">pic.twitter.com/m45ENIrlIM</a></p>&mdash; European Nucleotide Archive (ENA) (@ENASequence) <a href="https://twitter.com/ENASequence/status/1514229572425994245?ref_src=twsrc%5Etfw">April 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </embed>


ENA Submission routes
``````````````
ENA allows submissions via three routes, each of which is appropriate for a
different set of submission types. You may be required to use more than one in
the process of submitting your data:

- **Interactive Submissions** are completed by filling out web forms directly
  in your browser and downloading template spreadsheets that can be completed
  off-line and uploaded to ENA. This is often the most accessible submission route.
- **Command Line Submissions** use our bespoke Webin-CLI program. This
  validates your submissions entirely before you complete them, allowing you
  maximum control of the process.
- **Programmatic Submissions** are completed by preparing your submissions as
  XML documents and either sending them to ENA using a program such as cURL or using
  the Webin Portal.

The table below outlines what can be submitted through each submission route.

+------------------------+-------------+-----------+--------------+
|                        | Interactive | Webin-CLI | Programmatic |
+------------------------+-------------+-----------+--------------+
| Study                  |    **Y**    |     N     |     **Y**    |
+------------------------+-------------+-----------+--------------+
| Sample                 |    **Y**    |     N     |     **Y**    |
+------------------------+-------------+-----------+--------------+
| Read data              |    **Y**    |   **Y**   |     **Y**    |
+------------------------+-------------+-----------+--------------+
| Genome Assembly        |      N      |   **Y**   |       N      |
+------------------------+-------------+-----------+--------------+
| Transcriptome Assembly |      N      |   **Y**   |       N      |
+------------------------+-------------+-----------+--------------+
| Template Sequence      |      N      |   **Y**   |       N      |
+------------------------+-------------+-----------+--------------+
| Other Analyses         |      N      |     N     |     **Y**    |
+------------------------+-------------+-----------+--------------+

Register Metadata
~~~~~~

Register Study
``````````````

Data submissions to the ENA require that you register a study to contextualise and group your data. Details of how to do
this can be found in our `Study Registration Guide <https://ena-docs.readthedocs.io/en/latest/submit/study.html>`_.
Please ensure you describe your study adequately, as well as provide an informative title.

Your  studies can now be claimed using your ORCID ID and/or assigned a DOI. Please see `here <https://ena-browser-docs.readthedocs.io/en/latest/about/citing-ena.html#orcid-data-claiming>`_
and `here <https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html#doi-issuing>`_ for more information on these options.

Register Samples
``````````````

Having registered a study, please proceed to register your samples. These are metadata objects that describe the source
biological material of your experiments. Following this, the sequence data can be registered (as described in later sections).

Instructions for sample registration can be found in our `Sample Registration Guide <https://ena-docs.readthedocs.io/en/latest/submit/samples.html>`_.
As part of this process, you must select a sample checklist to describe metadata.
If you require any support regarding sample metadata, please contact ena-path-collabs@ebi.ac.uk.

for **interactive submission**, download the sample checklist template from the Webin Portal and once completed, submit
the checklist in **.tsv** format on the Webin Portal to register your Samples. See `programmatic sample submission <https://ena-docs.readthedocs.io/en/latest/submit/samples/programmatic.html#register-samples-programmatically>`_
if you are submitting samples programmatically.

Sample checklists
'''''''''''''''''
The following Sample checklists contain  **mandatory**, *recommended* and optional metadata fields (``<SAMPLE_ATTRIBUTE>``),
with a description for each field, to help with sample metadata completion.
The checklists were agreed by the Genomic Standards Consortium (GSC). In addition to the core checklist for each life domain,
the GSC also provides checklist extensions which may have the metadata field you are looking for.

You can use the `Sample checklists portal <https://www.ebi.ac.uk/ena/browser/checklists>`_ to browse all ENA checklists.
The pathogen specific checklists are provided below.

+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| **link**                                                        | **Checklist name**                                                        |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| `ERC000028 <https://www.ebi.ac.uk/ena/browser/view/ERC000028>`_ | ENA prokaryotic pathogen minimal sample checklist                         |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| `ERC000029 <https://www.ebi.ac.uk/ena/browser/view/ERC000029>`_ | ENA Global Microbial Identifier reporting standard checklist GMI_MDM:1.1  |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| `ERC000032 <https://www.ebi.ac.uk/ena/browser/view/ERC000032>`_ | ENA Influenza virus reporting standard checklist                          |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| `ERC000033 <https://www.ebi.ac.uk/ena/browser/view/ERC000033>`_ | ENA virus pathogen reporting standard checklist                           |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| `ERC000039 <https://www.ebi.ac.uk/ena/browser/view/ERC000039>`_ | ENA parasite sample checklist                                             |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| `ERC000041 <https://www.ebi.ac.uk/ena/browser/view/ERC000041>`_ | ENA Global Microbial Identifier Proficiency Test (GMI PT) checklist       |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+

Sample Taxonomy
'''''''''''''''''

Sample host field
''''''''''''''''''
subheading 1
````````

subheading 2
........

subheading 3
***********

subheading 4
+++++++

subheading 5
^^^^^^^^^


Submit raw read data
~~~~~~

add information here

Submit sequence or assembly data
~~~~~~


submit targeted sequences
``````````````

submit pathogen assemblies
``````````````

Viral assembly submission
'''''''''''''''''
``webin-cli command here``




bacterial assembly submission
'''''''''''''''''
``webin-cli command here``

::

   version: 2

   python:
     install:
       - requirements: docs/requirements.txt
       - method: pip
         path: .
         extra_requirements:
           - docs
       - method: pip
         path: another/package
     system_packages: true



eukaryotic assembly submission
'''''''''''''''''

``webin-cli command here``




heading 3
~~~~~~~~~