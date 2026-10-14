import math

BASE_CONSTANT = 81.5   # standard value of the formula (your text shows 8.15)


def gc_percent(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def melting_temperature(seq, na):
    return (BASE_CONSTANT
            + 16.6 * math.log10(na)
            + 0.41 * gc_percent(seq)
            - 600 / len(seq))


# --- Read and validate the DNA sequence ---
while True:
    S = input("Enter DNA sequence: ").strip().upper()
    if S and set(S) <= set("ACGT"):
        break
    print("Invalid sequence! Use only A, C, G, T. Try again.")

# --- Read and validate the Na+ concentration (in mol/L) ---
while True:
    try:
        na = float(input("Enter [Na+] in mol/L (e.g. 0.05): "))
        if na > 0:
            break
        print("Concentration must be greater than 0.")
    except ValueError:
        print("Please enter a number, e.g. 0.05")

# --- Results ---
print(f"\nSequence : {S}")
print(f"Length   : {len(S)} nt")
print(f"%GC      : {gc_percent(S):.2f} %")
print(f"[Na+]    : {na} M")
print(f"Tm       : {melting_temperature(S, na):.2f} °C")