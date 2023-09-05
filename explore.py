import matplotlib.pyplot as plt
plt.rcParams["axes.formatter.useoffset"] = False
plt.rcParams["axes.formatter.limits"] = (-1_000_000, 1_000_000)
import seaborn as sns

def plot_variable_pairs(df):
    """
    Accepts a dataframe as input and returns a plot and regression line for each pairwise relationship.

    """
    # Set the style of the plot
    sns.set(style="ticks")

    # Plot the pairwise relationships with regression line
    sns.pairplot(df, kind="reg")
    

    
def plot_categorical_and_continuous_vars(df, cat_vars, cont_vars):
    """
    """

    for cat_var in cat_vars:
        for cont_var in cont_vars:
            # Plot a boxplot of the continuous variable for each categorical variable
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=cat_var, y=cont_var, data=df)
            plt.title(f"{cont_var} by {cat_var}")
            plt.show()

            # Plot a histogram of the continuous variable for each categorical variable
            plt.figure(figsize=(8, 6))
            for cat in df[cat_var].unique():
                sns.histplot(
                    df[df[cat_var] == cat][cont_var], label=cat, alpha=0.5, kde=True
                )
            plt.title(f"{cont_var} by {cat_var}")
            plt.legend()
            plt.show()

            # Plot a swarmplot of the continuous variable for each categorical variable
            plt.figure(figsize=(8, 6))
            sns.catplot(data=df, x=cat_var, y=cont_var, kind='swarm')
            plt.title(f"{cont_var} by {cat_var}")
            plt.show()