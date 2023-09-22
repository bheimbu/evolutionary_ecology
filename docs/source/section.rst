.. _section:
Sections
========
 
.. _Geneious_Prime:
Geneious Prime
--------------
Geneious Prime is a molecular biology and sequence analysis tool, and helps you to organize data and projects in an efficient way.

.. note::
  It is important that the consensus sequences are of high quality (checked for sequencing errors or true heterozygosity) and that ambiguous positions are removed in order to infer correct phylogenies. Standard Sanger sequencing methods produce DNA sequences of ~700-900 bp long, however ~30 bp at the start/end of the sequence is usally of poor quality. This is due to primer deterioration, incorrect primer annealing, and/or aborted elongation, as well as technical limitations in accurately separating very short and very long DNA strands at the nucleotide level. To obtain high quality consensus sequences, it is common to sequence and assemble the forward and reverse strands of a PCR product. In this way it is possible to correct ambigous positions. Furthermore, by assembling forward and reverse sequences, the resulting consensus sequence is usually longer than any single strand, thus providing more phylogenetic information. Sequencing facilities normally provide raw sequencing data in .abi format (also known as DNA trace file). This file contains the DNA sequence electropherogram as well as raw data. The electropherogram (=chromatogram) shows the DNA trace during the sequencing process and can be viewed graphically. Most sequencing editors can open .abi trace files, such as BioEdit. However, most sequencing editors and analyses software that combine the DNA sequence and the chromatogram in a single analysis window, which considerably simplifies the processing of sequences, are commercial (e.g. Sequencher, CodonCodeAligner). Geneious Prime (Biomatters) provides a 30-day trial version, which we will use for analysing the sequences generated last week. You can download Geneious Prime `here <https://manage.geneious.com/free-trial>`_ and install it on your PC.

**1. Launch Geneious Prime**

**2. Create a new folder for your project**

**3. Drag and drop the .abi files from your explorer/finder into the sequence panel to import the sequence files**

.. image:: /_static/geneious_1.png

**4. Check out all single sequence files that belong to the same sample**

- For 18S there are 6 files (3 forward and 3 reverse)
- For 28S and COI there are only 2 (1 forward and 1 reverse)

**5. Assemble contigs**

- Select De Novo Assemble from the Align/Assemble menu
- (also: Tools —> Align/Assemble —> De Novo Assemble

.. image:: /_static/geneious_2.png

**6. Provide a name for the newly assembled sequence file**

.. attention::
  Never ever use special characters or white spaces!

.. image:: /_static/geneious_3.png

Now all single sequence files are pieced together (=assembled) and all complementary positions of all forward and reverse sequences are displayed underneath each other:

- You now have a .contig file (not a Sanger file or single nucleotide sequence), which is indicated by the icon in front of the name
- Scan the contig by eye to ensure that no ambiguous base calls are included 
- Geneious Prime automatically removes positions (base pairs) at the start/end of each sequence with a quality below a certain quality threshold (, which can be adjusted, if necessary)
- Positions that have been removed are indicated by a light pink bar underneath the respective sequence in the chromatogram
- If you have ambiguous positions (indicated by letters that are not A, C, G, or T; highlighted in red), correct them manually according to the peak call of the sequence with the highest quality at this position.

.. note::
  - Correcting the consensus sequence saves the change in both forward and reverse sequence
  - Correcting the base in the erroneous sequence (either forward or reverse) changes the consensus sequence, but saves the change only in the respective sequence

.. image:: /_static/geneious_4.png

.. note::
  The table below summarises the symbols used for ambiguous base calls.

.. image:: /_static/geneious_5.png

**9. After checking and correcting you sequences, export the consensus sequence (= a single sequence that is the combined product of all single sequences)**

- To export the consensus, see **Export Data**

.. image:: /_static/geneious_6.png

Export Data
^^^^^^^^^^^

**1. Use the default settings**

- Threshold: Highest Quality
- Assign Quality: Total

.. image:: /_static/geneious_7.png

**2. Select Format:**

- FASTA sequences/alignment (*.fasta)

.. image:: /_static/geneious_8.png

**3. Choose the destination**

.. image:: /_static/geneious_9.png

**4. Again, use default settings**

.. image:: /_static/geneious_10.png

**5. Now you can open the .fasta file in**

- Any text editor like Editor or Notepad++ (Windows), TextEdit (Mac), Notepadqq (Linux)
- Or in a sequence editor like BioEdit (Windows), AliView (Mac)
- Or Geneious Prime

.. image:: /_static/geneious_11.png

.. _Database_and_Search_Strategy:
Database and Search Strategies
------------------------------

Molecular sequence data is available from several online public databases, e.g. NCBI GenBank (USA), EMBL EBI (Europe), or DDBJ (Japan), to name a few. Providers manage and update entries daily via the World Wide Web. During this course, we use the service of NCBI GenBank to compare and validate our own sequence data and obtain additional sequences.

To screen the database for sequence data, two alternative search strategies are described below:
 
**1. Search the database for specific genes and taxa**

- Enter a species or higher taxon name in the search box. The order of search terms (e.g. 'oribatida d3') is neglible, as is the case sensitivity. However, it is important to limit the search to the required database, e.g., 'Nucleotide' or 'Protein'.

.. image:: /_static/database_1.png

**2. BLAST Search**

- Search for homologous genes using your own sequences.

.. image:: /_static/database_2.png

.. note::
  Again, it is important to limit the search to the required database within NCBI, e.g. 'Nucleotide' or 'Protein'.

You can upload your own sequences to the search mask (**see below**) either by copy-paste (**1a**) from a sequence editor like BioEdit or MEGA, or sequence files can be uploaded from a directory located on the hard drive (**1b**).
The BLAST search can be accelerated by limiting the search to an appropriate DATABASE (**2**, mandatory) and to a certain ORGANISM (optional). The search starts when pressing the „BLAST“-button (**3**).

.. tip::
  The accuracy of search parameters can be adjusted (Algorithm parameters; optional), which affects the degree of similarity of sequences from the database with your sequence data. Downscaling of search parameters can be helpful for searches within variable gene regions or among distantly related (or fast mutating) organisms. Upscaling of search parameters is reasonable when working with repetitive sequences.

.. image:: /_static/database_3.png

After starting a BLAST search a new window will open confirming the search request. The search is finished when a list with all results appears.

.. image:: /_static/database_4.png

.. note::
  When you click 'Back to Traditional Results Page' you will see a graphic that shows how your DNA fragment matches (aligns) with the BLAST results (**see below**). The graphic represents the complete length of the entered sequence, matching sequences from GenBank are listed below. The colour code illustrates the degree of similarity across the complete sequence and the mouse-over option enables quick assessment of results. When moving the mouse over the graph, names and genes of GenBank entries appear.

.. image:: /_static/database_5.png

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

.. image:: /_static/downloading_1.png

**1. Separate download of sequences from a list of search hits:**

- Tick the box left to the sequence you wish to save
- Go to 'Send to' (top right)
- Select 'Complete Record' (only visible for coding sequences)
- 'Choose Destination: File'
- 'Download 1 items: Format: FASTA'
- Select 'Create File', which saves the sequence to your hard drive

.. image:: /_static/downloading_2.png

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

.. image:: /_static/downloading_3.png

.. note::
  All sequences from the clipboard are now saved in a single file. Remember to change the file name from the default name (=sequences.fasta) to favouritename_favouritegene.fas.

.. tip::
  The Clipboard is a nice and easy way to collect and save large datasets from GenBank. However, if some sequences will be used in different datasets, they must be copied subsequently and saved separately.

.. hint::
  If you wish to download many sequences with continous accession numbers (e.g. from a paper), just enter the first and the last accession number separated by a colon `:` followed by the tag `[accn]`.
  
  .. code-block::
  
    EF091418:EF091227[accn]

.. _Bioedit:
BioEdit
-------

- Comfortable and easy editing of sequences and alignments
- Accepts most common file formats, most important formats for us are: ``.fas``, ``.aln``, ``.nex``, ``.txt``

.. image:: /_static/bioedit.png

**File**

- Open → each file opens in a separate window

- New Alignment

- Import → Sequence Alignment File → all files open in the same window > All Files `*.*` → choose to open ABI sequencing files

- Save As → ``.fas``


.. note::
  Most important features on the toolbar:
  
  - Title: `„name“.fas` → shows name of current file including directory path
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
 - FASTA-files work very well
 - Output file format for aligned sequences with file-extension `.aln`

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
  - The completed alignment opens in a new window, save it under a new name (e.g., `name_aln.fas` to point out that this file contains an already aligned dataset). You can select several file formats, the most common are `.fas`, `.txt`, and `.phy`
  - `.log` files of the alignment are saved to the folder BioEdit/temp; changes in the alignment can be traced there.
  - A `.dnd` file is generated in the same folder, containing a guide-tree, which is required for the alignment (a Neighbor Joining tree in Newick-format). The tree can be opened in `FigTree <http://tree.bio.ed.ac.uk/software/figtree/>`_, however, it is not a phylogenetic tree.

.. _Sequence_Editing:
Sequence Editing
----------------

.. note::
  File formats - some examples:
  
  Essentially, sequence data (protein and nucleotide sequences, alignments, etc.) are simple text files. They are edited in a specific format which is recognized by sequence editors and phylogenetic programs. Unfortunately, almost as many formatting styles as analyzing programs exist. Some of the most common editing styles (fasta and text for sequences, phylip and nexus for alignments) are listed here:

**Sequence files**

Example fasta (`.fas`) file

.. code:: text

  >Archegozetes_longisetosus_COI
  GGATCTTCACTG.....
  >Atropacarus_sp_COI
  GGAACTTCGTTA......
