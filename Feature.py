# Group by 'property_id' and count interactions
interactions_df = pd.read_csv('property_interactions.csv')
total_interactions = interactions_df.groupby('property_id').size().reset_index(name='total_interactions')

# Merge the interactions with the property data
final_df = pd.merge(final_df, total_interactions, on='property_id', how='left')

# Show the final DataFrame with interactions
print(final_df[['property_id', 'total_interactions']].head())
