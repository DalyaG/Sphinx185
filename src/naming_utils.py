

def s_star_index_node(i):
    """

    Given an index in the sequence, get the name of node corresponding to this index in s_star.

    :param i: Index in the sequence.
    :return: Name of node corresponding to this index in s_star.

    **Example:** ::

      s_star_index_node(3) = 's_star_3'

    .. The indented line above will appear as highlighted code.
    .. The "Example" will appear in bold.
    ..
       This comment and the one above will both not appear in the sphinx documentation.
    """
    return 's_star_{}'.format(i)


def index_color_node(i, c):
    """

    Given an index in the sequence, and a color, get the name of node who's index is i and color is c.

    :param i: Index in the sequence.
    :param c: Color, between 0 and 9.
    :return: Name of node corresponding to this index in s_star.

    **Example:** ::

      index_color_node(0, 9) = 'i_0_c_9'


    """
    return 'i_{}_c_{}'.format(i, c)

