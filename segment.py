# Visitor segmentation based on characteristics
# read the data
import pandas as pd
import matplotlib.pyplot as plt
visitor_df = pd.read_csv("clustervisitor.csv")

# Mask of data for segmentation basically conditions
age_groups = {
    'Young': visitor_df['Age'] <= 30,
    'Middle-aged': (visitor_df['Age'] > 30) & (visitor_df['Age'] <= 50),
    'Elderly': visitor_df['Age'] > 50
}

# Perform segmentation based on characteristics (e.g., age groups)
for group, condition in age_groups.items():
    visitors_in_group = visitor_df[condition]
    print(f"Visitors in {group} age group:")
    print(visitors_in_group)

# Create a list to store counts of visitors in each age group
visitor_counts=[]

# Count visitors in each age group
for group,condition in age_groups.items():
    visitors_in_group=visitor_df[condition]
    visitor_counts.append(len(visitors_in_group))

# Define age group labels and plot a bar chart
age_group_labels=list(age_groups.keys())
plt.figure(figsize=(8, 6))
plt.bar(age_group_labels, visitor_counts, color='skyblue')
plt.xlabel('Age Groups')
plt.ylabel('Number of Visitors')
plt.title('Visitor Distribution Across Age Groups')
plt.savefig('output.png')
