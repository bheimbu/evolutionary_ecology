.. _second-week:
Second Week
===========
Major Goals
-----------
This week focuses on DNA sequences: how to work with them, where to obtain them if you prefer not to sequence organisms yourself, and how to infer phylogenetic trees.

Lectures and videos provide a step-by-step guide on handling sequence data and conducting phylogenetic analyses. Each day, tutorials will cover a different method, and you must complete each tutorial and its exercises to progress to the next day's topic.

The week begins with assembling, checking, and exporting your raw sequences (PCR products sequenced last week) to generate high-quality consensus sequences. We start with your DNA sequences to help you become familiar with (1) Sanger DNA sequencing, (2) sequence evaluation (or 'What's the difference between a bad and good DNA sequence?'), (3) ambiguous (wobble) DNA positions and where do they come from; and (4) DNA sequences derived from public data repositories.

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
Then, you can start reading the sections about :ref:`Geneious_Prime` and Genbank (see :ref:`Database_and_Search_Strategy`), which introduces you to the handling of sequence data and how to use Genbank, a public sequence data repository.

By doing the exercises in this tutorial, you will generate a toy dataset, which you will be using for the whole week. All following tutorials and exercises are based on this toy dataset.

The basic idea is, that all of you work with the same toy dataset, which makes it easier to compare results. However, it is also fine if you add some of your own sequences (those you checked and exported earlier today).

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements
               
            1. Read section :ref:`Geneious_Prime` and check out the `Geneious Prime User Manual <https://manual.geneious.com/en/latest/index.html>`_.
            2. See the `sequence assignment list <https://docs.google.com/spreadsheets/d/1jLPmKAFAuehtg1MWWZrVGDfeNNqv-mfPGC4dCOA2GbI/edit?usp=sharing>`_.
            3. Check out, which raw reads have been assigned to you.

        .. tab:: Exercise 1

           1. Open Geneious Prime and create the folder **Monday/Tutorial_1** and subfolders for each gene.

           .. code::

              Local
                ├── Monday
                │     └── Tutorial_1
                │            ├── 18S
                │            ├── 28S
                |            └── COI
                └── …
           
           2. Download and import your `raw sequences  <https://owncloud.gwdg.de/index.php/s/043zOxxBqrRPwx2>`_ to Geneious Prime.

        .. tab:: Exercise 2
       
           1. Find the matching raw reads i.e., the forward and the reverse sequence(s) of the same sample (Note that 18S consists of more than two sequences).
           2. Assemble the matching read pairs (*Align/Assemble -> De Novo Assemble*), store them in separate subfolders (Check the box *Save in sub-folder*).
           3. Name your consensus sequences in the following format: ``$Sample number_$Genus_$Species_$Gene_$Initials`` (eg. ``1_Acrogalumna_longisetosa_18S_BH``).

           .. code::

              Local
                ├── Monday
                │     └── Tutorial_1
                │            ├── 18S
                |            |    └── 1_Acrogalumna_longisetosa_18S_BH
                │            ├── 28S
                |            └── COI
                └── …

           4. Check the consensus sequence and correct ambiguous positions.
           5. Export the consensus sequences as FASTA files to your PC.
           6. Upload the consensus files `here <https://owncloud.gwdg.de/index.php/s/HHos7foArlDQqtx>`_.

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

        .. tab:: Exercises

           1. Open the form and answer the question. `Click here for the form <https://form.jotform.com/250502078222345>`_.
           2. Download the sequences from NCBI with the accession numbers given in the form as separate sequence files in FASTA format.

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Exercises
    
           1. Draw a phylogenetic tree of the six major groups of Oribatida.
           2. Write the names of the major groups on the branches and the species' names from **Tutorial 3** at the tips.
           3. Take a picture of your drawing and upload it `here <https://owncloud.gwdg.de/index.php/s/OA626D9jAiUfDrP>`_.

  .. tab:: Tutorial 5

     .. tabs::

        .. tab:: Exercises

           1. Download the 18S rDNA gene for all taxa given in **Tutorial 3**.
           2. Use the Clipboard option to save all sequences in FASTA format as a single file (name the file ``Tutorial_5_Oribatida_18S.fas``) to your PC.

          .. attention::

              There is no 18S rDNA sequence available for *Carabodes femoralis*, use *Carabodes subarcticus*. For *Platynothrus peltifer*, four 18S sequences are available, download the sequence with the accession number ``EF091422``.

          .. hint::

              A rule of thumb: If two or more sequences are available for a species, always choose the longest sequence.

        .. tab:: Questions

           1. What do you consider the key benefits of an online database?
           2. Write down your answer on a sheet of paper.

  .. tab:: Tutorial 6

     .. tabs::

        .. tab:: Exercises

           1. Take the sequences from **Tutorial 3** and copy them to subfolder **Tutorial 6**.

           .. code::

              Local
                ├── Monday
                │     ├── Tutorial_1
                │     └── Tutorial_6
                └── …

           2. Change all sequence names from GenBank to: ``$GENUS_$SPECIES_$ACCESSION NUMBER_$GENE`` (e.g. ``Archegozetes_longisetosus_EF081321_EF``).

           .. code::

              Local
                ├── Monday
                │     ├── Tutorial_1
                │     └── Tutorial_6
                │            ├── Archegozetes_longisetosus_EF081321_EF
                │            └── …
                └── …

  .. tab:: Tutorial 7

     .. tabs::

        .. tab:: Exercise 1

           1. Open the file ``Tutorial_5_Oribatida_18S.fas`` from **Tutorial 5** with your local text editor of choice (e.g. Notepad++, Editor).
           2. Change the sequence names from GenBank just as in **Tutorial 6** (``$GENUS_$SPECIES_$ACCESSION NUMBER_$GENE``).
           3. Import the file to Geneious Prime in a new subfolder with the name **Monday/Tutorial_7** (as *separate sequences*).

           .. code::

              Local
                ├── Monday
                │     ├── Tutorial_1
                │     ├── Tutorial_5
                │     ├── Tutorial_6
                │     └── Tutorial_7
                │           ├── Archegozetes_longisetosus_EF081321_18S
                │           └── …
                └── …

           .. note::
              You now have two datasets with +/- identical taxon sampling but with two different genes. Awesome!

        .. tab:: Exercise 2

           1. Now you can add (import) some of your own sequences to the 18S file.
           2. Your own sequences should be named in the same logic as the sequences from NCBI.
           3. As no accession numbers are available for your new sequences, you may replace accession number with ``own``, to quickly identify your own sequence among the others, for example: ``Archegozetes_longisetosus_own_18S``.
     
           .. important::

              Do not add more than four 18S sequences, please. It is helpful to keep the dataset small, because larger datasets will require longer running times (i.e. longer waiting time for you). It will also be more difficult to focus on the most relevant information.

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

           1. Use your DNA sequences from Monday, namely from **Tutorial 6** and **Tutorial 7** to generate alignments in Geneious Prime using the parameters below (all other parameters **keep in default mode**).
           2. In order to do this, mark all sequences in the repective folder and click on ``Align/Assemble -> Multiple Align -> Geneious Alignment``.

           .. code::

              Local
                ├── Monday
                │     ├── …
                │     ├── Tutorial_6
                │     |     ├── Archegozetes_longisetosus_EF081321_EF
                │     |     └── …
                │     └── Tutorial_7
                │           ├── Archegozetes_longisetosus_EF081321_18S
                │           └── …
                └── …

           .. thumbnail:: /_static/T2_A_1.png

           .. attention::

               Use a period ``.`` not a comma ``,`` when typing the penalty values!

           2. Change the names of the alignments :kbd:`F2` like this ``18S_Tutorial_1_a_aln`` (``$GEN_$TUTORIAL_$ALIGNMENT LETTER_aln.``) and drag or move them to a new subfolder named Tuesday/Tutorial_1.

           .. code::

              Local
                ├── Monday
                └── Tuesday
                     └── Tutorial_1
                           ├── EF_Tutorial_1_a_aln
                           ├── EF_Tutorial_1_b_aln
                           ├── EF_Tutorial_1_c_aln
                           ├── 18S_Tutorial_1_d_aln
                           ├── 18S_Tutorial_1_e_aln
                           └── 18S_Tutorial_1_f_aln

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Exercises

           1. Open the form and answer the questions. Click `here <https://form.jotform.com/250502705235346>`_.
           2. Compare your results with your neighbour.

  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Exercises
               
           1. Read section :ref:`Sequence_Editing`.
           2. Download the `zip file <https://owncloud.gwdg.de/index.php/s/NTlCINO554DbSzZ>`_.
           3. Open each file in your local text editor of choice (i.e. Editor or Notepad++ for Windows) and answer the questions given in the form. Click `here <https://form.jotform.com/250495579645068>`_.

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Exercise

           1. Open the form and answer the questions. Click `here <https://form.jotform.com/250503287348357>`_.

.. _Wednesday_Second_Week:
Wednesday
---------

Today, we have three learning modules:

1. :ref:`Models_of_Sequence_Evolution`.

2. :ref:`How_to_Infer_Phylogenetic_Trees`.

3. :ref:`How_To_Draw_Phylogenetic_Trees`.

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
           2. Read section :ref:`Models_of_Sequence_Evolution`.

        .. tab:: Exercise 1

           1. Use jModelTest to calculate the best fitting model of sequence evolution (see section :ref:`Models_of_Sequence_Evolution` for how to work with jModelTest).
           2. Use your best alignments for EF and 18S, respectively from **Tuesday/Tutorial_1**.
           3. Safe the HTML log file on your PC.

        .. tab:: Exercise 2

           1. Open the form and answer the questions. Click `here <https://form.jotform.com/250503303460341>`_.

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`How_to_Infer_Phylogenetic_Trees`.
           2. Read section :ref:`How_To_Draw_Phylogenetic_Trees`. Don't be confused—this section primarily focuses on the standalone version of FigTree. However, all the settings explained here are also available in the Geneious Prime plugin.
           3. See also this `viewing-and-formatting-trees in Geneious Prime <https://manual.geneious.com/en/latest/Phylogenetics.html#viewing-and-formatting-trees>`_.

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

           2. Copy your best alignments from EF and 18S (from **Tuesday/Tutorial_1**) into their respective subfolders.
           3. For **both** alignments calculate a NJ tree using the **Jukes-Cantor** model of sequence evolution (`Tree -> Geneious Tree Builder -> Genetic Distance Model: Jukes-Cantor`) with 1000 bootstrap replicates (`Resample tree -> Resampling Method: Bootstrap` + `Number of Replicates: 1000`).
           4. Root the tree using *Zercon* sp. (Click on the end of the branch leading to *Zercon* sp. and hit `Root` in the subpanel).
           5. Indicate in the file name that this tree uses the **Jukes-Cantor** model, for example, ``EF_JC_model``.
       
        .. tab:: Exercise 2

           1. For **both** alignments calculate a NJ tree using the **Tamura-Nei** model of sequence evolution and 1000 bootstrap replicates.
           2. Root the tree using *Zercon* sp.           
           3. Indicate in the file name that this tree uses the **Tamura-Nei** model, for example, ``EF_TN_model``.

        .. tab:: Exercise 3

           1. Present the trees from **Exercise 1** and **Exercise 2** as phylograms in PowerPoint.
           2. Display the trees with increasing node order (see the right panel and click on `Formatting -> Order branches -> Ordering: increasing`) and export them as JPEG (`File -> Save as Image File`).
           3. Display the NJ trees of EF and 18S on separate slides/pages in PowerPoint (or any other presentation software).

        .. tab:: Questions
           
           Open the form and answer the questions. Click `here <https://form.jotform.com/250505928456058>`_.

  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Attention!

           .. attention::

              - Complete all **exercises** and **questions** by hand with pen and paper (except for **Exercise 2**)!
              - Hand in your results by the end of the day. 
              - We will discuss them tomorrow morning.

              - Do no forget to include your name or initals!

        .. tab:: Exercise 1

           1. Draw by hand all unrooted tree topologies that are possible for four taxa (A, B, C, D).
           2. In one of the trees, use arrows to indicate where the tree might be rooted.
           3. How many topologies are possible for a rooted tree with four taxa (A, B, C, D)?
           4. Draw all possible combinations.

           .. attention::
              Some topologies might be redundant!

        .. tab:: Exercise 2
  
           1. Use a text editor and draw the following tree: ``((((A,(B,(C,D))),E),(F,G)),H);``.
           2. Check your topology using FigTree in Geneious Prime.
        
        .. tab:: Questions

           1. Why are trees with four taxa interesting to mathematicians compared to trees with two or three taxa?
           2. What is the difference between a cladogram, a phylogram, and a chronogram?

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Background

           Phylogeography is the study of the genetic structure of species within or between geographic regions.
           If populations are geographically distant from each other, gene flow is usually reduced and both populations accumulate mutations independently, which increases genetic distance between taxa.
           If gene flow continues between geographically distant populations, or if they share a common ancestor from which they recently separated, their genetic distance is comparatively small.

           .. note::
              In the course of a Master's thesis, a student investigates the relationships of two populations of the oribatid mite `Steganacarus magnus` (SM) from Germany (D) and France (F). To understand the relationships between the two populations, the student sequenced the COI mitochondrial gene of seven individuals and generated a matrix that shows the genetic distances between all individuals (see distance matrix under **Exercise**).

        .. tab:: Exercises

           .. attention::
              Do it all by hand with pen and paper!

           1. To infer if the two populations have a recent common ancestor, draw a UPMGA tree and calculate the length of all tree branches.
           2. Write down the tree with all distance calculations and intermediate distance matrixes.
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
           | SM_F1 |   5   |   2   |   3   |  39   |   -   |       |       |
           +-------+-------+-------+-------+-------+-------+-------+-------+
           | SM_F2 |  67   |  68   |  71   |  70   |  68   |   -   |       |
           +-------+-------+-------+-------+-------+-------+-------+-------+
           | SM_F3 |  72   |  73   |  74   |  72   |  73   |   6   |   -   |
           +-------+-------+-------+-------+-------+-------+-------+-------+

.. _Thursday_Second_Week:
Thursday
---------

Today, it's all about search algorithms. You will learn the basics of the two most common methods for calculating phylogenetic trees – :ref:`Maximum_Likelihood` in the morning and :ref:`Bayesian_Inference` in the afternoon.

Both methods are widely used, because they are more thorough than Cluster methods and they approach the mathematical part of inferring phylogenetic trees from different angles. You will hear more about this in the :ref:`lectures` that are accompanied with the two sections.

Today, we use two programs that can only be controlled via the command line and do not have a GUI (graphical user interface), namely :ref:`RAxML <Raxml>` (`download here <https://owncloud.gwdg.de/index.php/s/feKtzea2J1avgZw>`_) and :ref:`MrBayes <MrBayes>` (`download here <https://owncloud.gwdg.de/index.php/s/YyIcVOeqUWKxilX>`_).

But luckily both programs can be installed as plugins in Geneious Prime. Heureka! See **Tutorial 1** and **Tutorial 2** for doing so.

While working through the exercises, many topics you have been dealing with earlier this week will come up again, such as input file format or :ref:`Models_of_Sequence_Evolution`.

.. note::
  **At the end of the day you will…**

  - Know the difference between Cluster and Search algorithms.
  - Know why search algorithms take so much longer for analysing genetic data than Cluster algorithms.
  - Know that ML uses likelihoods, and MrBayes uses posterior probabilities to calculate internal nodes and topologies of trees.
  - Know what MCMC is and for which type of analysis it is mandatory.
  - Be able to interpret the different statistics MrBayes provides.
  - Understand the meaning of prior and posterior probabilities.
  - Understand the difference between bootstraps and posterior probabilites and why they are not directly comparable.

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`RAxML <Raxml>`. Don't be confused—this section primarily focuses on the command-line version of RAxML. However, all the settings explained here are also available in the Geneious Prime plugin.
           2. Install the **RAxML** plugin in Geneious Prime (`Tools -> Plugins -> Available Plugins`).

        .. tab:: Exercise 1

           1. Create two new subfolders for the RAxML analyses of **EF** and **18S** in Geneious Prime.

           .. code::

              Local
                ├── Monday
                ├── Tuesday
                ├── Wednesday
                └── Thursday
                     └── Tutorial_1
                           ├── 18S
                           └── EF 

           2. Copy your best alignments from EF and 18S (from **Tuesday/Tutorial_1**) into their respective subfolders.
           3. Start the ML analyses with following parameters (`Tree -> RAxML`):

              - GTR GAMMA I (`Nucleotide Model: GTR GAMMA I`)
              - Rapid bootstrapping and search for best-scoring ML tree (`Algorithm: Rapid bootstrapping and search for best-scoring ML tree: Command line: -f a -x 1`) 
              - 500 bootstrap replicates (`Number of starting trees or bootstrap replicates: 500`)
              - Any other parameter in default settings
           4. Write down how long the analyses took (in seconds).

        .. tab:: Question
     
           1. How can we be sure that a tree is good? More than one solution is possible!

           .. note::
              When constructing phylogenetic trees, we can only approximate the true phylogenetic relationship between taxa because we only work with a random sample of taxa.

           .. thumbnail:: /_static/haplotypes.png


  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`MrBayes <MrBayes>`. Don't be confused—this section primarily focuses on the command-line version of MrBayes. However, all the settings explained here are also available in the Geneious Prime plugin.
           2. Install the **MrBayes** plugin in Geneious Prime (`Tools -> Plugins -> Available Plugins`).

        .. tab:: Exercise 1

           1. Create two new subfolders for the RAxML analyses of **EF** and **18S** in Geneious Prime.

           .. code::

              Local
                ├── Monday
                ├── Tuesday
                ├── Wednesday
                └── Thursday
                     ├── Tutorial_1
                     └── Tutorial_2
                           ├── 18S
                           └── EF

           2. Copy your best alignments from EF and 18S (from **Tuesday/Tutorial_1**) into their respective subfolders.
           3. Start the Bayesian Inference using MrBayes (`Tree -> MrBayes`) with following parameters:

              - Use ``GTR+G+I`` as model of sequence evolution (`Substitution Model: GTR` + `Rate Variation: invgamma`)
              - Set the outgroup (`Outgroup: Zercon sp.`)
              - Use 1 million generations (`Chain Length: 1,000,000`) and sample every 100th generation (`Subsampling Freq: 100`)
              - Use a burn-in of 10% (`Burn-in Length: 1000`)
           4. Write down how long the analysis took (minutes + seconds).

        .. tab:: Questions
       
           1. Which parameter-settings deviate from the default settings?
           2. What is the `Average standard deviation of split frequencies` of your analyses? Use ``EF_Tutorial_1_b_aln - Posterior output`` and look for the tab :kbd:`Raw Posterior Output` in the lower panel. There you will find a column `StdDev(s)`. Click on :kbd:`Show entire ### bytes (may be very slow)` to show the whole output.

           .. note::

              The **Average standard deviation of split frequencies** is a measure used in Bayesian phylogenetic inference to assess convergence and stability of the MCMC (Markov Chain Monte Carlo) chains during the analysis. The split frequency measures how often a particular split appears across all sampled trees from an MCMC chain.

              Low average standard deviation means the chains are producing similar trees, indicating that the analysis is likely converging to a consistent result.

              High average standard deviation means the chains are producing more different trees, indicating that the analysis may not have converged yet.
           
           **Bonus question:** What is the credible sets of trees (search online for more information)?

  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Background

           .. note::
              The choice of priors (setting of parameters prior to the analysis) is important for Bayesian Inferences, as they influence the computing time and the search efficiency in the parameter landscape
              However, as priors are usually unknown we will use flat priors!

        .. tab:: Questions
 
           Open the form and answer the questions. Click `here <https://form.jotform.com/250505884089364>`_.

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Exercises

           1. Import all trees you made into PowerPoint.
           2. Separate the trees according to gene, ML and BI analyses, respectively.
           3. Save them on a DIN A4 page.
           4. Label the nodes with corresponding bootstrap values and posterior probabilities. 
           5. What are the main differences between the ML and MrBayes trees?

.. _Friday_Second_Week:
Friday
------

Now you know all the essential steps and methods how to calculate a phylogenetic tree from sequence data. You may have realized that you had to use different file formats for different programs and different programs for different analyses.

You should also know that you can work with sequence data and make phylogenetic trees in R. One big advantage of using R is, that you can do all analyses in one software, without reformatting the input files. 

The other big advantage of R is, that you can do awesome downstream analyses with your phylogenetic tree, like analysing trait evolution when you have trait data for your taxa, or analyse community data. But this is another story.

This day is dedicated to introduce you into the basic commands in R that enable you to calculate a phylogenetic tree. Of course: R walks along the analytical path from sequence to tree in its very own way. However, this may even help you to better remember or even understand the single steps that are involved in building a phylogenetic tree from scratch.

Depending on your present day R skills, you may only skim through some of the sections. You will see which are relevant for you to read.

.. note::

  **At the end of the day, you will…**

  Be more versatile and confident when working with genetic data in R.

Tasks of the Day
^^^^^^^^^^^^^^^^

.. tabs::

  .. tab:: Tutorial 1

     .. tabs::

        .. tab:: Requirements

           1. Read section :ref:`Ape_package`.
           2. Read section :ref:`Getting_Started_with_R`.
           3. Install `R <https://cran.rstudio.com/>`_ and `RStudio <https://posit.co/download/rstudio-desktop/>`_. 
           4. Download the R script and the example files `here <https://owncloud.gwdg.de/index.php/s/7uxes6DVDjd44K7>`_.

        .. tab:: Exercise 1
           
           1. Export your sequences from **Monday/Tutorial_6** and **Monday/Tutorial_7** as FASTA files to your PC. Name them ``Oribatida_18S.fas`` and ``Oribatida_EF.fas``, respectively.
           2. Open R or RStudio and set the folder containing the files as the working directory.
           3. Remember to (download and) activate all required packages.

        .. tab:: Exercise 2

           1. Align the multifasta sequences ``Oribatida_EF.fas`` and ``Oribatida_18S.fas`` using the ``msa( )`` function in R.
           2. Use the CLUSTAL algorithm and set 10 and 0.1 as gap opening and gap penalties, respectively.
           3. Save the alignments as ``EF_aln1.fas`` and ``18S_aln1.fas``.
           4. Open the alignments in Geneious Prime, check and trim to the shortest sequence.
           5. Export the trimmed alignments as ``EF_aln2.fas`` and ``18S_aln2.fas`` to your PC preferably in the same folder as your other files.

        .. tab:: Questions

           1. How long (bp) is the untrimmed alignment for **18S** and **EF**?
           2. How long (bp) is the trimmed alignment for **18S** and **EF**?

           
           .. important::
              If you have followed the above instructions, you disobeyed a formal alignment rule. **Which one?** 

  .. tab:: Tutorial 2

     .. tabs::

        .. tab:: Exercise

           1. Calculate a Neighbor Joining tree based on p-distances for ``EF_aln2.fas`` and ``18S_aln2.fas``.
           2. Save the distance matrix for each alignment as ``csv``, name them ``distance_EF.csv`` and ``distance18S.csv``, to your PC.
           3. Calculate 1000 bootstraps for each tree.
           4. Plot each tree neatly (``ladders.right = FALSE``, ``cex = 0.7``), displaying bootstrap values as percentages in ``lightblue`` text color, enclosed by circles with a ``white`` background..
           5. Save the NJ trees with nodelabels as ``NJ_EF.tre`` (with ``red`` tip labels) and ``NJ_18S.tre`` (with ``lightblue`` tip labels).


  .. tab:: Tutorial 3

     .. tabs::

        .. tab:: Exercise

           Calculate the model of sequence evolution in R for the trimmed alignments ``EF_aln2.fas`` and ``18S_aln2.fas``.

        .. tab:: Question
           
           What is the best fitting model for **EF** and **18S**?

  .. tab:: Tutorial 4

     .. tabs::

        .. tab:: Exercise

           1. Calculate ML trees for ``EF_aln2.fas`` and ``18S_aln2.fas``, respectively.
           2. Plot both trees in one graphic, with facing tip labels. **EF** with ``green`` and **18S** with ``yellowgreen`` tip labels.
           3. Display bootstrap values enclosed in ``red`` circles with a ``pink1`` background.
           4. Save both trees in one plot as PDF to your PC, name it ``ML_EF_18S.pdf``.

        .. tab:: Questions

           1. Are the NJ and ML trees calculated in R similar to the trees calculated in Geneious Prime?
           2. Can you see fundamental differences?
           3. Do you consider both ways (R and MrBayes/RaXML in Geneious Prime) as comparable?

  .. tab:: Bonus Tutorial

     .. tabs::

        .. tab:: Exercise

           - Calculate the number of `haplotypes <https://en.wikipedia.org/wiki/Haplotype>`_ in the dataset ``Onova_example_COI``.
           - How many sequences are in this data set and how many haplotypes?
           - Plot the haplotype list as barplot, sorted from many to few.
           - Save the barplot including a title as pdf. Name it ``Onova_hts_plot.pdf``.
