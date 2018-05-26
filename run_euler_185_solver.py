
from optparse import OptionParser

from src.ilp_manager import ILPManager
from src.input_parser import input_parser


def main():
    """
    Run this code to get the solution to 185th problem in Project Euler.

    Terminal options:

    .. option:: -m <sequence_length>, --sequence_length <sequence_length>

       Length of sequence in the riddle. Assume file 'data/input_m.txt' exists.


    """
    parser = OptionParser()
    parser.add_option("-m", "--sequence_length",
                      help="Length of sequence in the riddle. Assume file 'data/input_m.txt' exists.")
    options, _ = parser.parse_args()

    m = int(options.sequence_length)
    sequences_list, n_correct_vertices_list = input_parser(m)

    ilp_manager = ILPManager(m)
    ilp_solver, s_star_to_color_edges = ilp_manager.build_ilp_solver(sequences_list, n_correct_vertices_list)
    s_star = ilp_manager.solve_ilp(ilp_solver, s_star_to_color_edges)

    print "Solution is: {}".format(''.join([str(i) for i in s_star]))

if __name__ == '__main__':
    main()
