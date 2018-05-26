

def input_parser(m):
    """
    Given length of sequences, load input data corresponding to this length.

    :param m: Length of sequences in the input.
    :return: tuple, containing:

        1. sequences_list: List of sequences in the input, parsed such that \
                           sequences_list[i] holds a list of integers that are the colors of this sequence.

        2. n_correct_vertices_list: List holding the number of correct vertices in each sequence in sequences_list.

    .. note:: This function assumes the existence of 'data/input_m.txt'

    .. todo:: find a better name for n_correct_vertices_list

    """

    print "Loading input..."
    with open('data/input_{}.txt'.format(m), 'r') as f:
        data = [line.rstrip() for line in f]
    sequences_list = [[int(i) for i in item[:m]] for item in data]
    n_correct_vertices_list = [int(item[m + 2]) for item in data]
    return sequences_list, n_correct_vertices_list
