import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from get_similarity import PosSimilarity
import math_excerpt_gen as math_excerpt_gen
import llm_excerpt_gen as llm_excerpt_gen

ROOT = Path(__file__).parent.parent
EXCERPTS_DIR = ROOT / "excerpts"
OUTPUT_DIR = ROOT / "output"

desired_prompt = """
    You are Ted Chiang writing the secret chapter of Division By Zero. The chapter should be after Renee had discovered
    that 1=2. She is trying to rewrite the proof for the quadratic formula. Make sure it fits thematically in the
    story, and maintain Chiang's grammar and syntax style.
"""

llm_cache = EXCERPTS_DIR / "llm_excerpts.md"
math_cache = EXCERPTS_DIR / "math_gen_output.md"

if llm_cache.exists():
    gemini_excerpt = llm_cache.read_text()
    print("Using cached Gemini excerpt.")
else:
    print("Generating LLM output...")
    gemini_excerpt = llm_excerpt_gen.collect_llm_excerpts(desired_prompt)

if math_cache.exists():
    math_gen_excerpt = math_cache.read_text()
    print("Using cached math excerpts.")
else:
    print("Collecting Math excerpts...")
    math_gen_excerpt = math_excerpt_gen.collect_math_excerpts()

raw_chiang_text = (EXCERPTS_DIR / "raw_chiang_text.md").read_text()

similarity = PosSimilarity(gemini_excerpt, math_gen_excerpt, raw_chiang_text)

similarity_matrix = similarity.get_similarity_matrix()
labels = ['Gemini Output', 'Math Gen Output', 'Raw Chiang Text']
similarity_matrix_df = pd.DataFrame(similarity_matrix, columns=labels, index=labels)

similarity_matrix_df.to_excel(OUTPUT_DIR / "similarity_matrix.xlsx", index=True)
similarity_matrix_df.to_csv(OUTPUT_DIR / "similarity_matrix.csv", index=True)

sns.heatmap(similarity_matrix_df, annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title('Cosine Similarity Matrix')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "similarity_matrix_heatmap.png")
plt.close()
