# This file contains functions to work with cells in a matrix
import numpy as np
import pandas as pd

#This function takes in two AnnData objects, one for healthy cells and one for cystic fibrosis cells, and calculates the mean expression of each gene in both groups. It then computes the difference in mean expression between the two groups and returns a DataFrame with the results, sorted by the absolute difference in mean expression.
def gene_mean_difference(healthy, diseased):

    healthy_means = np.asarray(
        healthy.X.mean(axis=0)
    ).flatten()

    diseased_means = np.asarray(
        diseased.X.mean(axis=0)
    ).flatten()

    difference = diseased_means - healthy_means

    results = pd.DataFrame({
        "gene": healthy.var["Symbol"],
        "healthy_mean": healthy_means,
        "diseased_mean": diseased_means,
        "difference": difference,
        "abs_difference": np.abs(difference)
    })

    results = results.sort_values(
        "abs_difference",
        ascending=False
    ).reset_index(drop=True)

    return results

 #This function assists in getting eligible genes to research by taking in an AnnData object and a gene name, and returns the expression values for that gene across all cells. It first finds the index of the specified gene in the AnnData object, then retrieves the expression values for that gene. If the values are stored in a sparse matrix format, it converts them to a dense array before returning them as a flattened array.   
def get_gene_expression(adata, gene_name):

    gene_index = np.where(
        adata.var["Symbol"] == gene_name)[0][0]
    
    values = adata.X[:, gene_index]

    if hasattr(values, "toarray"):
        values = values.toarray()

    return values.flatten()
    
#This function calculates the difference in gene detection between healthy and diseased cells. It computes the proportion of cells in which each gene is detected (i.e., has a non-zero expression) for both healthy and cystic fibrosis groups, then calculates the difference in detection rates between the two groups. The results are returned in a DataFrame sorted by the absolute difference in detection rates.
def gene_detection_difference(healthy, diseased):

    healthy_detected = np.asarray(
        (healthy.X > 0).mean(axis=0)
    ).flatten()

    diseased_detected = np.asarray(
        (diseased.X > 0).mean(axis=0)
    ).flatten()

    difference = diseased_detected - healthy_detected

    results = pd.DataFrame({
        "gene": healthy.var["Symbol"],
        "healthy_detected": healthy_detected,
        "diseased_detected": diseased_detected,
        "detection_difference": difference,
        "abs_detection_difference": np.abs(difference)
    })

    results = results.sort_values(
        "abs_detection_difference",
        ascending=False
    ).reset_index(drop=True)

    return results