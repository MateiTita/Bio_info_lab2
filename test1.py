import matplotlib.pyplot as plt


def melting_temperature(seq):
    gc = seq.count("G") + seq.count("C")
    at = seq.count("A") + seq.count("T")
    return 4 * gc + 2 * at


# --- Read and validate the sequence from the keyboard ---
while True:
    S = input("Enter DNA sequence: ").strip().upper()
    if S and set(S) <= set("ACGT"):
        break
    print("Invalid sequence! Use only A, C, G, T. Try again.")

tm = melting_temperature(S)
print(f"Tm = {tm} °C")

# --- Count each base ---
bases = ["A", "C", "G", "T"]
counts = [S.count(b) for b in bases]
colors = ["#4CAF50", "#2196F3", "#FFC107", "#F44336"]

for b, c in zip(bases, counts):
    print(f"{b}: {c}")

# --- Draw the frequency chart ---
plt.bar(bases, counts, color=colors)
for i, c in enumerate(counts):
    plt.text(i, c, str(c), ha="center", va="bottom")  # number on top of each bar

plt.title(f"Base frequency of {S}  (Tm = {tm} °C)")
plt.xlabel("Nucleotide")
plt.ylabel("Count")
plt.show()