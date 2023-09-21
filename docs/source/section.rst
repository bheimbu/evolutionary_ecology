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
- If you have ambiguous positions (indicated by letters that are not A, C, G, or T; highlighted in red), correct them manually according to the peak call of the sequence with the highest quality at this position. Please note that…

.. note::
  - Correcting the consensus sequence saves the change in both forward and reverse sequence
  - Correcting the base in the erroneous sequence (either forward or reverse) changes the consensus sequence, but saves the change only in the respective sequence


.. image:: /_static/geneious_4.png

.. note::
  The table below summarises the symbols used for ambiguous base calls.

.. image:: /_static/geneious_5.png

**9. After checking and correcting your sequences, export the consensus sequence (= a single sequence that is the combined product of all single sequences)**

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
- Or in a sequence editor like BioEdit (Windows), AliView (Mac) —> free software
- Or Geneious Prime —> commercial software

.. image:: /_static/geneious_11.png
