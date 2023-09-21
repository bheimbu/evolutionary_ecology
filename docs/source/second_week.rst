.. _second-week:
Second Week
===========
Goals
-----
This week it's all about DNA sequence: How to work with them, where to get them from (if you do not wish to sequence animals yourself), how to infer phylogenetic trees.

All steps for handling sequence data and phylogenetic analyses are explained step by step in online tutorials. Everyday, a tutorial is dedicated to a different method. You must finish the respective tutorial and its exercises in order to be able to continue with the next tutorial on the next day.

.. note::
   However, you start this week with assembling, checking, and exporting your raw sequences (= sequencing results of your PCR products from last week) to obtain good or even high quality consensus sequences.  We start with your DNA sequences so that you will get familiar with…
  - Sanger DNA sequencing
  - sequence evaluation (or 'What's the difference between a bad and good DNA sequence?')
  - ambiguous (wobble) DNA positions and where do they come from
  - DNA sequences from public data repositories

 After you processed your own sequences, you can start with the online tutorial.

 .. note::
  At the end of the week you will know…
  - what a sequence file is
  - what a fasta file is
  - how to use public gene databases
  - how to edit sequences
  - how to check if your own sequencing results are correct
  - what  an multiple sequence alignment is
  - how to distinguish multifasta files from alignment files
  - what a model of sequence evolution is and why they are important for phylogenetic analyses
  - what the difference of Cluster methods and search algorithms is when constructing phylogenetic trees
  - what ML and BI means
  - how to do basic phylogenetics in R

Monday
------
Summary
^^^^^^^
Today we will start with recapitulating the molecular work of last week and discuss the method of Sanger Sequencing.
After that, you start with processing your sequencing results i.e., you will assemble, check and correct the raw reads that have been assigned to you (see assignment list) in Geneious Prime and export the respective consensus sequences.
Then, you can start with the online tutorial, which introduces you to the handling of sequence data and how to use Genbank, a public sequence data repository.
By doing the exercises in this tutorial, you will generate a toy dataset, which you will be using for the whole week. All following tutorials and exercises are based on this toy dataset.
The basic idea is, that all of you work with the same toy dataset, which makes it easier to compare results. However, it is also fine if you add some of your own sequences (those you checked and exported earlier today).

Tasks of the Day
^^^^^^^^^^^^^^^^
Task 1
""""""
.. note::
  1. Read the section :ref:`Geneious_Prime`
  2. Download and install the `30-days trial version of Geneious Prime <https://manage.geneious.com/free-trial>`_

Task 2
""""""

- Navigate to `raw_sequences  <https://studip.uni-goettingen.de/dispatch.php/course/files/index/660b809717ef7407f199fdb5f7a87d89?cid=d7b80997f5efda59609a4cf69a04dbf7>`_ and download the folder
- Open the excel file “assignment list”
- Check out, which raw reads have been assigned to you
- Import raw reads to Geneious Prime
- Remember that each gene belongs to its own folder
  - Do not import your 28S sequences into your 18S or COI folder, and vice versa
- Find the matching raw reads i.e., the forward and the reverse sequence of the same sample
- Assemble the matching pair of raw reads

.. attention::
  Remember to name the consensus sequence correctly:
  
  - Running sample number (e.g. 01, 02, ... 09, 10, 11 ...)
  - Genus and species name (e.g. 01_Acrogalumna_longisetosa)
  - Gene of interest (e.g. 01_Acrogalumna_longisetosa_18S)
  - Your initials (e.g. 01_Acrogalumna_longisetosa_18S_IS)
  - Do not forget to use underscores _ to separate words

- Check the consensus sequence and correct ambiguous positions
- Export the consensus sequences
- Make sure the sequence name is correct!
- Keep in mind that a consensus sequence file consists of a single sequence

.. note::
  Upload the consensus files `here <https://studip.uni-goettingen.de/dispatch.php/course/files/index/8c1eff148df88fb568fb3c5445992b96?cid=d7b80997f5efda59609a4cf69a04dbf7>`_.

Task 3
""""""

.. note::
  Please read sections: :ref:`Database_and_Search_Strategy` and :ref:`Downloading_and_Saving`

Task 4
""""""

.. note::
  Complete exercises:
  
  - :ref:`T1A`
  - :ref:`T1B`

Task 5
"""""""

.. attention::
  Do not leave before **Tasks 1-4** are completed!

.. _Exercises:
Exercises
^^^^^^^^^

.. _T1A:
T1A
"""

Please create a folder on your USB Stick or under C:/ on your ⊞ Win hard drive with the name: EvolEcol. All the data from this course goes into this folder. Create a sub folder with the name T1, where the exercises of tutorial 1 will be saved. That is, create a new folder named T1 and the number of the exercise separated with underscore (e.g. T1_A2, T1_A3, ...). 

.. attention::
  Never use white space or special characters (e.g., ä, ö, ü, ß, ., :, ; ...) for sequence or file names; always separate words with underscores ( _ ). Most sequence editors and phylogenetic programs are very sensitive when it comes to sequence names and file formats. You will save a lot of time, if your file names are compatible right from the start.

**T1_A1**​​​

- Open GenBank and select the 'Nucleotide' database in your web browser of choice. Bookmark the page.

**T1_A2**

- Download sequences from NCBI with the following accession numbers as separate sequence files in FASTA format. Remember to change the names of the sequences as follows: Taxon_Gen.fas
- Read the 'Source Organism' section of the entry and write down the species' names and the major taxonomic group to which they belong (Brachypylina, Desmonomata, Enarthronota, Mixonomata, Palaeosomata, Parhyposomata) in the table next to the respective accession number.

.. note::
  You can download the file on DoIT! Once you have edited the docx file, upload the finished document.

**T1_A3**

- Oribatid mites are divided into six major groups. Draw a phylogenetic tree of the six major groups. Write the name of the major group on the branch and the species' names at the tip.

.. note::
  → Take a picture of your drawing and upload it on DoIT.

**T1_A4**

- Download the 18S gene for all taxa from A2 from GenBank. Use the Clipboard option to save all sequences in a single file. Save the file as T1_A4_Oribatida_18S.fas. Remember to create a new subfolder named T1_A4 in the folder T1.

.. attention::
  There is no 18S sequence available for Carabodes femoralis, use the 18S sequence of Carabodes subarcticus. For Platynothrus peltifer, three 18S sequences are available, download the sequence with the accession number .. code-block::
                                                   EF091422
  .

.. tip::
  In general: If two or more sequences are available for a species, always choose the longest sequence.
