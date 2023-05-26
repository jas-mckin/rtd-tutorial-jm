General Pathogen Submissions Guide
===================

Introduction
-----------

This guide provides general information and help for submitting pathogen sequence data to the ENA (European Nucleotide Archive).
All public `INSDC <https://www.insdc.org/>`_ pathogen data will be made available to browse using the Pathogens Portal.

Please see below for a specific guide for submitting pathogen related data. The guide frequently refers to the
`ENA Training Modules <https://ena-docs.readthedocs.io/en/latest/index.html>`_,
our general ENA submissions guide. If you have any queries or require assistance with your submission please contact
us at: ena-path-collabs@ebi.ac.uk.

Looking for something else? For pathogen-specific submissions guidance, please refer to these guides instead:

`ENA SARS-CoV-2 submissions guide <https://ena-covid19-docs.readthedocs.io/en/latest/index.html>`_
`Monkeypox virus ENA submissions Guidance <https://docs.google.com/viewer?url=https://github.com/enasequence/ena-content-dataflow/raw/master/docs/Monkeypox%20virus%20ENA%20Submission%20Guidance.pdf>`_

For small scale SARS-CoV-2 viral data submissions, with no prior knowledge of ENA submission routes, we have developed a
drag and drop submissions tool. Please complete the form if you would like to submit your data using this route:
`COVID-19 Drag and drop viral submissions tool <https://www.covid19dataportal.org/submit-data/viral-sequence-form>`_

Guide contents
------

.. contents::
   :local:
   :depth: 3
   
Getting Started
~~~~~~~
Register a submission account
``````````````
Before you can submit data to ENA you must register a Webin submission account.

Please navigate to the `Webin Portal <https://www.ebi.ac.uk/ena/submit/webin/login>`_ and click the ‘Register’
button and complete the registration form.


The ENA Metadata Model
``````````````
Before submitting data to ENA, it is important to familiarise yourself with the `ENA metadata model <https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html#the-ena-metadata-model>`_
and what parts of your research project can be represented by which metadata objects. This will determine what you need to submit.


.. raw:: html

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
  the `Webin Portal <general-guide/submissions-portal.html>`_.

The table below outlines what can be submitted through each submission route.
It is also recommended that you familiarise yourself with our `metadata model
<general-guide/metadata.html>`_.

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

Register Metadata - Study and Sample
~~~~~~

Register Study and Samples
``````````````

Data submissions to the ENA require that you register a study to contextualise and group your data. Details of how to do
this can be found in our `Study Registration Guide <https://ena-docs.readthedocs.io/en/latest/submit/study.html>`_.
Please ensure you describe your study adequately, as well as provide an informative title.

Your ENA SARS-CoV-2 studies can now be claimed using your ORCID ID and/or assigned a DOI. Please see `here <https://ena-browser-docs.readthedocs.io/en/latest/about/citing-ena.html#orcid-data-claiming>`_
and `here <https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html#doi-issuing>`_ for more information on these options.

Having registered a study, please proceed to register your samples. These are metadata objects that describe the source
biological material of your experiments. Following this, the sequence data can be registered (as described in later sections).

Instructions for sample registration can be found in our `Sample Registration Guide <https://ena-docs.readthedocs.io/en/latest/submit/samples.html>`_.
As part of this process, you must select a sample checklist to describe metadata.
If you require any support regarding sample metadata, please contact ena-path-collabs@ebi.ac.uk.

Pathogen Sample checklists and metadata
``````````````
for **interactive submission**, download the sample checklist template from the Webin Portal and once completed, submit
the checklist in tsv format on the Webin Portal to register you Samples. See `programmatic sample submission <https://ena-docs.readthedocs.io/en/latest/submit/samples/programmatic.html#register-samples-programmatically> `_
if you are submitting samples programmatically.

Sample checklists
'''''''''''''''''

You can use the `Sample checklists portal <https://www.ebi.ac.uk/ena/browser/checklists>`_ to browse ENA checklists.
Click on any checklist to browse **mandatory**, *recommended* and optional metadata fields (aka attirbutes).
The pathogen-specific checklists are linked below:

+--------------------------------------------------------------------------+------------------------------------------------------------------+
| **Checklist name**                                                       | **link**                                                         |
+--------------------------------------------------------------------------+------------------------------------------------------------------+
| | ENA prokaryotic pathogen minimal sample checklist                      | `ERC000028 <https://www.ebi.ac.uk/ena/browser/view/ERC000028>`_  |
+--------------------------------------------------------------------------+------------------------------------------------------------------+
| ENA Global Microbial Identifier reporting standard checklist GMI_MDM:1.1 | `ERC000029 <https://www.ebi.ac.uk/ena/browser/view/ERC000029>`_  |
+--------------------------------------------------------------------------+------------------------------------------------------------------+
| | ENA Influenza virus reporting standard checklist                       | `ERC000032 <https://www.ebi.ac.uk/ena/browser/view/ERC000032>`_  |
+--------------------------------------------------------------------------+------------------------------------------------------------------+
| | ENA virus pathogen reporting standard checklist                        | `ERC000033 <https://www.ebi.ac.uk/ena/browser/view/ERC000033>`_  |
+--------------------------------------------------------------------------+------------------------------------------------------------------+
| ENA parasite sample checklist                                            | `ERC000039 <https://www.ebi.ac.uk/ena/browser/view/ERC000039>`_  |
+--------------------------------------------------------------------------+------------------------------------------------------------------+
| ENA Global Microbial Identifier Proficiency Test (GMI PT) checklist      | `ERC000041 <https://www.ebi.ac.uk/ena/browser/view/ERC000041>`_  |
+--------------------------------------------------------------------------+------------------------------------------------------------------+

Pathogen host field guidance
'''''''''''''''''


Submit raw read data
~~~~~~

Submit sequence or assembly data
~~~~~~

submit targeted sequences
``````````````

submit pathogen assemblies
``````````````

Viral assembly submission
'''''''''''''''''

bacterial assembly submission
'''''''''''''''''


eukaryotic assembly submission
'''''''''''''''''

heading 3
~~~~~~