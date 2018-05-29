.. Sphinx185 documentation master file, created by
   sphinx-quickstart on Sat May 12 19:34:31 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Sphinx185's documentation!
=====================================
|

This documentation follows the solution of the 185th riddle from `Project Euler <https://projecteuler.net/problem=185>`_.

The goal of this piece is to help make `Sphinx <http://www.sphinx-doc.org/en/master/>`_ accessible and easy to use.

Feel as free as you can to copy, paste and change anything you see here.

|

The source code is available `here <https://github.com/DalyaG/Sphinx185>`_.

.. role:: pinktext

.. To make sure this is indeed colored pink, I added a .pinktext class to graphite.css

:pinktext:`Hope you find this useful!`

`@DalyaG <https://github.com/DalyaG>`_

|

OK Let's get to business:
*************************

|

.. maxdepth = 1 means the Table of Contents will only links to the separate pages of the documentation.
   Increasing this number will result in deeper links to subtitles etc.



.. toctree::
   :maxdepth: 1
   :name: mastertoc

   riddle_description
   run_euler_185_solver
   input_parser
   naming_utils
   ilp_manager
   conf



* :ref:`genindex`

|


.. TIP OF THE HOUR:
   The following command allows me to choose line breaks inside a "note" environment.
   Outside a special environment, i could use
   | vertical bars
   | to format lines
   | to my desire

.. |br| raw:: html

   <br />

.. topic:: How to use this for YOUR next project:

    * ``pip install sphinx``

    * Option 1: from the terminal, run ``sphinx-quickstart`` from the root of the project you wish to document, |br|
      and follow the suggestions of your choice from this tutorial. |br|
      (My advice: install sphinx inside a dedicated ``documentation`` folder, to keep your project from clutter)

    * Option 2: copy the ``documentation`` folder in this repository and make it a subdirectory in your local project, |br|
      and edit the relevant ``.rst`` files.

    * On any case, the way to add a page to your documentation, is by:

      #. Creating a ``.rst`` file for the function/module you wish to document |br|
         (you can use the templates supplied here), and

      #. Add the name of the ``.rst`` file to the ``toctree`` in ``index.rst`` |br|
         (the source code for this page).

    * After editing the files, run ``make html`` from inside the folder in which you installed sphinx. |br|
      (If you used "Option 2" above - this is the the ``documentation`` folder you copies) |br|
      (**TIP OF THE DAY**: actually, always run ``make clean html`` to clear sphinx cache and build from scratch)

    * To view locally - open the file ``documentation/_build/html/index.html`` in your browser, and enjoy the read :)

    * To share - you can use `GitHub Pages <https://pages.github.com/>`_ to host your documentation: |br|

      #. Copy the content of ``documentation/_build/html/`` into a new ``docs`` folder, under the root of the project.

      #. Create an empty file ``.nojekyll`` inside ``docs`` folder |br|
         (this tells GitHub Pages to bypass the default ``jekyll`` themes and use the ``html`` and ``css`` in your project)

      #. Push your changes to master branch.

      #. In your repository on GitHub, go to "Settings" -> "GitHub Pages" -> "Source" |br|
         and select "master branch /docs folder".

      #. Share your beautiful documentation site at ``https://<your_git_usrname>.github.io/<project_name>/``



|

.. topic:: Tiny disclaimer:

    As I enjoy Project Euler greatly, I was hesitant to publish my solution online.

    Yet, since I saw many similar solutions are already available, I decided the educational
    cause of this tutorial justifies the means.

    So all you Euler buddies out there - hope you share my view :)

|

This documentation was last updated on |today|.

|
|

This page was generated using this .rst code:
*********************************************

|

.. literalinclude:: index.rst
