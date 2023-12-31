.. _second-week:
Second Week
===========
Goals
-----
This week it's all about DNA sequences: How to work with them, where to get them from (if you do not wish to sequence organisms yourself), and how to infer phylogenetic trees.

All steps for handling sequence data and phylogenetic analyses are explained step by step in online tutorials. Everyday, a tutorial is dedicated to a different method. You must finish the respective tutorial and its exercises in order to be able to continue with the next one on the next day.

However, you start this week with assembling, checking, and exporting your raw sequences (sequenced PCR products from last week) to obtain good or even high quality consensus sequences.  We start with your DNA sequences so that you will get familiar with…

- Sanger DNA sequencing
- sequence evaluation (or 'What's the difference between a bad and good DNA sequence?')
- ambiguous (wobble) DNA positions and where do they come from
- DNA sequences from public data repositories

After you processed your own sequences, you can start with the :ref:`Tutorials`.

.. note::
  **At the end of the week, you will know…**

  - what a sequence file is
  - what a fasta file is
  - how to use public databases
  - how to edit sequences
  - how to check if sequencing results are correct
  - what an multiple sequence alignment is
  - how to distinguish multifasta files from alignment files
  - what a model of sequence evolution is and why it is important for phylogenetic analysis
  - what the difference of Cluster methods and search algorithms is when constructing phylogenetic trees
  - what ML and BI means
  - how to do basic phylogenetics in R

.. _Monday_Second_Week:
Monday
------
Summary
^^^^^^^

Today we will start with recapitulating the molecular work of last week and discuss the method of Sanger sequencing.
After that, you start with processing your sequencing results i.e., you will assemble, check and correct the raw reads that have been assigned to you (see sequence assignment list) in :ref:`Geneious_Prime` and export the respective consensus sequences.
Then, you can start with the online tutorial, which introduces you to the handling of sequence data and how to use Genbank, a public sequence data repository.
By doing the exercises in this tutorial, you will generate a toy dataset, which you will be using for the whole week. All following tutorials and exercises are based on this toy dataset.
The basic idea is, that all of you work with the same toy dataset, which makes it easier to compare results. However, it is also fine if you add some of your own sequences (those you checked and exported earlier today).

Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""
.. important::
  1. Read section :ref:`Geneious_Prime`
  2. Download and install the `30-days trial version of Geneious Prime <https://manage.geneious.com/free-trial>`_

Task 2
""""""

.. important::
  - Download the `raw sequences  <https://owncloud.gwdg.de/index.php/s/QSFR7r76OLJ5TsS>`_ (Download the right files!!!)
  - Open the `sequence assignment list <https://docs.google.com/spreadsheets/d/1jLPmKAFAuehtg1MWWZrVGDfeNNqv-mfPGC4dCOA2GbI/edit?usp=sharing>`_
  - Check out, which raw reads have been assigned to you
  - Import reads to Geneious Prime and watch the Geneious tutorial about `Sanger Sequencing <https://www.geneious.com/academy/getting-started/?wvideo=0htkkxq986>`_ if you haven't done so already
  - Remember that each gene belongs to its own folder (Do not import your 28S sequences into your 18S or COI folder, and *vice versa*!)
  - Find the matching raw reads i.e., the forward and the reverse sequence(s) of the same sample (Note that 18S consists of more than two sequences)
  - Assemble the matching read pairs

.. attention::
  Remember to name consensus sequences correctly, in the following format: 

  DNA sample number_Genus_Species_Gene_Initials ( ``1_Acrogalumna_longisetosa_18S_IS`` )

.. important::
  - Check the consensus sequence and correct ambiguous positions
  - Export the consensus sequences
  - Make sure the sequence name is correct
  - Keep in mind that a consensus sequence file consists of a single sequence

  - Upload the consensus files `here <https://owncloud.gwdg.de/index.php/s/seFkQ23tcEiTcA7>`_.

Task 3
""""""

.. important::
  - Read sections :ref:`Database_and_Search_Strategy` and :ref:`Downloading_and_Saving`

Task 4
""""""

.. important::
  - Complete :ref:`T1_A` and :ref:`T1_B`

Task 5
"""""""

.. attention::
  Do not leave before **Tasks 1-4** are completed!

.. _Tutorials:
Monday Tutorials
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
  - Remember to change the names of the sequences as follows: ``Taxon_Gen.fas``
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
  - Download the 18S gene for all taxa from :ref:`T1_A2` from GenBank.
  - Use the Clipboard option to save all sequences in a single file.
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
  - Write down your answer on a sheet of paper.

.. _T1_B:
T1_B
""""

.. _T1_B1:
T1_B1
"""""

.. important::
  .. tabs ::
     .. tab:: To do
        - Open all sequences from exercise :ref:`T1_A2` in a single window in Bioedit ('Import' → 'Sequence alignment file').
        - Save the pooled dataset in FASTA format (folder: **T1_B1**, filename: e.g. ``EF_all.fas``).
        - Change all sequence names from GenBank to: ``$GENUS_$SPECIES_$ACCESSION NUMBER_$GENE`` (e.g. ``Archegozetes_longisetosus_EF081321_EF``)
     .. tab:: Do you need help?
        Read section :ref:`Bioedit` for more information about using BioEdit. Please use `AliView <https://ormbunkar.se/aliview/>`_ if you're using a Mac or Linux PC.


.. attention::
  Never use special characters and spaces to separate words, always use underscores ``_``.

.. _T1_B2:
T1_B2
"""""

.. important::
  - Open the file ``T1_A4_Oribatida_18S.fas`` from :ref:`T1_A4` with your local text editor of choice (e.g. Notepad++, Editor).
  - Save the file in FASTA format (folder: **T1_B2**, filename: ``18S_all.fas`` )
  - Change sequence names from GenBank just as in **T1_B1** ( ``$GENUS_$SPECIES_$ACCESSION NUMBER_$GENE`` )
  - You now have two datasets with +/- identical taxon sampling but with two different genes
  - Now you can add (import) some of your own sequences to the 18S file
  - Your own sequences should be named in the same logic as the sequences from NCBI
  - As no accession numbers are available for your new sequences, you may replace accession number with ``own``, to quickly identify your own sequence among the others, for example: ``5_Archegozetes_longisetosus_own_18S``


.. note::
  Do not add more than four 18S sequences, please. It is helpful to keep the dataset small, because larger datasets will require longer running times (i.e. longer waiting time for you). It will also be more difficult to focus on the most relevant information.

Feedback Monday
^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1747958/Eo67R1>`_.

.. tip::
   Just in case, you can read about Geneious Prime again in :ref:`section`.

.. _Tuesday_Second_Week:
Tuesday
-------

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
  Start a discussion in Slack or write an entry to explain these issues to everyone.


Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""

.. important::
      Read section :ref:`Alignment` including the parts about :ref:`ClustalX` and :ref:`ClustalW_in_Bioedit`

Task 2
""""""

.. important::
  - Complete exercise :ref:`T2_A`
  - Work with your toy datasets (18S and EF) from yesterday and do alignments with different penalty values.
  - Eventually, you must decide which of the alignments of 18S and EF is best.
  - The best alignments will be used in downstream analyses over the next few days.


Task 3
""""""

.. important::
  - Complete exercise :ref:`T2_B`
  - Download the `.zip file <https://owncloud.gwdg.de/index.php/s/goYd3He8SyxE122>`_ that includes four example datasets without file-format assignments (no file extensions, like ``.fasta`` or ``.txt``) and answer the questions under :ref:`T2_B`.

Task 4
""""""

.. important::
  - Complete exercise :ref:`T2_C`

Task 5
""""""

.. important::
  Do not leave before Tasks **1-4** are completed!

.. _Tutorials_2:
Tuesday Tutorials
^^^^^^^^^

Create the folder **T2**, in which you safe all results of this tutorial

.. _T2_A1:
T2_A1
"""""

.. important::
  - Use your DNA datasets from exercises :ref:`T1_B1` and :ref:`T1_B2` to generate alignments in BioEdit using ClustalW (see section :ref:`ClustalW_in_Bioedit` for how to do this) using the parameters below

.. thumbnail:: /_static/T2_A_1.png

.. attention::
  Use a period (``.``), not a comma (``,``) when typing the penalty values!

.. important::
  Save the alignments as ``.fas`` file to the subfolder **T2_A1** with the name ``$Gen_T2_A1_a/_b/_c/_d/_e/_f_aln.fas``.

.. thumbnail:: /_static/T2_A_2.png

.. _T2_A2-A5:
T2_A2-A5
""""""""

.. important::
  - Download the `worksheet <https://owncloud.gwdg.de/index.php/s/1358UqllF4nUYlD>`_ and complete the tasks described therein. 
  - Compare your results with your neighbour.
  - Upload your results `here <https://owncloud.gwdg.de/index.php/s/CBj2Eoqz5G4mGIa>`_.

.. _T2_B:
T2_B
""""

.. important::
  - Read section :ref:`Sequence_Editing`.
  - Download the `.zip file <https://owncloud.gwdg.de/index.php/s/rpyJS4b4ng2BWDZ>`_.
  - Open each file in your local text editor of choice (i.e. Editor or Notepad++ for Windows) and answer the questions given `here <https://owncloud.gwdg.de/index.php/s/yPMW5k0jTv8TltC>`_.
  - Upload your answers `here <https://owncloud.gwdg.de/index.php/s/Jc8VqrpaWzpunHK>`_

.. _T2_C:
T2_C
"""""

.. important::
  1. Download the `worksheet <https://owncloud.gwdg.de/index.php/s/IfTXZ4cp03lAeLk>`_.
  2. Complete the exercises.
  3. Upload the completed worksheet `here <https://owncloud.gwdg.de/index.php/s/t4dVMcxPrN5Hwrw>`_.

Feedback Tuesday
^^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1748614/4i3E03>`_.

.. _Wednesday_Second_Week:
Wednesday
---------

Summary
^^^^^^^

Today, we have three learning modules:

1. Models of Sequence Evolution (:ref:`lectures`)
2. How to Infer Phylogenetic Trees (:ref:`lectures`)
  - Using Neighbor Joining
3. How to Draw Phylogenetic Trees
  - Introduction to FigTree (tree editing software)
  - Exercises on basic properties and attributes of phylogenetic trees

.. note::

  **At the end of the day, you will…**

  - know how phylogenetics account for evolutionary changes in your DNA sequences i.e., changes that happened in the past and are invisible to your eye.
  - understand the meaning of cluster algorithms and their limits as well as their advantages over search algorithms.
  - have inferred four phylogenetic trees with your toy dataset
  - experience how a cluster algorithm performs by calculating and drawing a UPGMA tree by hand.
  - have drawn phylogenetic trees by hand

Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""

.. important::
  - Download and install `jmodeltest2 <https://github.com/ddarriba/jmodeltest2>`_ on your PC
  - Read section :ref:`Models_of_Sequence_Evolution`
  - Complete exercises under :ref:`T3_A`


Task 2
""""""

.. important::
  - Download and install `SeaView <https://doua.prabi.fr/software/seaview>`_ on your PC
  - Read section :ref:`How_to_Infer_Phylogenetic_Trees`
  - Complete exercises under :ref:`T3_B`
  - Read section :ref:`How_To_Draw_Phylogenetic_Trees` for exercise :ref:`T3_B3`

Task 3
""""""

.. important::
  - Complete exercises under :ref:`T3_C` by hand using pen and paper


Task 4
""""""

.. attention::
  Do not leave before Tasks **1-3** are completed!

.. _Tutorials_3:
Wednesday Tutorials
^^^^^^^^^

Make a new folder named **T3** to save all results of the following exercises and within this folder create the subfolder **T3_A**.

.. _T3_A1:
T3_A1
"""""

.. important::
  - Use jModelTest to calculate the best fitting model of sequence evolution (see section :ref:`Models_of_Sequence_Evolution` for how to work with jModelTest) for both elongation factor and 18S alignments from exercise **T2_A2** (from the :ref:`Tutorials_2`).
  - Safe the results (the html log file) in the folder **T3_A**.

.. _T3_A2-A5:
T3_A2-A5
""""""""

.. important::
  - Download the docx file `here <https://owncloud.gwdg.de/index.php/s/LVvln6u9EcStj6d>`_ and answer the questions (**T3_A2-A5**)
  - Upload your results (**Please include your name or initals in the file name!**) `here <https://owncloud.gwdg.de/index.php/s/Ji9oFx2R5sWeeHQ>`_


.. _T3_B:
T3_B
"""""

For the following NJ exercises create two folders named **T3_EF** and **T3_18S**. Copy your alignment files in the respective subfolders.

.. _T3_B1:
T3_B1
"""""

.. important::
  - For both alignments from **T2_A2** calculate a NJ tree without a model of sequence evolution (`Distances Observed`) with `1000` bootstrap replicates (see section :ref:`How_to_Infer_Phylogenetic_Trees` for how to work with SeaView).
  - Save the rooted tree with bootstrap values and indicate in the file name that this tree is without (`w-o`) a model.

.. _T3_B2:
T3_B2
"""""

.. important::
  - For both alignments from **T2_A2** (from the :ref:`Tutorials_2`) calculate a NJ tree with a model of sequence evolution with `1000` bootstrap replicates
  - Use the most complex model available (`Distance HKY`)
  - Save the rooted tree with bootstrap values and indicate in the file name that this tree is with (`w`) a model

.. _T3_B3:
T3_B3
"""""

.. important::
  - Present the trees from :ref:`T3_B1` and :ref:`T3_B2` as phylograms in PowerPoint
  - Show the NJ trees of EF with and without model on one page, of 18S on another page
  - To do this, open the four trees from :ref:`T3_B1` and :ref:`T3_B2` in FigTree, display the tree with increasing node order (``STRG + U``) and export the tree as JPEG.

  - What is the effect of the model of sequence evolution on: (1) Tree topology and (2) node support?
  - What are the main differences between EF and 18S in terms of tree topology and node support?
  - Which phylogenetic tree is most satisfying in terms of topology and node support?

.. _T3_C:
T3_C
"""""

.. note::
  Do all the following exercises (**T3_C1 to T3_C5**) on a **sheet of paper**. Hand in your results at the end (**don't forget to write down your name**). We will discuss them tomorrow.

.. _T3_C1:
T3_C1
"""""

.. important::
  - Draw by hand all unrooted tree topologies that are possible for four taxa (A, B, C, D)
  - In one of the trees, use arrows to indicate where the tree might be rooted
  - How many topologies are possible for a rooted tree with four taxa (A, B, C, D)?
  - Draw all possible combinations

.. attention::
  Some topologies might be redundant.

.. _T3_C2:
T3_C2
"""""

.. important::
  - Draw the following tree: ``((((A,(B,(C,D))),E),(F,G)),H)`` 
  - Check your topology with FigTree.

.. _T3_C3:
T3_C3
"""""

.. important::
  - Why are trees with four taxa interesting to mathematicians compared to trees with two or three taxa?

.. _T3_C4:
T3_C4
"""""

.. note::
  - Phylogeography is the study of the genetic structure of species within or between geographic regions
  - If populations are geographically distant from each other, gene flow is usually reduced and both populations accumulate mutations independently, which increases genetic distance between taxa
  - If gene flow continues between geographically distant populations, or if they share a common ancestor from which they recently separated, their genetic distance is comparatively small

.. important::
  In the course of a Master's thesis, a student investigates the relationships of two populations of the oribatid mite `Steganacarus magnus` (SM) from Germany (D) and France (F). To understand the relationships between the two populations, the student sequenced the COI mitochondrial gene of seven individuals and generated a matrix that shows the genetic distances between all individuals (**see distance matrix below**).

  **With a phylogenetic tree, relationships between individuals can be analyzed. To infer if the two populations have a recent common ancestor, draw a UPMGA tree and calculate the length of all tree branches.**

  - Hand in the tree (**on paper, don't forget to write down your name**) with all distance calculations and intermediate distance matrixes.
  - Interpret the tree in a phylogeographic context.
  - Are both populations genetically separated or are there any indications for gene flow or dispersal?

+-------+-------+-------+-------+-------+-------+-------+-------+
|       | SM_D1 | SM_D2 | SM_D3 | SM_D4 | _SM_F1| SM_F2 | SM_F3 |
+=======+=======+=======+=======+=======+=======+=======+=======+
| SM_D1 |   -   |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| SM_D2 |   5   |   -   |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| SM_D3 |   6   |   1   |   -   |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| SM_D4 |  42   |  39   |  40   |   -   |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| _SM_F1|   5   |   2   |   3   |  39   |   -   |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| SM_F2 |  67   |  68   |  71   |  70   |  68   |   -   |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| SM_F3 |  72   |  73   |  74   |  72   |  73   |   6   |   -   |
+-------+-------+-------+-------+-------+-------+-------+-------+

.. _T3_C5:
T3_C5
"""""

.. important::
  What is the difference between a cladogram, a phylogram, and a chronogram?

Feedback Wednesday
^^^^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1726580/jLKvnZ>`_.

.. tip::
  If you feel stuck, have a chat in Slack or browse it for answers. 

.. _Thursday_Second_Week:
Thursday
---------

Summary
^^^^^^^

Today, it's all about search algorithms. You will learn the basics of the two most common methods for calculating phylogenetic trees – :ref:`Maximum_Likelihood` in the morning and :ref:`Bayesian_Inference` in the afternoon.

Both methods are widely used, because they are more thorough than Cluster methods and they approach the mathematical part of inferring phylogenetic trees from different angles. You will hear more about this in the :ref:`lectures` that are accompanied with the two sections.

Today, we use two programs that can only be controlled via the command line and do not have a GUI (graphical user interface), namely :ref:`RAxML <Raxml>` (`download here <https://owncloud.gwdg.de/index.php/s/feKtzea2J1avgZw>`_) and :ref:`MrBayes <MrBayes>` (`download here <https://owncloud.gwdg.de/index.php/s/YyIcVOeqUWKxilX>`_).

While working through the exercises, many topics you have been dealing with earlier this week will come up again, such as input file format or :ref:`Models_of_Sequence_Evolution`.

.. note::
  **At the end of the day you will…**

  - know the difference between Cluster and Search algorithms
  - know why search algorithms take so much longer for analysing genetic data than Cluster algorithms
  - know that ML uses likelihoods, and MrBayes uses posterior probabilities to calculate internal nodes and topologies of trees.
  - know what an MCMC-robot is and for which type of analysis it is mandatory
  - be able to interpret the different statistics MrBayes provides
  - understand the meaning of prior and posterior analyses.
  - understand the difference between bootstraps and posterior probabilites and why they are not directly comparable.

Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""

.. important::
  - Read section :ref:`RAxML <Raxml>`
  - Download `RAxML <https://owncloud.gwdg.de/index.php/s/feKtzea2J1avgZw>`_ if you haven't done it before
  - Complete exercises :ref:`T4_A1` and :ref:`T4-A2`

Task 2
""""""

.. important::
  - Read section :ref:`MrBayes <MrBayes>`
  - Download `MrBayes <https://owncloud.gwdg.de/index.php/s/YyIcVOeqUWKxilX>`_ if you haven't done it before
  - Complete exercises :ref:`T4_B1`, :ref:`T4_B2`, :ref:`T4_B3`, and :ref:`T4_B4`

Task 3
""""""

.. important::
  - If you feel stuck when answering the questions of tutorial **T4**, ask and discuss your thoughts with the group and tutors or in Slack
  - **Tasks 1** and **2** should be finished by 03:00 pm, so that we can discuss all results of today in presence

Task 4
""""""

.. important::
  If you have some spare time because your analyses runs/worked smoothly and you answered all questions satisfactorily, you may start with reading the first sections of :ref:`Friday_Second_Week`

Task 5
""""""

.. attention::
  Do not leave before **Tasks 1-4** are completed and discussed!

.. _Tutorials_4:
Thursday Tutorials
^^^^^^^^^

.. _T4_A:
T4_A
"""""

.. important::
  - Start a new folder named **T4** and save all results from the following exercises therein
  - Copy the **18S** and **EF** alignments in a new folder named **Alignments**
  - Use :ref:`Seaview` to convert the alignment from ``.aln`` or ``.fas`` to ``.phy`` (Phylip format)

.. _T4_A1:
T4_A1
"""""

.. important::
  - Create two new folders for the RAxML analyses of **EF** and **18S**, named **T4_A1_RAxML_EF** and **T4_A1_RAxML_18S**
  - Copy the executable file of RAxML (``RAxML.exe``), the ``batch`` file and your alignments in Phylip format in the respective folders, name the batch files ``gene_RAxML_Yourname.bat``
  - Start ML analyses with `500` bootstrap replicates for your **18S** and **EF** datasets
  - Write down how long the analysis took (in seconds)

.. _T4_A2:
T4_A2
"""""

.. important::

  - When constructing phylogenetic trees, we can only approximate the true phylogenetic relationship between taxa because we only work with a random sample of taxa
  - How can we be sure that a tree is good? More than one solution is possible.

.. thumbnail:: /_static/haplotypes.png

.. _T4_B1:
T4_B1
"""""

.. important::

  - Start a MrBayes analysis for both datasets (**18S** and **EF**), see section :ref:`MrBayes` for more details
  - optional (Use a ``batch`` file for each analysis)
  - Define the outgroup and set the parameters for the best fitting model of sequence evolution
  - Run the analyses for `1 million` generations and sample every `100th` generation

  - Write down how long the analysis took (minutes + seconds)
  - Which parameter-settings deviate from the default settings?
  - What is the average standard deviation of your analyses?
  - Write down the details of the credible set of trees
  - What is the meaning of the number of trees that are included in the credible sets (search online for more information)

.. _T4_B2:
T4_B2
"""""

.. note::

  - The choice of priors (setting of parameters prior to the analysis) is important for Bayesian Inferences, as they influence the computing time and the search efficiency in the parameter landscape
  - However, as priors are usually unknown you can use flat priors

.. important:: 

  - What are flat priors and how do they look like?
  - Are they realistic?
  - How do they affect likelihoods during the search among trees?
  - How do they affect the efficiency of the search?
  - What is the meaning of „burnin“?

.. _T4_B3:
T4_B3
"""""

.. important::

  - Explain briefly -- in your own words -- why MrBayes uses Metropolis-Coupled Markov-Chain Monte Carlo

.. _T4_B4:
T4_B4
"""""

.. important::

  - Import all trees you made into PowerPoint
  - Separate the trees according to gene, ML and BI analyses, respectively
  - Save them on a DIN A4 page
  - Label the nodes with corresponding bootstrap values and posterior probabilities
  - What are the main differences between the ML and MrBayes trees?

Feedback Thursday
^^^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1749822/P4f2b7>`_.

.. _Friday_Second_Week:
Friday
------

Summary
^^^^^^^

Now you know all the essential steps and methods how to calculate a phylogenetic tree from sequence data. You may have realized that you had to use different file formats for different programs and different programs for different analyses.

You should know that you can also work with sequence data and make phylogenetic trees in R. One big advantage of using R is, that you can do all analyses in one software, without reformatting the input files. 

The other big advantage of R is, that you can do awesome downstream analyses with your phylogenetic tree, like analysing trait evolution when you have trait data for your taxa, or analyse community data. But this is another story.

This day is dedicated to introduce you into the basic commands in R that enable you to calculate a phylogenetic tree. Of course: R walks along the analytical path from sequence to tree in its very own way. However, this may even help you to better remember or even understand the single steps that are involved in building a phylogenetic tree from scratch.

Depending on your present day R skills, you may only skim through some of the sections. You will see which are relevant for you to read.

.. note::

  **At the end of the day, you will**

  - be more versatile and confident when working with genetic data.

Tasks of the Day
^^^^^^^^^^^^^^^^

Task 1
""""""

.. important::

  Read section :ref:`Ape_package`

Task 2
""""""

.. important::

  Read section :ref:`Getting_Started_with_R`

Task 3
""""""

.. important::

  - Download the R script and the example files `here <https://owncloud.gwdg.de/index.php/s/png6HlTkiN1FjO5>`_
  - Work through the script to understand how to make phylogenetic trees in R.


Task 4
""""""

.. important::

   - Use the same R script as in **Task 3**
   - Work through the script to see in which way you can also analyse genetic data in R.

Task 5
""""""

.. important::

  Run the script of Task 3 with your own toy dataset

Task 6
""""""

.. important::

  Do not leave before you finished **at least three of the five** tasks!

.. _Tutorials_5:
Friday Tutorials
^^^^^^^^^

.. _T5_A:
T5_A
"""""

.. note::

  - Copy-and-paste the multisequence FASTA files from :ref:`T1_A2` and :ref:`T1_A4` (``T1_A4_Oribatida_EF.fas`` and ``T1A4_Oribatida_18S.fas``) to a new folder named **T5_A1**. 
  - Open R or RStudio and set the folder **T5_A1** as working directory.

.. _T5_A1:
T5_A1
"""""

.. important::

  - Align the multifasta sequences ``T1_A4_Oribatida_EF.fas`` and ``T1_A4_Oribatida_18S.fas`` using the ``msa( )`` function in R
  - Use the CLUSTAL algorithm and set `10` and `0.1` as gap opening and gap penalties, respectively
  - Save the alignments as ``EF_aln1.fas`` and ``18S_aln1.fas``

  - Open the alignments in BioEdit, check and trim to the shortest sequence
  - Save the trimmed alignments as ``EF_aln2.fas`` and ``18S_aln2.fas``
  - Remember to (download and) activate the required packages
  - How long (bp) is the trimmed alignment for: **EF** and **18S**
  - How long (bp) is the best alignment from **T2**: **EF** and **18S**
  
  - If you have followed the above instructions, you disobeyed a formal alignment rule. Which one? 

.. _T5_A2:
T5_A2
"""""

.. important::

  - Calculate a Neighbor Joining tree based on p-distances for ``EF_aln2.fas`` and ``18S_aln2.fas``.
  - Save the distance matrix for each alignment as ``csv``, name it ``dEF.csv`` and ``d18S.csv``.
  - Calculate `1000` bootstraps for each tree.
  - Plot each tree nicely (``ladders right=FALSE, cex=0.7``) with bootstrap in percent and in ``lightblue`` colour in circles with ``white`` background.
  - Save the NJ trees with nodelabels as ``njEF.tre`` (with ``red`` tip labels) and ``nj18S.tre`` (with ``lightblue`` tip labels).

.. _T5_A3:
T5_A3
"""""

.. important::

  - Calculate the model of sequence evolution in R for the trimmed alignments ``EF_aln2.fas`` and ``18S_aln2.fas``.
  - What is the best fit model for: **EF** and **18S**

.. _T5_A4:
T5_A4
"""""

.. important::

  - Calculate an ML tree for ``EF_aln2.fas`` and ``18S_aln2.fas``.
  - Plot both trees in one graphic, with facing tip labels. **EF** with ``green`` and **18S** with ``yellowgreen`` tip labels.
  - Display bootstrap values in ``circles`` and in ``red`` with background in ``pink1``.
  - Save the plot as PDF, name it ``ML_EF_18S.pdf``

.. _T5_A5:
T5_A5
"""""

.. important::

  - Are the NJ and ML trees calculated in R similar to the trees calculated in Exercises of :ref:`Tutorials_3` and :ref:`Tutorials_4`?
  - Can you see fundamental differences?
  - Do you consider both ways (R and Seaview or RAxML) as comparable?

.. _T5_B:
T5_B
"""""

.. _T5_B1:
T5_B1
"""""

.. important::

  - Calculate the number of haplotypes in the dataset ``Onova_example_COI``.
  - How many sequences are in this data set and how many haplotypes?
  - Plot the haplotype list as barplot, sorted from many to few.
  - Save the barplot including a title as pdf. Name it ``Onova_hts_plot.pdf``.

.. _T5_B2:
T5_B2
"""""

.. important::

  - Calculate a haplotype network for ``Onova_example_COI.fas`` and ``Onova_example_data.csv``.
  - Save the graph as pdf, name it ``Onova_HTNW.pdf``

.. _Special_Exercise:
Special Exercise
""""""""""""""""
.. attention::
  
  - Translate the nucleotide alignment of ``EF_aln2.fasta`` into protein sequences using R.
  - Write down the script.

Feedback Friday
^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1750601/rb9hpW>`_.
