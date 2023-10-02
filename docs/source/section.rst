.. _section:
Sections
========
 
.. _Geneious_Prime:
Geneious Prime
--------------
Geneious Prime is a molecular biology and sequence analysis tool, and helps you to organize data and projects in an efficient way.

.. note::
  It is important that the consensus sequences are of high quality (checked for sequencing errors or true heterozygosity) and that ambiguous positions are removed in order to infer correct phylogenies. Standard Sanger sequencing methods produce DNA sequences of ~700-900 bp long, however ~30 bp at the start/end of the sequence is usally of poor quality. This is due to primer deterioration, incorrect primer annealing, and/or aborted elongation, as well as technical limitations in accurately separating very short and very long DNA strands at the nucleotide level. To obtain high quality consensus sequences, it is common to sequence and assemble the forward and reverse strands of a PCR product. In this way it is possible to correct ambigous positions. Furthermore, by assembling forward and reverse sequences, the resulting consensus sequence is usually longer than any single strand, thus providing more phylogenetic information. Sequencing facilities normally provide raw sequencing data in ``.abi`` format (also known as DNA trace file). This file contains the DNA sequence electropherogram as well as raw data. The electropherogram (=chromatogram) shows the DNA trace during the sequencing process and can be viewed graphically. Most sequencing editors can open ``.abi`` trace files, such as BioEdit. However, most sequencing editors and analyses software that combine the DNA sequence and the chromatogram in a single analysis window, which considerably simplifies the processing of sequences, are commercial (e.g. Sequencher, CodonCodeAligner). Geneious Prime (Biomatters) provides a 30-day trial version, which we will use for analysing the sequences generated last week. You can download Geneious Prime `here <https://manage.geneious.com/free-trial>`_ and install it on your PC. If you want to watch a tutorial about Geneious Prime see `here <https://owncloud.gwdg.de/index.php/s/sqsaiyuKYoiHgT0>`_ or under :ref:`lectures`.

Working with Geneious Prime
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Launch Geneious Prime

2. Create a new folder for your project

3. Drag and drop the ``.abi`` files from your explorer/finder into the sequence panel to import the sequence files

.. thumbnail:: /_static/geneious_1.png

4. Check out all single sequence files that belong to the same sample

- For 18S there are 6 files (3 forward and 3 reverse)
- For 28S and COI there are only 2 (1 forward and 1 reverse)

5. Assemble contigs

- Select De Novo Assemble from the Align/Assemble menu
- (also: Tools —> Align/Assemble —> De Novo Assemble

.. thumbnail:: /_static/geneious_2.png

6. Provide a name for the newly assembled sequence file

.. attention::
  Never ever use special characters or spaces!

.. thumbnail:: /_static/geneious_3.png

Now all single sequence files are pieced together (=assembled) and all complementary positions of all forward and reverse sequences are displayed underneath each other:

- You now have a ``.contig`` file (not a Sanger file or single nucleotide sequence), which is indicated by the icon in front of the name
- Scan the contig by eye to ensure that no ambiguous base calls are included 
- Geneious Prime automatically removes positions (base pairs) at the start/end of each sequence with a quality below a certain quality threshold (, which can be adjusted, if necessary)
- Positions that have been removed are indicated by a light pink bar underneath the respective sequence in the chromatogram
- If you have ambiguous positions (indicated by letters that are not ``A``, ``C``, ``G``, or ``T``; highlighted in red), correct them manually according to the peak call of the sequence with the highest quality at this position.

.. note::
  - Correcting the consensus sequence saves the change in both forward and reverse sequence
  - Correcting the base in the erroneous sequence (either forward or reverse) changes the consensus sequence, but saves the change only in the respective sequence

.. thumbnail:: /_static/geneious_4.png

.. note::
  The table below summarises the symbols used for ambiguous base calls.

.. thumbnail:: /_static/geneious_5.png

9. After checking and correcting you sequences, export the consensus sequence (= a single sequence that is the combined product of all single sequences)

- To export the consensus, see **Export Data**

.. thumbnail:: /_static/geneious_6.png

Export Data
^^^^^^^^^^^

1. Use the default settings

- Threshold: Highest Quality
- Assign Quality: Total

.. thumbnail:: /_static/geneious_7.png

2. Select Format:

- FASTA sequences/alignment (``.fasta``)

.. thumbnail:: /_static/geneious_8.png

3. Choose the destination

.. thumbnail:: /_static/geneious_9.png

4. Again, use default settings

.. thumbnail:: /_static/geneious_10.png

5. Now you can open the ``.fasta`` file in

- Any text editor like Editor or Notepad++ (Windows), TextEdit (Mac), Notepadqq (Linux)
- Or in a sequence editor like BioEdit (Windows), AliView (Mac)
- Or in Geneious Prime

.. thumbnail:: /_static/geneious_11.png

.. _Database_and_Search_Strategy:
Database and Search Strategies
------------------------------

Molecular sequence data is available from several online public databases, e.g. `NCBI GenBank` (USA), `EMBL EBI` (Europe), or `DDBJ` (Japan), to name a few. Providers manage and update entries daily via the World Wide Web. During this course, we use the service of NCBI GenBank to compare and validate our own sequence data and obtain additional sequences.

To screen the database for sequence data, two alternative search strategies are described below:
 
**1. Search the database for specific genes and taxa**

- Enter a species or higher taxon name in the search box. The order of search terms (e.g. 'oribatida d3') is neglible, as is the case sensitivity. However, it is important to limit the search to the required database, e.g., 'Nucleotide' or 'Protein'.

.. thumbnail:: /_static/database_1.png

**2. BLAST Search**

- Search for homologous genes using your own sequences.

.. thumbnail:: /_static/database_2.png

.. note::
  Again, it is important to limit the search to the required database within NCBI, e.g. 'Nucleotide' or 'Protein'.

You can upload your own sequences to the search mask (**see below**) either by copy-paste (**1a**) from a sequence editor like BioEdit or MEGA, or sequence files can be uploaded from a directory located on the hard drive (**1b**).
The BLAST search can be accelerated by limiting the search to an appropriate DATABASE (**2**, mandatory) and to a certain ORGANISM (optional). The search starts when pressing the „BLAST“-button (**3**).

.. tip::
  The accuracy of search parameters can be adjusted (Algorithm parameters; optional), which affects the degree of similarity of sequences from the database with your sequence data. Downscaling of search parameters can be helpful for searches within variable gene regions or among distantly related (or fast mutating) organisms. Upscaling of search parameters is reasonable when working with repetitive sequences.

.. thumbnail:: /_static/database_3.png

After starting a BLAST search a new window will open confirming the search request. The search is finished when a list with all results appears.

.. thumbnail:: /_static/database_4.png

.. note::
  When you click 'Back to Traditional Results Page' you will see a graphic that shows how your DNA fragment matches (aligns) with the BLAST results (**see below**). The graphic represents the complete length of the entered sequence, matching sequences from GenBank are listed below. The colour code illustrates the degree of similarity across the complete sequence and the mouse-over option enables quick assessment of results. When moving the mouse over the graph, names and genes of GenBank entries appear.

.. thumbnail:: /_static/database_5.png

In both figures, detailed results are listed below the graph, providing the accession numbers if the BLAST hits in the last (**see above**) or first column (**see below**), linking to the complete database entry with a full description of the sequence. Columns to the right provide information on the degree of similarity and the probability of stochastic agreement. The e-value is the most important, indicating the probability that a database entry matches with the original sequence simply by chance. The smaller the e-value the better: the lower the probability that two sequences match by chance the higher the probability to have a real homologous sequence. Ideally the e-value should be very small (e.g. 2e-152).

.. hint::
  Any published sequence in GenBank is linked with a unique `accession number <https://www.ncbi.nlm.nih.gov/genbank/samplerecord/#AccessionB>`_. A GenBank record provides information on the length, name of the gene, and a detailed taxonomic description of the organism from which the sequence derived. Additionally, information on authors and a reference to the publication in which the sequence was first cited are provided within the record, as well as many other things.

Any sequence from GenBank can be downloaded to a local hard drive. The GenBank file format is rather inconvenient and not recognized by some text editors and phylogenetic programs. The most common sequence format supported is `FASTA <https://en.wikipedia.org/wiki/FASTA_format>`_.


.. _Downloading_and_Saving:
Downloading and Saving
----------------------

Sequences can be visualized and downloaded in different formats by selecting „Display Settings“ options (top left). Selecting FASTA, the website is updated showing the sequence in the respective file format. To download the sequence on the local hard drive, click on „Send to“ (top right) which opens a drop-down menu to select the destination and format of the sequence file.

.. note::
  Sequences can be saved separately (one-by-one) or as sequence stack (=multiple FASTA file), see below for more.

.. thumbnail:: /_static/downloading_1.png

**1. Separate download of sequences from a list of search hits:**

- Tick the box left to the sequence you wish to save
- Go to 'Send to' (top right)
- Select 'Complete Record' (only visible for coding sequences)
- 'Choose Destination: File'
- 'Download 1 items: Format: FASTA'
- Select 'Create File', which saves the sequence to your hard drive

.. thumbnail:: /_static/downloading_2.png

**2. Download a stack of sequences from a list of search hits:**

- Tick all sequences of interest
- Go to „Send to“and select „Clipboard“ [files from alternative searches can be added (tick the box left to the sequence → 'Send to' → 'Clipboard')]
- Once all required sequences are saved to the clipboard:
- Click on 'Clipboard' (top right) and check if your desired sequences are included
- Saving the content of the clipboard to a local hard drive:

  - Go to 'Send to' (top right)
  - Select 'Complete Record'
  - 'Choose Destination: File'
  - 'Format: FASTA'
  - Select: 'Create File', which saves the sequence file to a local hard drive

.. thumbnail:: /_static/downloading_3.png

.. note::
  All sequences from the clipboard are now saved in a single file. Remember to change the file name from the default name (=sequences.fasta) to favouritename_favouritegene.fas.

.. tip::
  The Clipboard is a nice and easy way to collect and save large datasets from GenBank. However, if some sequences will be used in different datasets, they must be copied subsequently and saved separately.

.. hint::
  If you wish to download many sequences with continous accession numbers (e.g. from a paper), just enter the first and the last accession number separated by a colon ``:`` followed by the tag ``[accn]`` or use NCBI's `Batch Entrez <https://www.ncbi.nlm.nih.gov/sites/batchentrez>`_.
  
  .. code-block::
  
    EF091418:EF091227[accn]

.. _Bioedit:
BioEdit
-------

- Comfortable and easy editing of sequences and alignments
- Accepts most common file formats, most important formats for us are: ``.fas``, ``.aln``, ``.nex``, ``.txt``

.. thumbnail:: /_static/bioedit.png

**File**

- Open → each file opens in a separate window

- New Alignment

- Import → Sequence Alignment File → all files open in the same window > All Files `*.*` → choose to open ABI sequencing files

- Save As → ``.fas``


.. note::
  **Most important features on the toolbar:**
  
  - Title: ``„name“.fas`` → shows name of current file including directory path
  - Mode Select/Slide, Edit, Drag & Drop / Overwrite, Insert
  - Edit → read and write mode, files can be modified and saved
  - Overwrite → not recommended as accidental changes are not traceable
  - Insert → insert nucleotides or gaps
  - Selection: Position: → how many sequences are marked, name of sequence and nucleotide position
  - View → Back-colored view - options to colour-code nucleotides and invariable alignment positions (just try) 
     
.. tip::

  **Left window (text)**
  
  - sequence name → double click: opens a window with information and editing options
  - change sequence name → Apply / Apply and Close right window

  **Right window (sequence)**

  - click on sequence → overwrite / insert / copy / paste gaps or characters 
     
.. note::
  **Edit**

  - Cut/Copy/Paste/Delete ... → applies only to sequences (right window)
  - Cut/Copy/Paste/Delete ... Sequences → applies to sequences and sequence names (right and left window)
  - search → search and find for nucleotide motives in marked sequences, e.g.,primer sequences
  - select to End/Beginning → selects marked sequences from curser to end or beginning of the sequence
  
  **Sequence**

  - Nucleic Acid → Reverse / Reverse Complement → turns and translates complementary marked sequence; helpful when aligning forward- and reverse-strand
  - Toggle Translation → translates marked nucleotide sequence into the respective protein sequence and back
  - Toggle (permanent) → required in order to save translated protein sequence
  - Gaps, Lock/Unlock Gaps: After toggling between nucleotide and protein sequences,gaps are unlocked (`~`) and must be locked (`-`) again before saving the alignment

.. _Alignment:
Alignment
---------

Alignment means that molecular data (sequences) are sorted by homologous positions, and you will learn in the lecture what is meant by homologous positions in molecular data (nucleotide and amino acid sequences) and which methods have been developed to sort molecular datasets efficiently and objectively.

.. note::
  **At the end of the day you will…**

  - be able to recognize an alignment and to distinguish it from a multifasta file
  - understand why you always need to double or even triple-check an alignment
  - know what the Needleman-Wunsch algorithm is and which alignment scores exist
  - be able to explain 'gap opening' and 'gap extension' penalties and why they are used
  - recognize and understand the relevance of conserved and variable regions in genetic markers and their use in phylogeny
  - know what a reading frame is, for which type of markers it is relevant and how you take it into account in your alignment
  - understand the difficulties when aligning ribosomal DNA/RNA
  - recognize different file formats and distinguish interleaved from non-interleaved file format

ClustalX 
^^^^^^^^

- Alignment software with a graphical user interface (GUI)
- Converts several sequence and alignment formats reliably, but cannot read all formats
 - ``.fasta`` files work very well
 - Output file format for aligned sequences with file extension ``.aln``

.. attention::
  - No spaces and special characters allowed! Names of taxa longer than 30 characters are automatically truncated, potentially resulting in name duplications and program failure
  - No editing possible! Alignment file (`.aln`) needs to be opened in a sequence editor for corrections
   - **But**: Clustal algorithm is implemented in several phylogenetic programs, e.g. BioEdit, MEGA and PhyDE
   - …which enables editing of alignments without changing the program
   - allows easy switching between nucleotide- and protein sequences

 
ClustalW in BioEdit
^^^^^^^^^^^^^^^^^^^

1. Open a file with more than one sequence in BioEdit
2. Select: 'Accessory Applications'
3. Select: 'ClustalW Multiple Alignment'
4. Select: 'Multiple Alignment Parameters'
5. Fill in 'gap opening' and 'gap extension' parameters (see info box next page)
6. Run ClustalW

.. note::
  - The completed alignment opens in a new window, save it under a new name (e.g., ``name_aln.fas`` to point out that this file contains an already aligned dataset). You can select several file formats, the most common are ``.fas``, ``.txt``, and ``.phy``
  - ``.log`` files of the alignment are saved to the folder ``BioEdit/temp``; changes in the alignment can be traced there.
  - ``.dnd`` file is generated in the same folder, containing a guide-tree, which is required for the alignment (a Neighbor Joining tree in Newick-format). The tree can be opened in `FigTree <http://tree.bio.ed.ac.uk/software/figtree/>`_, note that it is not a phylogenetic tree.

.. _Sequence_Editing:
Sequence Editing
----------------

.. note::
  Essentially, sequence data (protein and nucleotide sequences, alignments, etc.) are simple text files. They are edited in a specific format which is recognized by sequence editors and phylogenetic programs. Unfortunately, almost as many formatting styles as analyzing programs exist. Some of the most common editing styles (fasta and text for sequences, phylip and nexus for alignments) are listed here:

**Sequence files**

Example fasta file ( ``.fas`` )

.. code:: text

  >Archegozetes_longisetosus_COI
  GGATCTTCACTG.....
  >Atropacarus_sp_COI
  GGAACTTCGTTA......

Example txt file ( ``.txt`` )

.. code:: text

  Archegozetes_longisetosus_COI   GGATCTTCACTG....
  Atropacarus_sp_COI   GGAACTTCGTTA.....

**Alignment files**

Example phylip file ( ``.phy`` )

.. code:: text

  2 565
  Archegozet   GGATCTTCACT....
  Atropacaru   GGAACTTCGTTA...


Example nexus file ( ``.nex`` )

.. code:: text

  #NEXUS
  BEGIN DATA;
  dimensions ntax=4 nchar=565; format missing=?
  interleave=no datatype=DNA gap= -;

  matrix
  Archegozetes_longisetosus_COI GGATCTTCACTGAGAGCTCTAATCCGTCTCGAATTAGGACAACCAGG...
  Hermannia_gibba_COI GGGTCCTCCTTAAGAGGTTTAATTCGACTGGAGTTAGGCCAGCCTGG...
  Tectocepheus_velatus_COI GGATCTTCTCTGAGAGGATTGATTCGTTTAGAATTGGGACAGCCAGG...
  Atropacarus_sp_COI GGAACTTCGTTAAGGTCTATGATTCGATTTGGGGGGGTTAGGTTCGA...

.. thumbnail:: /_static/alignments_1.png

.. thumbnail:: /_static/alignments_2.png

.. thumbnail:: /_static/alignments_3.png

.. _Models_of_Sequence_Evolution:
Models of Sequence Evolution
----------------------------

**jModelTest 2 (Darriba et al. 2012)**

- Compares models of sequence evolution and finds the model that fits best to the dataset
- GUI and command line mode
- Strategies for statistical model selection include:
 - Sequential likelihood ratio tests (LRTs)
 - Akaike Information Criterion (AIC)
 - Bayesian Information Criterion (BIC)
 - Performance-based decision theory (DT)


**How to compute likelihoods of models of sequence evolution**

Start jModelTest

'File' > 'Load DNA alignment'

.. thumbnail:: /_static/jmodeltest_1.png

'Analysis' > 'Compute likelihood scores'

- choose 'Likelihood settings'

'Number of substitution schemes' > 3

Start analysis > 'Compute Likelihoods'

.. thumbnail:: /_static/jmodeltest_2.png

After likelihoods have been calculated for each model, a list with all models, parameters and likelihood scores is available under

- 'Results' > 'Show results table'

Now we can calculate the model with the best likelihood score. Comparing likelihoods is not easy and sensitive to parameters. In jModelTest different methods (AIC, BIC, DT, and hLRT) are available to estimate the best likelihood.

In this course, we only want to calculate AIC and BIC using default settings → go to:

- 'Analysis' > 'Do AIC calculations'
- 'Analysis' > 'Do BIC calculations'

.. thumbnail:: /_static/jmodeltest_3.png

The program provides a very detailed list of the AIC and BIC results. For detailed information on parameters and analyses of jModeltest, click `here <http://www.phylo.org/pdf_docs/jmodeltest-2.1.6-manual.pdf>`_.

Save results of AIC and BIC calculations:

- 'Results' > 'Build HTML log' 

.. thumbnail:: /_static/jmodeltest_4.png

.. _How_to_Infer_Phylogenetic_Trees:
How to Infer Phylogenetic Trees
-------------------------------

.. note::
  Phylogenetic analyses always start with a search for the best tree followed by an a posteriori analysis that statistically checks the probabilities for the tree topology. First, you should get a feeling for properties and logic constraints of phylogenetic trees. For this, you will find here some exercises in which you need to draw trees by hand. For displaying complex trees, use the open source software FigTree. You will find more information about working with FigTree in the next section :ref:`How_To_Draw_Phylogenetic_Trees.

**Neighbor Joining (NJ)**

Neighbor Joining is one of the earliest methods to infer phylogenetic trees using molecular data. The method is fast and economic on computing time, which makes it attractive for large data sets and for a first analysis to get a „feeling“ for new data sets (Do I need more taxa? Which taxa might be useful? Is the selected outgroup appropriate?), before the longer but more accurate methods Maximum Likelihood (ML) or Bayesian Inference (BI) are used. A disadvantage of this method is that the sequence data cannot be reconstructed from the phylogenetic tree and NJ will not always find the „best“ or the „correct“ tree. The order of taxa in the alignment can also affect the tree topology.

**NJ in Seaview (Gouy et al. 2010)**

Download the program `SeaView <https://doua.prabi.fr/software/seaview>`_ and load your alignment file:

'File' > 'Open'

- Select all taxa (STRG + A)

'Trees' > 'Distance methods'

- Starts NJ analysis

.. thumbnail:: /_static/seaview_1.png

A window opens in which you can choose different parameters for the NJ analysis.

'NJ'

'BioNJ'

- an improved version of NJ that is more reliable if taxa differ strongly in substitution rate

'Save to file' 

- does not compute a tree but saves the distance matrix to a file

'Distance' (implemented models of sequence evolution that correct genetic distances according to specific model parameters)

- Observed (actual distance = uncorrected distances = pairwise-distances = p-distances)
- J-C (Jukes-Cantor) - 1 parameter model: equal base frequencies, equal transition/transversion rates
- K2P (Kimura 2 parameter) - 2 parameter model: equal base frequencies, unequal ti/tv rates
- HKY (Hasegawa, Kishino, Yano) - 5 parameter model: unequal base frequencies, unequal ti/tv rates

'Ignore all gap sites'

- on: all gap-containing sites are excluded from analysis
- off: not all sequence pairs use the same set of sites for computation of distances

'Bootstrap'

- Performs bootstrap evaluation of clade statistical support
- Type in number of replicates (min. 100; the more the better; 500 and 1000 are common numbers of replicates, depending on the size of the dataset i.e., number of taxa and positions)

'Go'

- Run Analysis

.. thumbnail:: /_static/seaview_2.png

After the NJ analysis finsihes, the resulting tree opens in a new window. Here you can (among other options):

- Display bootstrap values
- Root your tree (Re-root to set the outgroup; click on relevant square that appears)

To save your tree in Newick format:

'File' > 'Save' (rooted/unrooted) tree

- Select where you want the tree to be saved, add the file ending .tre (or .tree) so that you will recognize your tree file in your folder
- Save the tree with bootstrap values (tick the box before saving)

.. _How_To_Draw_Phylogenetic_Trees:
How To Draw Phylogenetic Trees
-------------------------------

**FigTree (Andrew Rambaut)**

This is a versatile program for the graphical visualization of phylogenetic trees. It is recommended to save the opened tree (e.g. the `.tre` file) directly under a new name to avoid to accidentally overwrite the original tree file.

.. thumbnail:: /_static/figtree_1.png

Open a tree file:

- 'File'
- 'Open'
- Select file containing the trees (e.g. .tre)

.. note::
  Always display the tree with increasing node order (STRG + U; as shown above) and save the tree with a new name ('File' → 'Save As').

In FigTree, you can make the tree pretty and easy to understand by making lines thicker, increasing font size, and adding colors to branches, clades, or taxa (as shown above). To do this, use the toolbar on the left and top. If you want to annotate or highlight, first assign to either a node, clade, or taxa. Just play around a little bit 🛝. The annotated tree can then be exported as vector graphic, PDF, or bitmap and uploaded in PowerPoint or any other presentation tool.

.. attention::
  All trees in this course should be displayed uniformly. Nodes should spread from the lower left to the upper right side (under 'Trees' -> 'Increasing Node Order'; or STR + U).
  The ``.tre`` files must be exported (File/Export ...) as ``JPEG`` in order to import them in PowerPoint or any other presentation tool.

Statistical node support (bootstraps and/or posterior probabilities) are displayed by selecting the tool 'Node Labels' or 'Branch Labels'. These are given as decimals for posterior probabilities (BI) and as percentages for bootstraps (NJ, ML).

In FigTree the relevant results of the phylogenetic analyses can be highlighted or summarized by colouring clades, branches, and tiplabels. In PowerPoint (or in other graphics editors such as `Inkscape <https://inkscape.org/de/>`_) you can add annotations, such as boxes, arrows, and other graphical objects.

.. thumbnail:: /_static/figtree_2.png

.. _Maximum_Likelihood:
Maximum Likelihood
------------------

- Stochastic approach to estimate parameters
 - Convergence to the „true“ parameters with increasing amount of data 
 - Minimal variation around the „true value“

- Calculates a likelihood for each character (any position in an alignment) and requires a lot of computing time

- Final tree is calculated from the sum of all likelihoods, the topology with the best (highest) likelihood value is selected
    
- Model of sequence evolution obligatory

**ML in RAxML (Randomized Accelerated Maximum Likelihood, Stamatakis 2006)**

The ML algorithm in older software (such as PAUP*) is very thorough but even moderately sized datasets (e.g. 40 taxa à 2,000 bp) require days to weeks of computing time. For very large datasets with dozens of genes and hundreds of taxa, a less time-intensive method is necessary. In recent years with advances in high-end computer hardware, new algorithms have been written to improve and accelerate the ML-algorithms used in PAUP*. Meanwhile, several programs exist that calculate Maximum Likelihoods faster than PAUP*. The results of ML analyses can differ between programs even if the same data set and parameters are used. If several programs yield the same results this is further support for the „true“ topology.

RAxML is one of these „fast“ ML-algorithms written for the analysis of large data sets with hundreds of taxa and several genes per taxa. Alignments with 1,900 taxa and 1,200 bp are considered small for RAxML. The high speed for ML analyses is based on the assumption that a topological search (the number of analyzed topologies) is more important for the construction of a „good“ ML tree than the calculation of exact likelihood scores.

.. thumbnail:: /_static/raxml.png

.. note::

  To avoid error messages, the alignment should be checked for formatting errors:
  
   1. Format

    - Alignment must be in phylip-format

   2. Identical sequence-names
  
    - Alignment must not contain identical sequence-names, this happens when sequence -names are truncated during format conversions
  
   3. Identical sequences
  
    - Occurs when variable regions are removed from the alignment or datasets contain only one species (e.g. data sets for biogeography)

.. attention::
  Never use special characters such as ``:``, ``;``, ``( )``, ``[ ]``.

**Settings in RAxML**

RAxML is not executed via command line or graphical user interface, but with a batch file. The complete command line is written into the batch file before starting the analysis. Here is an example command line for an „easy & fast“ ML analysis with bootstrapping:

.. code::

  RAxML-7.0.3-WIN.exe -f a -o taxaname_1,taxaname_2 -x 12345 -p 12345 -# 500 -m GTRGAMMAI -s name_alignment.phy -n suffix_of_output_file (e.g. Run01)

**Start RAxML**

The executable file (``RAxML-7.0.3-WIN.exe``), the batch file (``name.batch``) and the ``.phylip`` file have to be in the same folder. To start the program click on the ``batch`` file.

**RAxML results**

The „easy & fast“ analysis generates four output files:

- ``RAxML_info.RUN01``
 - Text file with all likelihood-values + time/bootstrap
- ``RAxML_bootstrap.RUN01``
 - Text file with all bootstrap trees
- ``RAxML_bestTree.RUN01``
 - Tree with the best likelihood-value without bootstraps
- ``RAxML_bipartitions.RUN01``
 - Tree with the best Likelihood value + bootstraps
 - Can be open directly in FigTree

.. note::
  These four files should be copied to a separate folder (``RAxML_Bsp_18S`` or ``ef``) after every analysis to avoid overwriting. To limit the risk of overwriting results, each RAxML analysis can also be started from a separate folder. This folder contains all important files (alignment, analysis specific batch file, results) after the analysis.

.. _Ape_package:
Ape package
-----------

**A very short introduction in the Ape package**

This tutorial provides basic commands for basic phylogenetic analyses in R. The advantages of using R are that different analyses can be done with one software. Phylogenetic, i.e. sequence data, and ecological data like traits, abundances, and other data like sampling sites, sampling year, can be combined easily.

In the previous tutorials you learned that one program comes for each fundamental analysis, and often files need to be converted when switching between softwares. This can be tedious for phylogenetic analyses and becomes even more complicated and time consuming for phylogenographic and populations genetic analyses, as these often use additional, non-genetic, data to analyses genetic patterns.

.. note::

  The advantages of R seem to be obvious, but one disadvantage is that you need to learn „its language“.

In this tutorial and in this course we provide commands and functions for some basic analyses and to plot the trees. Functions are not explained and we do not introduce you to the syntax of R. However, by playing around and just getting started you can learn already the basics. If you like R and appreciate its potential when it comes to data analysis, you should consider to take different courses, read some books and consult some of the many online tutorials.

.. tip::

  If you feel very insecure about R, check out this `online tutorial  <https://www.pluralsight.com/search?q=R>`_. It provides a very clear introduction into the basic terminologies and functions of R.
  On Youtube, you can find many more tutorials on R and RStudio and how to use them to do statistics, phylogenetics, and so on.

.. attention::

  Despite its many advantages, R does not have the stophisticated algorithms and efficiency of a 'real' phylogenetic software. When considering publishing your results, you should use the proper software designed for Maximum Likelihood and Bayesian Inference. The 'proper' trees can easily be imported into R and used for further analyses.

.. _Getting_Started_with_R:
Getting Started with R
----------------------

**R or RStudio**

This is up to you. `RStudio <https://posit.co/download/rstudio-desktop/>`_ is very handy, in particular if you are not used to work in the console. However, the more you get used to using R the switch to R is not unlikely. In the course you can choose what you like best, RStudio is installed on all computers.
About this tutorial

All instructions are given for the console (if not specifically indicated otherwise) but some commands are executed by mouse click in RStudio or even in R, which is not always indicated.

.. tip::
  Make notes in this tutorial which way you prefer or if you find functions you like better than others - you will need all of this again when analyzing your own data later in this course.
 
.. note::

  .. code:: r

   # This is an example R code block
   > # indicates commands, do not type it
   # Expected output is shown in grey
   # Comments and notes written after # are ignored by R and shown in green
   # Pay attention to quotes ( " " ) in commands, they indicate character strings that can be a vector or a file name or an option within a function
     
  Try to use autocomplete options when working in the console, e.g.

  - Use the tab key Tab ↹ when typing a path
  - Select the pop-up suggestions when typing commands
  - Use the ↑ arrow key to repeat previous commands

.. attention::
  If a command did not work, R returns an error message in the console. Always read the error message, most of the time these messages will be helpful and tell you about spelling mistakes or a missing bracket or that it could not find a file because it is not present in your working directory. Regardless, do not hesitate to ask any of the tutors or your neighbour.

.. note::

  All files and an R-Script are in the folder `T5.zip <https://owncloud.gwdg.de/index.php/s/png6HlTkiN1FjO5>`_.

**Before you import your data:**

.. code:: r

  #Check your working directory
  > getwd()
  [1] "C:/Users/Desktop/R/"

  # Change your working directory to the folder Tutorial 5:
  > setwd("C:/Users/Desktop/R/tutorial")

**… or in RStudio**

- To change the working directory just for this sesssion

 - 'Session' → 'Set Working Directory' → 'Choose Directory → Browse and select

- To set up a working directory as default

 - 'Tools' → 'Global Options' … → Set default directory (browse and select)

**Some useful commands**

.. code:: r

  # lists files in the current working directory
  > list.files("C:/Users/Desktop/R/tutorial") # or
  > list.files( )
  [1] "alnTest_trimmed.fas"      "datafile18S.csv"        
  [3] "datafile18S.txt"          "my_alignment_aln.fas"   
  [5] "my18Sphylogeny.tre"       "my28Sphylogeny.tre"     
  [7] "Onova_example_COI.fas"    "Onova_example_data.csv" 
  [9] "sequences.fas"            "test.fas"               
  [11] "Tutorial5_RScript.R"

.. code:: r
  
  # gives information about a file
  > file.info("18S_Alle.fasta")
                  size   isdir          mode     mtime                  ctime   
  18S_Alle.fasta  27207  FALSE          644      2011-10-13 22:35:48    2016-12-30 22:32:02
                  atime                 uid      gid       uname    grname
  18S_Alle.fasta  2017-01-04 11:22:04   501      20        hraefn   staff

.. code:: r

  # lists all objects in current environment
  > ls( )
  [1]       "countHap"      "countnet"        "dOnova"         "h"       "habitat"
  [6]       "HTnet"         "ind.hap"          "list"          "net"

.. code:: r

  # remove objects, helpful for cleaning up your working environment after playing around with data
  > rm(content)  # removes object content, note there will be no warning whatsoever

.. code:: r

  # returns the class R assigns to objects by R, functions use and require specific classes
  > class(my.sequences)
  [1] "DNAbin"

.. code:: r

  # gives internal structure of R object, to some extent useful alternative to summary()
  > str(On_data)
  'data.frame':      39 obs. of  5 variables:
  $ sequence: Factor w/ 39 levels "KF293402_On_HA_F_048",..: 1 2 3 4 5 6 7 8 9 10 ...
  $ accn    : Factor w/ 39 levels "KF293402","KF293403",..: 1 2 3 4 5 6 7 8 9 10 ...
  $ habitat : Factor w/ 4 levels "F","G","IFG",..: 1 1 1 1 3 3 3 3 4 3 ...
  $ site    : Factor w/ 4 levels "HA","KW","SO",..: 1 1 1 1 1 1 1 1 2 2 ...
  $ ht      : int  3 3 3 3 4 4 4 4 4 7 …

  → object On_data is a data frame (table) with 39 entries for 5 different variables, these are
  •   sequence with 39 different entries, i.e. 39 different sequence names, names are strings (" ")
  •   accn with 39 different entries, i.e. 39 different accession numbers, which are are strings (" ")
  •   habitat, coded as character (strings = " ") F, G, IFG
  •   site, coded as HA, KW, SO
  •   ht (= haplotypes in this dataset) which are coded as numbers (integers)

.. code:: r

  # shows first parts of a vector, matrix, table or data frame; handy to check large datasets
  > head(On_data)
                                   sequence       accn      habitat  site   ht
  1   KF293402_On_HA_F_048         KF293402       F         HA       3
  2   KF293403_On_HA_F_049         KF293403       F         HA       3
  3   KF293404_On_HA_F_050         KF293404       F         HA       3
  4   KF293405_On_HA_F_051         KF293405       F         HA       3
  5   KF293406_On_HA_IFG_053       KF293406       IFG       HA       4

.. code:: r

  # shows last parts of a vector, matrix, table or data frame; handy to check if (large) dataset is complete
  > tail(On_data)
  sequence                            accn            habitat              site     ht
  34 KF293498_On_UE_IFG_078           KF293498        IFG                  UE       30
  35 KF293503_On_UE_IFG_083           KF293503        IFG                  UE       30
  36 KF293505_On_UE_IFG_085           KF293505        IFG                  UE       20
  37 KF293506_On_UE_IFG_087           KF293506        IFG                  UE       20
  38 KF293508_On_UE_IFG_089           KF293508        IFG                  UE       30
  39 KF293509_On_UE_IFG_090           KF293509        IFG                  UE

**Graphics**

.. code:: r

  > par(mfrow=c(nrow,mcol))   # defines number of rows and columns to graph
  > par(mfrow=c(1,2)          # 1 row, 2 columns = 2 graphs next to each other → | |
  > par(mfrow=c(2,1)          # 2 rows, 1 column = 2 graphs above each other  → ==
  > par(mfrow=c(2,2)          # 2 rows, 2 columns = 4 graphs on one page

  > plot( ) 
  > title( "some title")      # adds a title to the first graph
  > boxplot(x,main="title")   # boxplot
  > hist()                    # histogram
  > plot()                    # scatterplot - or phylogenetic tree → plot.phylo( )

**Tables**

.. code:: r

  > table <- read.delim( )       # for tab-delimited files (sep="t\")
  > table <- read.csv( )         # for comma-delimited files (sep=",")
  > table <- read.txt( )         # for space delimited files (sep=" ")
  > table                        # returns an object named table, to check that your data was read in correctly
  > head( )                      # to check just the first rows
  > tail( )                      # to check just the last rows
  > table[1,3]                   # gives you the 1st ROW in the third COLUMN in object table
  > table[,1,4:10]               # shows you in COLUMN 1 the values of ROWS 4 to 10 in object table
  > table[,2,4:10]               # shows you in COLUMN 2 the values of ROWS 4 to 10 in object table
  > grep("A",habitat)            # shows you which ROWS have factor A (arable field) in object habitat
  > grep("8",site)               # as previous, shows you where you can find site 8 in table

**Phylogenetic packages**

.. code:: r

  install.packages("ape")
  library(ape)                  # instead of library( ) you can also use require( ), matter of taste
  install.packages("pegas")     # install.packages("picante")
  library(pegas)                # requires package picante
  install.packages("phangorn")                
  install.packages("seqinr")


.. thumbnail:: /_static/R.png
