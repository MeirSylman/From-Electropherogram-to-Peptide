import pytest
from Electropherogram_to_peptide_quiz import generate_random_peptide, is_allowed, aa_to_nucleotide_sequence, divide_into_kmers

def test_generate_random_peptide():
    peptide = generate_random_peptide(length=6)
    assert len(peptide) >= 3

def test_is_allowed():
    assert is_allowed('A') == True
    assert is_allowed('Z') == False

def test_aa_to_nucleotide_sequence():
    nucleotide_sequence = aa_to_nucleotide_sequence("A")
    assert nucleotide_sequence in ['GCT', 'GCC', 'GCA', 'GCG']

