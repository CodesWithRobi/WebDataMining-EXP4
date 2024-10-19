#### NAME: ROBINSON J

#### REG.NO: 212223040170

## Experiment-04: Implementation of Cluster and Visitor Segmentation for Navigation patterns

## DATE: 19/10/24

### AIM: To implement Cluster and Visitor Segmentation for Navigation patterns in Python.

### Description:

<div align= "justify">Cluster visitor segmentation refers to the process of grouping or categorizing visitors to a website, 
  application, or physical location into distinct clusters or segments based on various characteristics or behaviors they exhibit. 
  This segmentation allows businesses or organizations to better understand their audience and tailor their strategies, marketing efforts, 
  or services to meet the specific needs and preferences of each cluster.</div>
  
### Procedure:
1) Read the CSV file: Use pd.read_csv to load the CSV file into a pandas DataFrame.
2) Define Age Groups by creating a dictionary containing age group conditions using Boolean conditions.
3) Segment Visitors by iterating through the dictionary and filter the visitors into respective age groups.
4) Visualize the result using matplotlib.

### Program:

```python
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
```

### Output:

![output](https://github.com/user-attachments/assets/622a9f67-dd5c-4004-956c-f8fa0e1e84ff)


### Visualization:

```python
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
```

### Output:

![Visualization](output.png)

### Result:

Successfully implemented Cluster and Visitor Segmentation for Navigation patterns in Python.
