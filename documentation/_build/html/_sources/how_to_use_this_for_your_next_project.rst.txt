How To Use This for YOUR Next Project :)
========================================
|


.. TIP OF THE HOUR:
   The following command allows me to choose line breaks inside a "numbering" environment.
   Outside a special environment, i could use
   | vertical bars
   | to format lines
   | to my desire

.. |br| raw:: html

   <br />


#. ``pip install sphinx``

#. Copy the ``documentation_template_for_your_next_project`` folder in this repository, |br|
   make it a subdirectory in your local project and rename it ``documentation``.

#. Edit ``conf.py`` by searching the pattern ``#CHNAGEME#`` inside the file and follow the instructions.

#. Edit ``index.rst`` by following the inline instructions.

#. To add a page to your documentation:

   #. Create a ``.rst`` file for the function/module you wish to document |br|
      (you can use the templates supplied here), and

   #. Add the name of the ``.rst`` file to the ``toctree`` in ``index.rst``.

#. In terminal, inside the ``documentation`` folder, run ``make html``. |br|
   (**TIP OF THE WEEK**: actually, always run ``make clean html`` to clear sphinx cache and build from scratch)

#. To view locally - open the file ``documentation/_build/html/index.html`` in your browser, and enjoy the read :)

#. To share - you can use `GitHub Pages <https://pages.github.com/>`_ to host your documentation: |br|

   #. Copy the content of ``documentation/_build/html/`` into a new ``docs`` folder, under the root of the project.

   #. Create an empty file ``.nojekyll`` inside ``docs`` folder |br|
      (this tells GitHub Pages to bypass the default ``jekyll`` themes and use the ``html`` and ``css`` in your project)

   #. Push your changes to master branch.

   #. In your repository on GitHub, go to "Settings" -> "GitHub Pages" -> "Source" |br|
      and select "master branch /docs folder".

   #. Share your beautiful documentation site at ``https://<your_git_usrname>.github.io/<project_name>/``

|

.. topic:: When updating your documentation:

    #. Delete everything in ``docs`` besides the ``.nojekyll`` file.

    #. Commit your changes.

    #. Copy the new content of ``documentation/_build/html/`` into ``docs``.

    #. Commit and push your changes.

    #. Wait a few minutes for your website on GitHub Pages to be updated.


:ref:`Return Home <mastertoc>`


|
|

This page was generated using this .rst code:
*********************************************

|

.. literalinclude:: how_to_use_this_for_your_next_project.rst