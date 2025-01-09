import seaborn as sns
import matplotlib.pyplot as plt

# Example: Distribution of rent
sns.histplot(final_df['rent'], kde=True)
plt.title('Distribution of Rent')
plt.show()

# Example: Boxplot of rent by property type
sns.boxplot(x='type', y='rent', data=final_df)
plt.title('Rent by Property Type')
plt.show()
