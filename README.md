
# From Electropherogram to Peptide


### Goals:

#### Practicing Electropherogram Reading, Sequence Assembly, and Translating Nucleotides to Peptides:
This code serves as a valuable tool for students in genetics and molecular biology to enhance their skills in interpreting and translating output files from sequencing experiments.

![Electropherogram](https://github.com/MeirSylman/Project_from_Electropherogram_to_peptide/blob/main/Chromatogram.jpg) 

*Electropherograme*



An [electropherogram](https://en.wikipedia.org/wiki/Electropherogram), a graphical representation of nucleotide sequences, is commonly used in DNA sequencing.
By generating simulated electropherograms from known peptide sequences, users can practice reading these plots and understand the nuances of signal interpretation. Following successful interpretation of the electropherogram outputs, the nucleotide fragments need to be connected by finding overlapping bases—a step known as "[assembly](https://en.wikipedia.org/wiki/Sequence_assembly)." 

![assembly](https://github.com/MeirSylman/Project_from_Electropherogram_to_peptide/blob/main/Types_of_sequencing_assembly.png)

*Sequence asemmbly*




Since we obtain the complete DNA sequence, we can use the [genetic code](https://en.wikipedia.org/wiki/Genetic_code) to translate it into an amino acid sequence. Practicing this step teaches the usage and structure of the genetic code.

#### A Biologist's Game: Decoding the Message:
Beyond its educational utility, this code can be adapted into an engaging and educational game for biologists. In this game, participants receive electropherogram plots generated from a peptide sequence. The challenge is to decode these plots to uncover the original peptide sequence. To add an element of fun and intrigue, a conventional text can be used as the query peptide, encoding a secret message. The game not only tests their practical skills but also encourages teamwork, problem-solving, and a deeper understanding of molecular biology.


![quiz](https://github.com/MeirSylman/Project_from_Electropherogram_to_peptide/blob/main/quiz.png)

*Example quize*







### Brief Code structure:

- Users choose whether to input an amino acid sequence or generate a random one for self-practicing.
- The amino acid sequence is translated into a nucleotide sequence using the genetic code.
- The nucleotide sequence is divided into overlapping k-mers, resembling sequencing output.
- Each k-mer is plotted as an electropherogram, showing signal intensities for nucleotides.




### Instructions:

#### 1. **Install Dependencies:**

Use the following command to install the required dependencies:

```sh
pip install -r requirements.txt
```

#### 2. **Run the Program:**

To run the program, use the following command in your terminal:

```sh
python Electropherogram_to_peptide_quiz.py
```

- Choose if you want to *enter* your own amino acid sequence or to use *random* sequences.
- Save the outputs (figures, nucleotide & peptide sequences).

#### 3. **Run Tests with `pytest`:**

To run the tests, use the following command in your terminal:

```sh
pytest
```




This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04) at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) taught by [Gabor Szabo](https://szabgab.com/)

