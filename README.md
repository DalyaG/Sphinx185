# Sphinx185
A [sphinx](http://www.sphinx-doc.org/en/master/) 
documentation helper, using the solution of 
[Problem 185 from Project Euler](https://projecteuler.net/problem=185) 
as a case study.


You can start your onboarding with sphinx by browsing 
[the documentation of this repository](http://htmlpreview.github.io/?https://github.com/DalyaG/Sphinx185/blob/experimentations/documentation/_build/html/index.html),
that has this landing page:

![Documentation Landing Page](../experimentations/data/LandingPage.png)

At the button of every page, you can find the source code 
that will help you generate cool documentation for your own project!

The tl;dr goes something like this:

1. `pip install sphinx`
2. Download the `documentation` folder from this repository into the local project you wish to document.
3. For each documentation page you with to generate, create a designated `.rst` file, following the templates provided in this repository.
4. In the file `<path to your project>/documentation/index.rst`, edit the `toctree` to include the files you created in the previous step.
5. In the terminal, inside the `documentation` directory, run `make clean html`.
6. Open in your browser the generated file `<path to your project>/documentation/_build/html/index.html` 
and enjoy your beautiful documentation!

If you have any suggestions and ideas, please let me know :)
