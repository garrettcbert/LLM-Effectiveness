import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.get_similarity import PosSimilarity
import src.math_excerpt_gen as math_excerpt_gen
import src.llm_excerpt_gen as llm_excerpt_gen

desired_prompt = """
    You are Ted Chiang writing the secret chapter of Division By Zero. The chapter should be after Claire had discovered \\
    that 1=2. She is trying to rewrite the proof for the quadratic formula. Make sure it fits thematically in the \\
    story, and maintain Chiang's grammer and sytax style. 
"""

gemini_excerpt = llm_excerpt_gen.collect_llm_excerpts(desired_prompt)
math_gen_excerpt = math_excerpt_gen.collect_math_excerpts()

with open('excerpts/raw_chiang_text.md', 'r') as f:
    raw_chiang_text = f.read()

similarity = PosSimilarity(gemini_excerpt, math_gen_excerpt, raw_chiang_text)

similarity_matrix = similarity.get_similarity_matrix()
similarity_matrix_df = pd.DataFrame(similarity_matrix, columns=['Gemini Output', 'Math Gen Output', 'Raw Chiang Text'], index=['Gemini Output', 'Math Gen Output', 'Raw Chiang Text'])

similarity_matrix_df.to_excel('output/similarity_matrix.xlsx', index=True)
similarity_matrix_df.to_csv('output/similarity_matrix.csv', index=True)

sns.heatmap(similarity_matrix_df, annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt.title('Cosine Similarity Matrix')
plt.tight_layout()
plt.savefig('output/similarity_matrix_heatmap.png')
plt.close()
