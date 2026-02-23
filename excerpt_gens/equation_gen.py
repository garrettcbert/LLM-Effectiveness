import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (4, 1))
ax.text(0.5, 0.5, r'$\cos(\theta) = \frac{A \cdot B}{||A|| \times ||B||}$', fontsize=20, ha='center', va='center')
ax.axis('off')
plt.savefig('output/cosine_similarity_equation.png', dpi = 150, bbox_inches='tight')