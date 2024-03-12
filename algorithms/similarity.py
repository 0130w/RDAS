def jaccard_similarity(list1, list2) -> float:
    """ Compute the jaccard similarity between two lists
    Parameters:
        list1 (list): first list
        list2 (list): second list
    Returns:
        float: jaccard similarity
    """
    if list1 is None or list2 is None:
        return 0.0
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0.0