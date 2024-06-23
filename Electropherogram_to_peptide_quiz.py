import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the translation table from amino acids to nucleotide codons
codon_table = {
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAT', 'AAC'],
    'D': ['GAT', 'GAC'],
    'C': ['TGT', 'TGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'H': ['CAT', 'CAC'],
    'I': ['ATT', 'ATC', 'ATA'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'K': ['AAA', 'AAG'],
    'M': ['ATG'],
    'F': ['TTT', 'TTC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'W': ['TGG'],
    'Y': ['TAT', 'TAC'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}


# Function to check if a letter is allowed
def is_allowed(letter):
    return letter.upper() in codon_table


# List of allowed amino acid letters
allowed_letters = list(codon_table.keys())


# Function to generate a random amino acid sequence
def generate_random_peptide(length=6):
    return ''.join(random.choice(allowed_letters) for _ in range(length))


# Function to convert an amino acid sequence to a nucleotide sequence
def aa_to_nucleotide_sequence(aa_sequence):
    nucleotide_sequence = ""
    for aa in aa_sequence:
        if aa == '*':  # Treat '*' as stop codon
            codons = codon_table['STOP']
        else:
            codons = codon_table.get(aa.upper(), ['NNN'])  # Use 'NNN' for unknown amino acids
        nucleotide_sequence += random.choice(codons)
    return nucleotide_sequence


# Function to plot the nucleotide sequence with smooth curves and low-quality signals
def plot_nucleotide_sequence(nucleotide_sequence, title):
    bases = ['A', 'T', 'C', 'G']
    colors = {'A': 'green', 'T': 'red', 'C': 'blue', 'G': 'black'}

    # Add low-quality signals at the beginning and end
    low_quality_length = 4
    nucleotide_sequence = ('N' * low_quality_length) + nucleotide_sequence + ('N' * low_quality_length)

    x = np.arange(len(nucleotide_sequence))

    fig, ax = plt.subplots()

    for base in bases:
        y = np.array([1 if nucleotide == base else 0 for nucleotide in nucleotide_sequence])

        if np.sum(y) > 0:
            # Add minor variability between true signals
            y = y.astype(float)  # Convert y to floating-point array
            y += np.random.normal(0, 0.05, len(y))

            # Ensure signals are not above 0.99
            y = np.clip(y, None, 0.99)

            # Spline interpolation for smooth curves
            spline = make_interp_spline(x, y, k=3)
            x_smooth = np.linspace(x.min(), x.max(), 300)
            y_smooth = spline(x_smooth)
            ax.plot(x_smooth, y_smooth, label=base, color=colors[base])

    ax.set_ylim(-0.1, 1.1)
    ax.set_yticks(np.linspace(0, 1, 5))
    ax.set_xlabel('Base Position')
    ax.set_ylabel('Signal')
    ax.set_title(title)
    ax.legend()
    ax.set_xticks(np.arange(len(nucleotide_sequence)))
    ax.grid(True)

    plt.show()


# Function to divide the nucleotide sequence into overlapping k-mers
def divide_into_kmers(nucleotide_sequence, k=5, overlap=3):
    kmers = []
    step = k - overlap
    for i in range(0, len(nucleotide_sequence) - k + 1, step):
        kmers.append(nucleotide_sequence[i:i + k])
    if (len(nucleotide_sequence) - k) % step != 0:
        kmers.append(nucleotide_sequence[-k:])
    return kmers


# Main function for user interaction
def main():
    print("Allowed letters (amino acids):", allowed_letters)

    while True:
        choice = input(
            "Do you want to enter an amino acid sequence or generate a random one? (enter/random): ").strip().lower()

        if choice == 'enter':
            while True:
                amino_acid_sequence = input("Please enter an amino acid sequence (minimum length 3): ").strip()

                # Check for allowed and unallowed letters
                allowed = [letter for letter in amino_acid_sequence if is_allowed(letter)]
                unallowed = [letter for letter in amino_acid_sequence if not is_allowed(letter)]

                if unallowed:
                    print(f"Error: The following letters are not allowed: {', '.join(unallowed)}")
                elif len(amino_acid_sequence) < 3:
                    print("Error: The sequence must be at least 3 amino acids long.")
                else:
                    break
            break  # Exit the outer loop after valid input is received

        elif choice == 'random':
            amino_acid_sequence = generate_random_peptide()
            break

        else:
            print("Invalid choice. Please enter 'enter' or 'random'.")

    nucleotide_sequence = aa_to_nucleotide_sequence(amino_acid_sequence)
    print(f"Amino Acid Sequence: {amino_acid_sequence}")
    print(f"Nucleotide Sequence: {nucleotide_sequence}")

    # Divide the nucleotide sequence into overlapping k-mers with a minimum k-mer length of 4
    kmers = divide_into_kmers(nucleotide_sequence, k=max(4, 5))

    # Plot each k-mer
    for idx, kmer in enumerate(kmers):
        plot_nucleotide_sequence(kmer, title=f'K-mer {idx + 1}')

    # Ask if the user wants to quit or start over
    while True:
        again = input("Do you want to quit or start over? (quit/start): ").strip().lower()
        if again == 'quit':
            print("Goodbye!")
            break
        elif again == 'start':
            main()  # Restart the main function
            break
        else:
            print("Invalid choice. Please enter 'quit' or 'start'.")


# Run the main function
if __name__ == "__main__":
    main()
