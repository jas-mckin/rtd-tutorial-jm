Submitting linked cohort datasets
---------------------------------

Introduction
------------
Infectious disease plays out as an intricate set of molecular interactions between the systems of both pathogen and infected host. 
In cases of vector-borne disease, such as malaria, or diseases with intermediate hosts, such as tapeworm, interactions with further 
species are involved. Studying these interconnected biologies, such as to understand infection mechanisms and patient response, 
develop clinical and public health interventions and predict outcomes of the circulation of new pathogen variants, requires the 
use of combined data sets which span the two or more organisms involved in the infection.

Regardless of which technical platform is used for their generation, biological data can be organised around the concept of 
sample. A biological sample, such as a blood sample from a patient, can be represented as a digital record with an identifier. 
When the sample is subjected to different assays, such as genomic sequencing or serology analysis, each of the resultant data 
sets can reference the identifier of the sample from which they were derived. In many workflows, samples are divided, such as 
when a wastewater sample is size-filtered to yield a bacterial subsample and a viral subsample. Records for each of these new 
samples can be created and given their own identifiers, and reference can be made back to the sample from which they were derived 
by using its sample identifier.

test mermaid diagram:

.. mermaid::

   flowchart TD
      A[Christmas] -->|Get money| B(Go shopping)
      B --> C{Let me think}
      C -->|One| D[Laptop]
      C -->|Two| E[iPhone]
      C -->|Three| F[fa:fa-car Car]


.. mermaid:: path/to/mermaid-gantt-code.mmd


