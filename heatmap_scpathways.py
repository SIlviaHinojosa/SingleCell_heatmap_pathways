import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_heatmap(csv_file, heatmap_title="Heatmap of Pathways by Cluster"):
    """
    Generates a heatmap from a CSV file with a specific structure.

    Parameters:
    - csv_file: Path to the CSV file.
    - heatmap_title: Title for the heatmap.
    """
    # Load the file with the first two rows as headers
    data_cleaned = pd.read_csv(csv_file, header=[0, 1], encoding='latin1')

    # Remove empty columns or undesired headers
    data_cleaned = data_cleaned.dropna(axis=1, how="all")

    # Combine header levels to simplify column names
    data_cleaned.columns = [' '.join(col).strip() for col in data_cleaned.columns.values]

    # Remove completely empty rows
    data_cleaned = data_cleaned.dropna(how="all")

    # Transform data into long (tidy) format
    tidy_data = pd.melt(
        data_cleaned,
        var_name="Cluster",
        value_name="Pathway"
    )

    # Filter rows where the pathway is NaN
    tidy_data_cleaned = tidy_data.dropna(subset=["Pathway"])

    # Create a binary presence table for pathways by cluster
    presence_table = tidy_data_cleaned.pivot_table(
        index="Pathway",
        columns="Cluster",
        aggfunc=lambda x: 1,
        fill_value=0
    )

    # Generate the heatmap
    plt.figure(figsize=(14, 16))
    sns.heatmap(
        presence_table,
        cmap="YlGnBu",  # Yellow-blue pastel color palette
        cbar_kws={'label': 'Pathway Presence (1=Present, 0=Absent)'},
        xticklabels=True,
        yticklabels=True,
        linewidths=0.5,  # Grid lines
        linecolor='gray'  # Grid line color
    )

    # Adjust labels and title
    plt.title(heatmap_title, fontsize=16)
    plt.xlabel("Clusters", fontsize=12)
    plt.ylabel("Pathways", fontsize=12)
    plt.xticks(rotation=90, fontsize=10)  # Cluster labels
    plt.yticks(fontsize=8)  # Pathway labels
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example usage:
# generate_heatmap("path_to_file.csv", "Custom Heatmap Title")
