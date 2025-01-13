.. _second-week:
Second Week
===========
Major Goals
-----------
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

  - What a sequence file is.
  - What a fasta file is.
  - How to use public databases.
  - How to edit sequences.
  - How to check if sequencing results are correct.
  - What an multiple sequence alignment is.
  - How to distinguish multifasta files from alignment files.
  - What a model of sequence evolution is and why it is important for phylogenetic analysis.
  - What the difference of Cluster methods and search algorithms is when constructing phylogenetic trees.
  - What ML and BI means.

.. _Monday_Second_Week:
Monday
------
Today we will start with recapitulating the molecular work of last week and discuss the method of Sanger sequencing.
After that, you start with processing your sequencing results in Geneious Prime i.e., you will assemble, check and correct the raw reads that have been assigned to you (see sequence assignment list) and export the respective consensus sequences.
Then, you can start reading the sections about Geneious and Genbank under , which introduces you to the handling of sequence data and how to use Genbank, a public sequence data repository.
By doing the exercises in this tutorial, you will generate a toy dataset, which you will be using for the whole week. All following tutorials and exercises are based on this toy dataset.
The basic idea is, that all of you work with the same toy dataset, which makes it easier to compare results. However, it is also fine if you add some of your own sequences (those you checked and exported earlier today).

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements
               
            1. Read section :ref:`Geneious_Prime`.
            2. See the `sequence assignment list <https://docs.google.com/spreadsheets/d/1jLPmKAFAuehtg1MWWZrVGDfeNNqv-mfPGC4dCOA2GbI/edit?usp=sharing>`_.
            3. Check out, which raw reads have been assigned to you.

        .. tab:: Exercise 1

           1. Open Geneious Prime and create the folder **Monday/Tutorial_1** and subfolders for each gene

           .. code::

              Local
                ├── Monday
                │     └── Tutorial_1
                │            ├── 18S
                │            ├── 28S
                |            └── COI
                └── …
           
           2. Download and import your `raw sequences  <https://owncloud.gwdg.de/index.php/s/QSFR7r76OLJ5TsS>`_ to Geneious Prime (Download the right files!!!).

        .. tab:: Exercise 2
       
           1. Find the matching raw reads i.e., the forward and the reverse sequence(s) of the same sample (Note that 18S consists of more than two sequences).
           2. Assemble the matching read pairs.
           3. Name your consensus sequences in the following format: ``$DNA sample number_$Genus_$Species_$Gene_$Initials`` (      ``1_Acrogalumna_longisetosa_18S_IS``).
           4. Check the consensus sequence and correct ambiguous positions.
           5. Export the consensus sequences as FASTA files to **Monday/Tutorial_1** on your PC.
           6. Upload the consensus files `here <https://owncloud.gwdg.de/index.php/s/seFkQ23tcEiTcA7>`_.

           .. attention::
              Never use space or special characters (e.g., ``ä``, ``.``, ``:``) in sequence or file names; always separate words with underscores ``_``. Most sequence editors and phylogenetic programs are very sensitive when it comes to sequence names and file formats. You will save a lot of time, if your file names are compatible right from the start.

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Requirements
   
           1. Read sections :ref:`Database_and_Search_Strategy` and :ref:`Downloading_and_Saving`.

        .. tab:: Exercises

           1. Open GenBank and select the 'Nucleotide' database in your web browser of choice.
           2. Bookmark the page.

  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Requirements

           1. Download the `spreadsheet <https://owncloud.gwdg.de/index.php/s/4AgQzz4MhNtuCRf>`_.

        .. tab:: Exercises

           1. Look up the accession numbers on NCBI GenBank.
           2. See the 'Source Organism' section of the entry and enter the species' names and the major taxonomic group to which they belong (Brachypylina, Desmonomata, Enarthronota, Mixonomata, Palaeosomata, Parhyposomata) in the spreadsheet that contains the accession numbers.
           3. Upload your results `here <https://owncloud.gwdg.de/index.php/s/sMMflDL2wJxGJv2>`_.

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Exercises
    
           1. Draw a phylogenetic tree of the six major groups of Oribatida.
           2. Write the names of the major groups on the branches and the species' names at the tips.
           3. Take a picture of your drawing and upload it `here <https://owncloud.gwdg.de/index.php/s/OA626D9jAiUfDrP>`_.

  .. tab:: Tutorial 5

     .. tabs::

        .. tab:: Exercises

           1. Download the 18S rDNA gene for all taxa given in **Tutorial 3**.
           2. Use the Clipboard option to save all sequences in FASTA format as a single file (name the file ``Tutorial_5_Oribatida_18S.fas``).
           3. Import the file to **Monday/Tutorial_5** in Geneious Prime.

           .. code::

              Local
                ├── Monday
                │     ├── Tutorial_1
                │     └── Tutorial_5
                └── …


          .. attention::

              There is no 18S sequence available for *Carabodes femoralis*, use the 18S sequence of *Carabodes subarcticus*. For *Platynothrus peltifer*, three 18S sequences are available, download the sequence with the accession number ``EF091422``.

          .. hint::

              A rule of thumb: If two or more sequences are available for a species, always choose the longest sequence.

        .. tab:: Questions

           1. What do you consider the key benefits of an online database?
           2. Write down your answer on a sheet of paper.

  .. tab:: Tutorial 6

     .. tabs::

        .. tab:: Exercises

           1. Download all sequences from **Tutorial 3** and import them to Geneious Prime.

           .. code::

              Local
                ├── Monday
                │     ├── Tutorial_1
                │     ├── Tutorial_5
                │     └── Tutorial_6
                └── …

           2. Change all sequence names from GenBank to: ``$GENUS_$SPECIES_$ACCESSION NUMBER_$GENE`` (e.g. ``Archegozetes_longisetosus_EF081321_EF``)

  .. tab:: Tutorial 7

     .. tabs::

        .. tab:: Exercise 1

           1. Open the file ``Tutorial_5_Oribatida_18S.fas`` from **Tutorial 5** with your local text editor of choice (e.g. Notepad++, Editor).
           2. Change the sequence names from GenBank just as in **Tutorial 6** (``$GENUS_$SPECIES_$ACCESSION NUMBER_$GENE``).
           3. Import the file as ``18S_all`` to **Monday/Tutorial_7**

           .. code::

              Local
                ├── Monday
                │     ├── Tutorial_1
                │     ├── Tutorial_5
                │     ├── Tutorial_6
                │     └── Tutorial_7
                └── …

           .. note::
              You now have two datasets with +/- identical taxon sampling but with two different genes. Awesome!

        .. tab:: Exercise 2

           1. Now you can add (import) some of your own sequences to the 18S file.
           2. Your own sequences should be named in the same logic as the sequences from NCBI
           3. As no accession numbers are available for your new sequences, you may replace accession number with ``own``, to quickly identify your own sequence among the others, for example: ``Archegozetes_longisetosus_own_18S``
     
           .. important::
              Do not add more than four 18S sequences, please. It is helpful to keep the dataset small, because larger datasets will require longer running times (i.e. longer waiting time for you). It will also be more difficult to focus on the most relevant information.

Feedback Monday
^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1747958/Eo67R1>`_.

.. tip::
   Just in case, you can read about Geneious Prime again in :ref:`section`.

.. _Tuesday_Second_Week:
Tuesday
-------
Today, we focus on sequence alignments and their significance in analyzing genetic data. In this tutorial, you will perform sequence alignments using your toy datasets with Geneious Prime.

Remember, sequence files—whether aligned or not—can be saved in various file formats, and the required input format may vary depending on the software you use. If the format is incorrect, the software will not function as expected. Understanding the correct input file format is essential to overcoming initial challenges when working with phylogenetic software.

.. note::
  **At the end of the day, you know…**

  - How an alignment is generated by the Needleman-Wunsch algorithm.
  - How computer algorithms (basically) perform.
  - The meaning of penalty values and their effects on alignments.
  - How to find criteria that will help you to decide if an alignment is good or not.
  - The difference between sequence file formats, and the difference between multifasta and alignment files and how to recognize them.

.. important::
  The different properties of coding and non-coding sequences will not be explained explicitly and we assume that you already know what reading frames are. However, if you are lost, do not hesitate to ask one of the tutors or me.


Tasks of the Day
^^^^^^^^^^^^^^^^
.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements
               
           1. Read section :ref:`Alignment`.

           .. note::

              .. thumbnail:: /_static/T2_A_2.png

        .. tab:: Exercise

           1. Use your DNA datasets from Monday, namely **Tutorial 6** and **Tutorial 7** to generate alignments in Geneious Prime (``Align/Assemble -> Geneious Alignment``) using the parameters below (all other parameters **keep in default mode**).

           .. code::

              Local
                ├── Monday
                │     ├── …
                │     ├── Tutorial_6
                │     └── Tutorial_7
                └── Tuesday
                     └── Tutorial_1

           .. thumbnail:: /_static/T2_A_1.png

           .. attention::

               Use a period ``.`` not a comma ``,`` when typing the penalty values!

           2. Change the names of the alignments like this ``18S_Tutorial_1_a_aln`` (``$GEN_$TUTORIAL_$ALIGNMENT LETTER_aln.``).

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Requirements

           1. Download the `spreadsheet <https://owncloud.gwdg.de/index.php/s/1358UqllF4nUYlD>`_ and answer the questions.

        .. tab:: Exercises

           1. Compare your results with your neighbour.
           2. Upload your results `here <https://owncloud.gwdg.de/index.php/s/CBj2Eoqz5G4mGIa>`_ (**Do no forget to include your name or initals in the file name!**).


  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Requirements
               
           1. Read section :ref:`Sequence_Editing`.
           2. Download the `.zip folder <https://owncloud.gwdg.de/index.php/s/rpyJS4b4ng2BWDZ>`_.

        .. tab:: Exercise
     
           1. Open each file in your local text editor of choice (i.e. Editor or Notepad++ for Windows) and answer the questions given in the `spreadsheet <https://owncloud.gwdg.de/index.php/s/yPMW5k0jTv8TltC>`_.
           2. Upload your answers `here <https://owncloud.gwdg.de/index.php/s/Jc8VqrpaWzpunHK>`_ (**Do no forget to include your name or initals in the file name!**).

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Requirements

           1. Download the `spreadsheet <https://owncloud.gwdg.de/index.php/s/IfTXZ4cp03lAeLk>`_ and answer the questions.

        .. tab:: Exercise
     
           1. Upload the completed spreadsheet `here <https://owncloud.gwdg.de/index.php/s/t4dVMcxPrN5Hwrw>`_.

Feedback Tuesday
^^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1748614/4i3E03>`_.

.. _Wednesday_Second_Week:
Wednesday
---------

Today, we have three learning modules:


.. tabs::

  .. tab:: Models of Sequence Evolution

     - See :ref:`lectures`.

  .. tab:: How to Infer Phylogenetic Trees

     - See :ref:`lectures`.
     - Using Neighbor Joining.

  .. tab:: How to Draw Phylogenetic Trees
  
     - Introduction to FigTree (tree editing software).
     - Exercises on basic properties and attributes of phylogenetic trees.

.. note::

  **By the end of the day, you will:**

  - Understand how phylogenetics accounts for evolutionary changes in DNA sequences, including past changes that are not immediately visible.
  - Grasp the concept of clustering algorithms, their limitations, and their advantages over search algorithms.
  - Have constructed four phylogenetic trees using your toy dataset.
  - Experience the process of a clustering algorithm by manually calculating and drawing a UPGMA tree.
  - Have practiced drawing phylogenetic trees by hand.

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements

           1. Download and install `jmodeltest2 <https://github.com/ddarriba/jmodeltest2>`_ on your PC.
           2. Read section :ref:`Models_of_Sequence_Evolution`

        .. tab:: Exercise 1

           1. Use jModelTest to calculate the best fitting model of sequence evolution (see section :ref:`Models_of_Sequence_Evolution` for how to work with jModelTest) for both elongation factor and 18S alignments from **Tuesday/Tutorial_1**.
           2. Safe the html log file in the folder **Wednesday/Tutorial_1**.

        .. tab:: Exercise 2

           1. Download the docx file `here <https://owncloud.gwdg.de/index.php/s/LVvln6u9EcStj6d>`_ and answer the questions.
           2. Upload your results `here <https://owncloud.gwdg.de/index.php/s/Ji9oFx2R5sWeeHQ>`_ (**Do no forget to include your name or initals in the file name!**).

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`How_to_Infer_Phylogenetic_Trees`.
           2. Read section :ref:`How_To_Draw_Phylogenetic_Trees`.

        .. tab:: Exercise 1

           1. Create two subfolders named **Wednesday/Tutorial_2/EF** and **Wednesday/Tutorial_2/18S**.

           .. code::

              Local
                ├── Monday
                ├── Tuesday
                |    └── Tutorial_1
                └── Wednesday
                     └── Tutorial_2
                           ├── 18S
                           └── EF  

           2. Copy your alignment files  from **Tuesday/Tutorial_1** in the respective subfolders.
           3. For both alignments calculate a NJ tree without a model of sequence evolution (`Distances Observed`) with `1000` bootstrap replicates (see section :ref:`How_to_Infer_Phylogenetic_Trees` for how to generate a tree in Geneious Prime).
           4. Save the rooted tree with bootstrap values in **Wednesday/Tutorial_2** and indicate in the file name that this tree is without (`w-o`) a model.
       
        .. tab:: Exercise 2

           1. For both alignments calculate a NJ tree with a model of sequence evolution with `1000` bootstrap replicates
           2. Use the most complex model available (`Distance HKY`)
           3. Save the rooted trees with bootstrap values in **Wednesday/Tutorial_2** and indicate in the file name that this tree is with (`w`) a model

        .. tab:: Exercise 3

           1. Present the trees from **Exercise 1** and **Exercise 2** as phylograms in PowerPoint.
           2. Show the NJ trees of EF with and without model on one page, of 18S on another page.
           3. In order to do this, open the four trees from **Exercise 1** and **Exercise 2** in FigTree implemented in Genious Prime, display the tree with increasing node order :kbd:`Strg`+:kbd:`U` and export the tree as JPEG.

        .. tab:: Questions
           
           1. What is the effect of the model of sequence evolution on: (1) Tree topology and (2) node support?
           2. What are the main differences between EF and 18S in terms of tree topology and node support?
           3. Which phylogenetic tree is most satisfying in terms of topology and node support?

  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Requirements

           1. Complete all exercises by hand using pen and paper!
           2. Hand in your results at the end (**Don't forget to write down your name**). 
           3. We will discuss them tomorrow morning.

        .. tab:: Exercise 1

           1. Draw by hand all unrooted tree topologies that are possible for four taxa (A, B, C, D).
           2. In one of the trees, use arrows to indicate where the tree might be rooted.
           3. How many topologies are possible for a rooted tree with four taxa (A, B, C, D)?
           4. Draw all possible combinations

           .. attention::
              Some topologies might be redundant.

        .. tab:: Exercise 2
  
           1. Draw the following tree: ``((((A,(B,(C,D))),E),(F,G)),H)``.
           2. Check your topology with FigTree.
        
        .. tab:: Questions

           1. Why are trees with four taxa interesting to mathematicians compared to trees with two or three taxa?
           2. What is the difference between a cladogram, a phylogram, and a chronogram?

  .. tab:: Bonus Tutorial 4

     .. tabs::

        .. tab:: Requirements

           Phylogeography is the study of the genetic structure of species within or between geographic regions
           If populations are geographically distant from each other, gene flow is usually reduced and both populations accumulate mutations independently, which increases genetic distance between taxa
           If gene flow continues between geographically distant populations, or if they share a common ancestor from which they recently separated, their genetic distance is comparatively small

           .. note::
              In the course of a Master's thesis, a student investigates the relationships of two populations of the oribatid mite `Steganacarus magnus` (SM) from Germany (D) and France (F). To understand the relationships between the two populations, the student sequenced the COI mitochondrial gene of seven individuals and generated a matrix that shows the genetic distances between all individuals (see distance matrix under **Exercise**).

        .. tab:: Exercise

           1. To infer if the two populations have a recent common ancestor, draw a UPMGA tree and calculate the length of all tree branches.
           2. Hand in the tree (**on paper, don't forget to write down your name**) with all distance calculations and intermediate distance matrixes.
           3. Interpret the tree in a phylogeographic context.
           4. Are both populations genetically separated or are there any indications for gene flow or dispersal?

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

Feedback Wednesday
^^^^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1726580/jLKvnZ>`_.

.. tip::
  If you feel stuck, have a chat in Slack or browse it for answers. 

.. _Thursday_Second_Week:
Thursday
---------

Today, it's all about search algorithms. You will learn the basics of the two most common methods for calculating phylogenetic trees – :ref:`Maximum_Likelihood` in the morning and :ref:`Bayesian_Inference` in the afternoon.

Both methods are widely used, because they are more thorough than Cluster methods and they approach the mathematical part of inferring phylogenetic trees from different angles. You will hear more about this in the :ref:`lectures` that are accompanied with the two sections.

Today, we use two programs that can only be controlled via the command line and do not have a GUI (graphical user interface), namely :ref:`RAxML <Raxml>` (`download here <https://owncloud.gwdg.de/index.php/s/feKtzea2J1avgZw>`_) and :ref:`MrBayes <MrBayes>` (`download here <https://owncloud.gwdg.de/index.php/s/YyIcVOeqUWKxilX>`_).

While working through the exercises, many topics you have been dealing with earlier this week will come up again, such as input file format or :ref:`Models_of_Sequence_Evolution`.

.. note::
  **At the end of the day you will…**

  - Know the difference between Cluster and Search algorithms.
  - Know why search algorithms take so much longer for analysing genetic data than Cluster algorithms.
  - Know that ML uses likelihoods, and MrBayes uses posterior probabilities to calculate internal nodes and topologies of trees.
  - Know what an MCMC-robot is and for which type of analysis it is mandatory.
  - Be able to interpret the different statistics MrBayes provides.
  - Understand the meaning of prior and posterior analyses.
  - Understand the difference between bootstraps and posterior probabilites and why they are not directly comparable.

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`RAxML <Raxml>`.

        .. tab:: Exercise 1

           1. Create two new subfolders for the RAxML analyses of **EF** and **18S**, named **Thursday/Tutorial_1/EF** and **Thursday/Tutorial_1/18S**, respectively, in Geneious.
           2. Start the ML analyses with following parameters:

              - GTR GAMMA I
              - 500 bootstrap replicates
              - any other parameter in default settings

           3. Write down how long the analyses took (in seconds).

        .. tab:: Question
     
           .. note::
              When constructing phylogenetic trees, we can only approximate the true phylogenetic relationship between taxa because we only work with a random sample of taxa

           1. How can we be sure that a tree is good? More than one solution is possible!

           .. thumbnail:: /_static/haplotypes.png


  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`MrBayes <MrBayes>`.

        .. tab:: Exercise 1

           1. Create two new subfolders for the Bayesian analyses of **EF** and **18S**, named **Thursday/Tutorial_2/EF** and **Thursday/Tutorial_2/18S**, respectively, in Geneious.
           2. Define the outgroup.
           3. Set the parameters:

              - Use ``GTR+G+I`` as model of sequence evolution (see `Substitution Model:` and `Rate Variation:`)
              - 1 million generations (see `Chain Length:`) and sample every 100th generation (see `Subsampling Freq:`)

           4. Write down how long the analysis took (minutes + seconds).

        .. tab:: Questions
       
           1. Which parameter-settings deviate from the default settings?
           2. What is the average standard deviation of your analyses?
           3. Write down the details of the credible set of trees.
           4. What is the meaning of the number of trees that are included in the credible sets (search online for more information).

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Background

           .. note::
              The choice of priors (setting of parameters prior to the analysis) is important for Bayesian Inferences, as they influence the computing time and the search efficiency in the parameter landscape
              However, as priors are usually unknown you can use flat priors!

        .. tab:: Questions
 
           1. What are flat priors and how do they look like?
           2. Are they realistic?
           3. How do they affect likelihoods during the search among trees?
           4. How do they affect the efficiency of the search?
           5. What is the meaning of „burnin“?
           6. Explain briefly -- in your own words -- why MrBayes uses Metropolis-Coupled Markov-Chain Monte Carlo.

  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Exercise

           1. Import all trees you made into PowerPoint.
           2. Separate the trees according to gene, ML and BI analyses, respectively.
           3. Save them on a DIN A4 page.
           4. Label the nodes with corresponding bootstrap values and posterior probabilities

        .. tab:: Question
           
           What are the main differences between the ML and MrBayes trees?

Feedback Thursday
^^^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1749822/P4f2b7>`_.

.. _Friday_Second_Week:
Friday
------

Now you know all the essential steps and methods how to calculate a phylogenetic tree from sequence data. You may have realized that you had to use different file formats for different programs and different programs for different analyses.

You should know that you can also work with sequence data and make phylogenetic trees in R. One big advantage of using R is, that you can do all analyses in one software, without reformatting the input files. 

The other big advantage of R is, that you can do awesome downstream analyses with your phylogenetic tree, like analysing trait evolution when you have trait data for your taxa, or analyse community data. But this is another story.

This day is dedicated to introduce you into the basic commands in R that enable you to calculate a phylogenetic tree. Of course: R walks along the analytical path from sequence to tree in its very own way. However, this may even help you to better remember or even understand the single steps that are involved in building a phylogenetic tree from scratch.

Depending on your present day R skills, you may only skim through some of the sections. You will see which are relevant for you to read.

.. note::

  **At the end of the day, you will**

  Be more versatile and confident when working with genetic data.

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`Ape_package`.
           2. Read section :ref:`Getting_Started_with_R`.
           3. Download the R script and the example files `here <https://owncloud.gwdg.de/index.php/s/png6HlTkiN1FjO5>`_.

        .. tab:: Exercise 1
           
           1. Copy-and-paste the multisequence FASTA files for **EF** and **18S** from **Monday** to a new folder named **Friday/Tutorial_1** on your PC. 
           2. Open R or RStudio and set the folder **Friday/Tutorial_1** as working directory.
           3. Remember to (download and) activate all required packages.

        .. tab:: Exercise 2

           1. Align the multifasta sequences ``T1_A4_Oribatida_EF.fas`` and ``T1_A4_Oribatida_18S.fas`` using the ``msa( )`` function in R.
           2. Use the CLUSTAL algorithm and set `10` and `0.1` as gap opening and gap penalties, respectively.
           3. Save the alignments as ``EF_aln1.fas`` and ``18S_aln1.fas``.
           4. Open the alignments in Geneious Prime, check and trim to the shortest sequence.
           5. Save the trimmed alignments as ``EF_aln2.fas`` and ``18S_aln2.fas`` to **Friday/Tutorial_1**.

        .. tab:: Questions

           1. How long (bp) is the trimmed alignment for: **EF** and **18S**
           2. How long (bp) is the best alignment from **T2**: **EF** and **18S**
           
           .. important::
              If you have followed the above instructions, you disobeyed a formal alignment rule. **Which one?** 

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Exercise

           1. Calculate a Neighbor Joining tree based on p-distances for ``EF_aln2.fas`` and ``18S_aln2.fas``.
           2. Save the distance matrix for each alignment as ``csv``, name it ``dEF.csv`` and ``d18S.csv``, to **Friday/Tutorial_2** on your PC
           3. Calculate 1000 bootstraps for each tree.
           4. Plot each tree nicely (:r:`ladders right=FALSE, cex=0.7`) with bootstrap in percent and in ``lightblue`` colour in circles with ``white`` background.
           5. Save the NJ trees with nodelabels as ``NJ_EF.tre`` (with ``red`` tip labels) and ``NJ_18S.tre`` (with ``lightblue`` tip labels).


  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Exercise

           Calculate the model of sequence evolution in R for the trimmed alignments ``EF_aln2.fas`` and ``18S_aln2.fas``.

        .. tab:: Question
           
           What is the best fit model for: **EF** and **18S**?

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Exercise

           1. Calculate ML trees for ``EF_aln2.fas`` and ``18S_aln2.fas``, respectively.
           2. Plot both trees in one graphic, with facing tip labels. **EF** with ``green`` and **18S** with ``yellowgreen`` tip labels.
           3. Display bootstrap values with ``red circles`` and background in ``pink1``.
           4. Save both trees in one plot as PDF, name it ``ML_EF_18S.pdf``

        .. tab:: Questions

           1. Are the NJ and ML trees calculated in R similar to the trees calculated in Exercises of :ref:`Tutorials_3` and :ref:`Tutorials_4`?
           2. Can you see fundamental differences?
           3. Do you consider both ways (R and MrBayes/RaXML in Geneious Prime) as comparable?

.. important::

  - Calculate the number of haplotypes in the dataset ``Onova_example_COI``.
  - How many sequences are in this data set and how many haplotypes?
  - Plot the haplotype list as barplot, sorted from many to few.
  - Save the barplot including a title as pdf. Name it ``Onova_hts_plot.pdf``.

Feedback Friday
^^^^^^^^^^^^^^^
To provide feedback, please complete our `questionnaire <https://easy-feedback.de/evolecol/1750601/rb9hpW>`_.
