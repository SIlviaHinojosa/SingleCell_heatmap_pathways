This script generates a heatmap visualizing the presence or absence of pathways across different clusters, based on a CSV file with a specific structure.

CSV File Requirements

The CSV file must meet the following conditions:

Headers:

The first two rows of the file represent hierarchical headers.

The first row contains the type of information (e.g., "Tumorales", "Macrophages", etc.).

The second row contains the cluster names (e.g., "Cluster 0", "Cluster 1", etc.).

EXAMPLE: 

Tumorales,                   Tumorales,                   Macrophages,
Cluster 0,                   Cluster 1,                   Cluster 2,
Non-alcoholic fatty liver disease, Hormone signaling,       Staphylococcus aureus infection,
Human papillomavirus infection,     Staphylococcus aureus infection, Systemic lupus erythematosus,
Vibrio cholerae infection,          Systemic lupus erythematosus,    Rheumatoid arthritis,
Th1 and Th2 cell differentiation,   Hematopoietic cell lineage,      Hematopoietic cell lineage,

Table Body:

Each row starting from the third contains the pathway names associated with the clusters.

Empty cells (“NaN”) indicate missing data.

How to Use the Script

Prerequisites

Make sure to have the following Python libraries installed:

pandas
seaborn
matplotlib

You can install them by running:
pip install pandas seaborn matplotlib
