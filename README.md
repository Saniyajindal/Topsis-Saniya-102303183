# Topsis-Saniya-102303183

`Topsis-Saniya-102303183` is a Python library for solving **Multiple Criteria Decision Making (MCDM)** problems using the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**.

---

## Methodology

TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (best possible value) and the longest geometric distance from the negative ideal solution (worst possible value).

### Step-by-Step Implementation:

1. **Normalization**  
   The decision matrix is normalized to scale all criteria to a common range (0 to 1).  
   The formula used is vector normalization:  

   rᵢⱼ = xᵢⱼ / √(∑ xᵢⱼ²)

2. **Weighting**  
   The normalized matrix is multiplied by the weights provided for each criterion:  

   vᵢⱼ = rᵢⱼ × wⱼ

3. **Ideal Best & Ideal Worst**  

   - Beneficial Criteria (+): Max value is best  
   - Non-Beneficial Criteria (-): Min value is best  

4. **Euclidean Distance**  

   Sᵢ⁺ = √(∑ (vᵢⱼ − Vⱼ⁺)²)  
   Sᵢ⁻ = √(∑ (vᵢⱼ − Vⱼ⁻)²)

5. **Performance Score**  

   Pᵢ = Sᵢ⁻ / (Sᵢ⁺ + Sᵢ⁻)

---

## Installation

```bash
pip install Topsis-Saniya-102303183
