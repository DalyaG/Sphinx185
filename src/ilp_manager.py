import pulp
from itertools import product

from naming_utils import s_star_index_node, index_color_node


class ILPManager(object):
    """Model the 185th problem in Project Euler as an ILP (Integer Linear Program)"""
    def __init__(self, m):
        """To instantiate this module, please specify the length on sequences."""
        self.m = m
        self.n_digits = 10
        self.optimal_status = 'Optimal'
        self.active_edge = 1.0

    def build_ilp_solver(self, sequences_list, n_correct_vertices_list):
        """

        Given input sequences, and number or correct vertices in each of them,
        build an ILP representation of the problem.

        :param sequences_list: List of sequences, each of length self.m, of integers between 0 and 9.
        :param n_correct_vertices_list: Number of correct vertices in each sequence in sequences_list. \
                                        A vertex is correct if its color is equal to the color of \
                                        the corresponding vertex in the solution s_star.
        :return: tuple, containing:

            * ilp_solver: Pulp instance, holding all the information needed for the solution.

            * s_star_to_color_edges: The edges (variables) in the ilp_solver.
        """
        print "Building ILP..."
        ilp_solver = pulp.LpProblem("ilp_solver", pulp.LpMinimize)
        s_star_to_color_edges = self._get_s_star_to_color_edges()
        ilp_solver += 0
        self._add_s_star_constraints(ilp_solver, s_star_to_color_edges)
        self._add_correct_vertices_constraints(ilp_solver, s_star_to_color_edges,
                                               n_correct_vertices_list, sequences_list)
        return ilp_solver, s_star_to_color_edges

    def solve_ilp(self, ilp_solver, s_star_to_color_edges):
        """

        Given a solver with the needed information, solve the ILP and extract the solution to problem 185.

        :param ilp_solver: Pulp instance, holding all the information needed for the solution.
        :param s_star_to_color_edges: The edges (variables) in the ilp_solver.
        :return: s_star: List of integers that is the solution to problem 185.
        """
        print "Solving ILP..."
        ilp_solver.solve()
        self._assert_optimal(ilp_solver)
        s_star = self._get_solution(s_star_to_color_edges)
        return s_star

    def _get_s_star_to_color_edges(self):
        s_star_to_color_edges = pulp.LpVariable.dicts("s_star_to_color_edges",
                                                      ((s_star_index_node(i), index_color_node(i, c))
                                                       for i, c in product(range(self.m), range(self.n_digits))),
                                                      cat="Binary")
        return s_star_to_color_edges

    def _add_s_star_constraints(self, ilp_solver, s_star_to_color_edges):
        for i in range(self.m):
            ilp_solver += pulp.lpSum(s_star_to_color_edges[s_star_index_node(i), index_color_node(i, c)]
                                     for c in range(self.n_digits)) == 1

    def _add_correct_vertices_constraints(self, ilp_solver, s_star_to_color_edges,
                                          n_correct_vertices_list, sequences_list):
        for i, s in enumerate(sequences_list):
            ilp_solver += pulp.lpSum(s_star_to_color_edges[s_star_index_node(i), index_color_node(i, s[i])]
                                     for i in range(self.m)) == n_correct_vertices_list[i]

    def _assert_optimal(self, ilp_solver):
        assert (pulp.LpStatus[ilp_solver.status] == self.optimal_status)

    def _get_solution(self, s_star_to_color_edges):
        s_star_unsorted = {i: c
                           for i, c in product(range(self.m), range(10))
                           if pulp.value(s_star_to_color_edges[s_star_index_node(i), index_color_node(i, c)])
                           == self.active_edge}
        s_star = [s_star_unsorted[i] for i in range(self.m)]
        return s_star


