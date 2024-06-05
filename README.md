# Project_from_Electropherogram_to_peptide

### Project Goals:

#### Practicing Electropherogram Reading, Sequence Assembly, and Translating Nucleotides to Peptides:
This code serves as a valuable tool for students in genetics and molecular biology to enhance their skills in interpreting and translating output files from sequencing experiments.

![Electropherogram](https://github.com/MeirSylman/Project_from_Electropherogram_to_peptide/blob/main/Chromatogram.jpg) 

*Electropherograme*

An [electropherogram](https://en.wikipedia.org/wiki/Electropherogram), a graphical representation of nucleotide sequences, is commonly used in DNA sequencing. By generating simulated electropherograms from known peptide sequences, users can practice reading these plots and understand the nuances of signal interpretation. Following successful interpretation of the electropherogram outputs, the nucleotide fragments need to be connected by finding overlapping bases—a step known as "[assembly](https://en.wikipedia.org/wiki/Sequence_assembly)." Since we obtain the complete DNA sequence, we can use the [genetic code](https://en.wikipedia.org/wiki/Genetic_code) to translate it into an amino acid sequence. Practicing this step teaches the usage and structure of the genetic code.

#### A Biologist's Game: Decoding the Message:
Beyond its educational utility, this code can be adapted into an engaging and educational game for biologists. In this game, participants receive electropherogram plots generated from a peptide sequence. The challenge is to decode these plots to uncover the original peptide sequence. To add an element of fun and intrigue, a conventional text can be used as the query peptide, encoding a secret message. The game not only tests their practical skills but also encourages teamwork, problem-solving, and a deeper understanding of molecular biology.

### Brief Code Plan:

- Users choose whether to input an amino acid sequence or generate a random one for self-practicing.
- The amino acid sequence is translated into a nucleotide sequence using the genetic code.
- The nucleotide sequence is divided into overlapping k-mers, resembling sequencing output.
- Each k-mer is plotted as an electropherogram, showing signal intensities for nucleotides.


