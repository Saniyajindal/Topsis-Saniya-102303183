# Topsis-Saniya-102303183

`Topsis-Saniya-102303183` is a Python library for solving **Multiple Criteria Decision Making (MCDM)** problems using the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**.

---

## Methodology

TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (best possible value) and the longest geometric distance from the negative ideal solution (worst possible value).

### Step-by-Step Implementation:

1. **Normalization**  
The decision matrix is normalized to scale all criteria to a common range using vector normalization.

2. **Weighting**  
The normalized matrix is multiplied by the weights provided for each criterion.

3. **Ideal Best & Ideal Worst**  
Ideal best and ideal worst values are identified based on impacts.

- Beneficial criteria (+): Higher value is better  
- Non-beneficial criteria (-): Lower value is better  

4. **Euclidean Distance**  
Distance of each alternative from the ideal best and ideal worst is calculated.

5. **Performance Score**  
Final TOPSIS score is calculated and alternatives are ranked.

---

## Installation

```bash
pip install Topsis-Saniya-102303183
```

---

## Usage

Run the package via command line as follows:

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

---

## Example

**Command:**

```bash
topsis data.csv "0.25,0.25,0.25,0.25" "+,+,-,+" result.csv
```

---

## Input Data (data.csv)

| Model | Storage | Camera | Price | Looks |
|------|--------|--------|-------|-------|
| M1 | 16 | 12 | 250 | 5 |
| M2 | 16 | 8 | 200 | 3 |
| M3 | 32 | 16 | 300 | 4 |
| M4 | 32 | 8 | 275 | 4 |
| M5 | 16 | 16 | 225 | 2 |

---

## Output Result (result.csv)

| Model | Storage | Camera | Price | Looks | Topsis Score | Rank |
|------|--------|--------|-------|-------|--------------|------|
| M1 | 16 | 12 | 250 | 5 | 0.534277 | 3 |
| M2 | 16 | 8 | 200 | 3 | 0.308368 | 5 |
| M3 | 32 | 16 | 300 | 4 | 0.691632 | 1 |
| M4 | 32 | 8 | 275 | 4 | 0.534737 | 2 |
| M5 | 16 | 16 | 225 | 2 | 0.401046 | 4 |

---

## Result Analysis

Based on the TOPSIS scores obtained:

- **Model M3** achieves the highest score (~0.69), making it the **Rank 1** choice.
- **Model M2** receives the lowest score (~0.30), placing it at **Rank 5**.

The graph below (generated in the accompanying Colab notebook) visualizes the performance scores:

- X-axis: Alternatives  
- Y-axis: TOPSIS Score  

![TOPSIS Score Comparison](image.png)

---

## License

MIT License
