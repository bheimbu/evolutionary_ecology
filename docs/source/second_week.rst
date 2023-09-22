.. _second-week:
Second Week
===========
Goals
-----
This week it's all about DNA sequences: How to work with them, where to get them from (if you do not wish to sequence animals yourself), how to infer phylogenetic trees.

All steps for handling sequence data and phylogenetic analyses are explained step by step in online tutorials. Everyday, a tutorial is dedicated to a different method. You must finish the respective tutorial and its exercises in order to be able to continue with the next tutorial on the next day.

However, you start this week with assembling, checking, and exporting your raw sequences (= sequencing results of your PCR products from last week) to obtain good or even high quality consensus sequences.  We start with your DNA sequences so that you will get familiar with…
- Sanger DNA sequencing
- sequence evaluation (or 'What's the difference between a bad and good DNA sequence?')
- ambiguous (wobble) DNA positions and where do they come from
- DNA sequences from public data repositories

After you processed your own sequences, you can start with the :ref:`Tutorials`.

.. note::
  **At the end of the week you will know…**

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

.. _Monday_Second_Week:
Monday
------
Summary
^^^^^^^

Today we will start with recapitulating the molecular work of last week and discuss the method of Sanger Sequencing.
After that, you start with processing your sequencing results i.e., you will assemble, check and correct the raw reads that have been assigned to you (see assignment list) in :ref:`Geneious_Prime` and export the respective consensus sequences.
Then, you can start with the online tutorial, which introduces you to the handling of sequence data and how to use Genbank, a public sequence data repository.
By doing the exercises in this tutorial, you will generate a toy dataset, which you will be using for the whole week. All following tutorials and exercises are based on this toy dataset.
The basic idea is, that all of you work with the same toy dataset, which makes it easier to compare results. However, it is also fine if you add some of your own sequences (those you checked and exported earlier today).

Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""
.. important::
  1. Read the section :ref:`Geneious_Prime`
  2. Download and install the `30-days trial version of Geneious Prime <https://manage.geneious.com/free-trial>`_

Task 2
""""""

- Download `raw_sequences  <https://studip.uni-goettingen.de/dispatch.php/course/files/index/660b809717ef7407f199fdb5f7a87d89?cid=d7b80997f5efda59609a4cf69a04dbf7>`_
- Open the "assignment list”
- Check out, which raw reads have been assigned to you
- Import reads to Geneious Prime
- Remember that each gene belongs to its own folder
  - Do not import your 28S sequences into your 18S or COI folder, and *vice versa*
- Find the matching raw reads i.e., the forward and the reverse sequence of the same sample
- Assemble the matching pair of reads

.. attention::
  Remember to name consensus sequences correctly, in the following format:
  
  SampleNumber_*Genus*_*species*_Gene_`.fasta`

  for example: ``01_Acrogalumna_longisetosa_18S_IS``

- Check the consensus sequence and correct ambiguous positions
- Export the consensus sequences
- Make sure the sequence name is correct!
- Keep in mind that a consensus sequence file consists of a single sequence

.. important::
  Upload the consensus files `here <https://studip.uni-goettingen.de/dispatch.php/course/files/index/8c1eff148df88fb568fb3c5445992b96?cid=d7b80997f5efda59609a4cf69a04dbf7>`_.

Task 3
""""""

.. important::
  Please read sections: :ref:`Database_and_Search_Strategy` and :ref:`Downloading_and_Saving`

Task 4
""""""

.. important::
  Complete Tutorials:
  
  - :ref:`T1_A`
  - :ref:`T1_B`

Task 5
"""""""

.. attention::
  Do not leave before **Tasks 1-4** are completed!

.. _Tutorials:
Tutorials
^^^^^^^^^

.. _T1_A:
T1_A
"""""

Please create a folder on your USB Stick or under C:/ on your ⊞ Win hard drive with the name: **EvolEcol**. All the data from this course goes into this folder. Create a sub folder with the name **T1**, where the exercises of tutorial 1 will be saved. That is, create a new folder named **T1** and the number of the exercise separated with underscore (e.g. **T1_A1**, **T1_A2**, ... ). 

.. attention::
  Never use space or special characters (e.g., ``ä``, ``.``, ``:``) in sequence or file names; always separate words with underscores ``_``. Most sequence editors and phylogenetic programs are very sensitive when it comes to sequence names and file formats. You will save a lot of time, if your file names are compatible right from the start.

.. _T1_A1:
T1_A1
"""""

.. important::
  - Open GenBank and select the 'Nucleotide' database in your web browser of choice.
  - Bookmark the page.

.. _T1_A2:
T1_A2
"""""

.. important::
  - Download sequences from NCBI with following accession numbers (click `here <https://owncloud.gwdg.de/index.php/s/4AgQzz4MhNtuCRf>`_) as separate sequence files in FASTA format.
  - Remember to change the names of the sequences as follows: Taxon_Gen.fas
  - Read the 'Source Organism' section of the entry and enter the species' names and the major taxonomic group to which they belong (Brachypylina, Desmonomata, Enarthronota, Mixonomata, Palaeosomata, Parhyposomata) in the spreadsheet that contains the accession numbers.
  - Upload your results `here <https://owncloud.gwdg.de/index.php/s/sMMflDL2wJxGJv2>`_.

.. _T1_A3:
T1_A3
"""""

.. important::
  - Draw a phylogenetic tree of the six major groups of Oribatida.
  - Write the names of the major groups on the branches and the species' names at the tips.

  Take a picture of your drawing and upload it `here <https://owncloud.gwdg.de/index.php/s/OA626D9jAiUfDrP>`_.

.. _T1_A4:
T1_A4
"""""

.. important::
  - Download the 18S gene for all taxa from A2 from GenBank. Use the Clipboard option to save all sequences in a single file.
  - Save the file as ``T1_A4_Oribatida_18S.fas``.
  - Remember to create a new subfolder named **T1_A4** in the folder **T1**.

.. attention::
  There is no 18S sequence available for *Carabodes femoralis*, use the 18S sequence of *Carabodes subarcticus*. For *Platynothrus peltifer*, three 18S sequences are available, download the sequence with the accession number ``EF091422``.

.. tip::
  A rule of thumb: If two or more sequences are available for a species, always choose the longest sequence.

.. _T1_A5:
T1_A5
"""""

.. important::
  - What do you consider the key benefits of an online database?

  Write down your answer on a sheet of paper.

.. _T1_B:
T1_B
""""

.. _T1_B1:
T1_B1
"""""

.. important::
  - Open all sequences from exercise **T1_A2** in a single window in :re:`Bioedit` ('Import' → 'Sequence alignment file').
  - Save the pooled dataset in FASTA-format (folder: **T1_B1**, filename: e.g. ``EF_all.fas``).
  - Change all sequence names from GenBank to: genus_species_accession number_gene (e.g. ``Archegozetes_longisetosus_EF081321_EF``)
     
.. attention::
  Never use special characters and spaces to separate words, always use underscores ``_``.

.. _T1_B2:
T1_B2
"""""

.. important::
  - Open the file ``T1A4_Oribatida_18S.fas`` from **T1_A4** with your local text editor of choice (e.g. Notepad++, Editor).
  - Save the file in FASTA-format (folder: **T1_B2**, filename: ``18S_all.fas``).
  - Change sequence names from GenBank just as in **T1_B1** (genus_species_accession number_gene).
  - You now have two datasets with +/- identical taxon sampling but with two different genes.
  - Now you can add (import) some of your own sequences to the 18S file.
  - Your own sequences should be named in the same logic as the sequences from NCBI.
  - As no accession numbers are available for your new sequences, you may replace accession number with "own", to quickly identify your own sequence among the others, for example: ``05_Archegozetes_longisetosus_own_18S``


.. note::
  Do not add more than four 18S sequences, please. It is helpful to keep the dataset small, because larger datasets will require longer calculation times (i.e. longer waiting time for you) and it will be more difficult to focus on the most relevant information.

Feedback Monday
^^^^^^^^^^^^^^^
To provide feedback, please complete our questionnaire: [Questionnaire Link](https://www.example.com/questionnaire).

.. tip::
   Just in case, you can read about Geneious again in :ref:`section`.

.. _Tuesday_Second_Week:
Tuesday
------

Summary
^^^^^^^

Today, it's all about sequence alignments and their importance for analysing genetic data. In this tutorial, you do sequence alignments with your toy datasets using the software `ClustalW <http://www.clustal.org/clustal2/>`_ implemented in :ref:`Bioedit`, the sequence editor you used yesterday.
It is important to remember that sequence files, whether aligned or not, can be saved in different file formats. Input file formats can change between used software. If the format is not correct, the software isn't do anything for you. Knowing what the input file format should look like will help you overcome the initial hurdles when using phylogenetic software.

.. note::
  **At the end of the day, you know…**

  - how an alignment is generated by the Needleman-Wunsch algorithm
  - how computer algorithms (basically) perform
  - the meaning of penalty values and their effects on alignments
  - how to find criteria that will help you to decide if an alignment is good or not
  - the difference between sequence file formats, and the difference between multifasta and alignment files and how to recognize them

.. important::
  **Additionally, you need to know…**

  - the consequences of using coding versus non-coding sequences for an alignment
  - the meaning and use of reading frames when aligning your data

The different properties of coding and non-coding sequences will not be explained explicitly and we assume that you already know what reading frames are. However, if you are lost, do not hesitate to ask one of the tutors or me.

.. tip::
  Start a discussion in the Forum and/or write a Wiki-entry, explaining these issues to everyone.


Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""

.. important::
      Read the section about 'Alignment'.


Task 2
""""""

.. important::
  - Complete exercise :ref:`T2_A`
  - Work with your toy datasets (18S and EF) from yesterday, do alignments with different penalty values.
  - Eventually, you must decide which of the alignments of 18S and EF is best.
  - The best alignments will be used in downstream analyzes over the next few days.


Task 3
""""""

.. important::
  - Complete exercise :ref:`T2_B`
  - Download the `.zip file <https://owncloud.gwdg.de/index.php/s/goYd3He8SyxE122>`_ that includes four example datasets without file-format assignments (no file extensions, like `.fasta` or `.txt`) and answer the questions under :ref:`T2_B`.

Task 4
""""""

.. important::
  - Complete exercise :ref:`T2_C`

Task 5
""""""

.. important::
  Do not leave before Tasks **1-4** are completed!
  
.. _T2_A1:
T2_A1
"""""

.. important::
  Create the folder **T2**, in which you safe all results of this tutorial.

  - Use your DNA datasets from exercises :ref:`T1_B1` and :ref:`T1_B2` to generate alignments in BioEdit using the following parameters (see below)

.. image:: /_static/T2_A_1.png

.. attention::
  Use a period (`.`), not a comma (`,`) when typing the penalty values!

.. important::
  Save the alignments as `.fas` file to the folder **T2_A1** with the name `Gen_T2A1a/b/c/d/e/f_aln.fas`.

.. image:: /_static/T2_A_2.png

.. _T2_A2:
T2_A2
"""""

.. important::
  - Download the `worksheet <https://owncloud.gwdg.de/index.php/s/1358UqllF4nUYlD>`_ and complete the tasks described therein. Compare your results with your neighbour.
  - Upload your results `here <https://owncloud.gwdg.de/index.php/s/CBj2Eoqz5G4mGIa>`_.

.. _T2_B:
T2_B
""""

.. important::
  - Read section :ref:`Sequence_Editing`
  - Download the `.zip file <https://owncloud.gwdg.de/index.php/s/goYd3He8SyxE122>`_
  - Open each file in your local text editor of choice (i.e. Editor or Notepad++ for Windows) and answer the questions given `here <https://owncloud.gwdg.de/index.php/s/yPMW5k0jTv8TltC>`_ 


