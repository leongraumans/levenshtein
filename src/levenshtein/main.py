import numpy as np

from typing import List, Union


def levenshtein(
    string_a: str, string_b: str, calculate_ratio: bool = False
) -> Union[int, float]:
    """Calculate the Levenshtein distance and ratio.

    The Levenshtein distance is a string metric for measuring the difference
    between two strings. If the calculate_ratio parameter is provided, the
    ratio of similarity between two strings is computed.

    The Levenshtein distance is computed using a matrix with distance costs.
    For all i and j, distance[i,j] will contain the Levenshtein distance
    between the first i characters of s and the first j characters of t.

    https://en.wikipedia.org/wiki/Levenshtein_distance

    :param string_a: String A
    :param string_b: String B
    :param calculate_ratio: Boolean to determine whether to return the distance
    or the ratio between the two strings, default is False

    :return: Distance or similarity ratio
    :rtype: int or float

    """
    # Make sure string_a and string_b are string types
    assert type(string_a) is str, "string_a must be of type str"
    assert type(string_b) is str, "string_b must be of type str"

    # Initialize matrix of zeros
    rows: int = len(string_a) + 1
    cols: int = len(string_b) + 1
    distance: np.ndarray = np.zeros((rows, cols), dtype=int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for j in range(1, cols):
            distance[i][0] = i
            distance[0][j] = j

    # Iterate over the matrix to compute the cost of deletions, insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if string_a[row - 1] == string_b[col - 1]:
                cost = 0  # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if calculate_ratio:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(
                distance[row - 1][col] + 1,  # Cost of deletions
                distance[row][col - 1] + 1,  # Cost of insertions
                distance[row - 1][col - 1] + cost,
            )  # Cost of substitutions

    if calculate_ratio:
        # Computation of the Levenshtein Distance Ratio
        ratio: float = ((len(string_a) + len(string_b)) - distance[row][col]) / (
            len(string_a) + len(string_b)
        )
        return ratio
    else:
        # This is the minimum number of edits needed to convert string a to string b
        return distance[row][col]


def calculate_distance(string_a: str, string_b: str) -> int:
    return levenshtein(string_a, string_b)


def calculate_similarity(string_a: str, string_b: str) -> float:
    return levenshtein(string_a, string_b, calculate_ratio=True)


def get_most_similar_in_list(
    string_a: str, list_of_strings: List[str], calculate_ratio: bool = False
) -> str:
    """Iterate over list and return string with the highest distance ratio."""

    assert type(list_of_strings) in (
        list,
        set,
    ), "list_of_strings must be of type list or set"

    set_of_strings = set(list_of_strings)
    max_score: float = 0.0
    succes_term: str = ""
    for term in set_of_strings:
        score = calculate_similarity(string_a, term)
        if score > max_score:
            max_score = score
            succes_term = term
    return succes_term
