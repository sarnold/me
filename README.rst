What is this thing?
===================

This repo contains the pelican sources used to generate all (static) content
for my developer blog site.  The output is essentially a bunch of html files
and a theme dir for style data, while the input defaults to ReStructuredText
source files, along with config, plugin, and theme data.

See the following upstream URLs for documentation and source:

* http://docs.getpelican.com/en/3.3.0/getting_started.html
* https://gist.github.com/josefjezek/6053301  (secondary)
* http://pirsquared.org/blog/pelican-tags-vs-categories.html
* https://github.com/getpelican/pelican-themes
* https://github.com/DandyDev/pelican-bootstrap3
* http://oncrashreboot.com/elegant-best-pelican-theme-features
* https://github.com/getpelican/pelican-blog

The content folder is both for static pages (content/pages) and time-ordered
posts, eg, blog/news articles (note the use of the term "article" in the docs).
The output folder (not tracked by git due to .gitignore) will contain the
static files, images, themes, etc, that will be uploaded to the web server
document root.

The current theme that I like so far is pelican-bootstrap3 - see the theme
readme file from DandyDev above for config options, features, etc (also the
primary pelican docs).  Clone it to get the latest updates::

  $ git clone https://github.com/DandyDev/pelican-bootstrap3.git

The current pelicanconf.py should point directly to the pelican-bootstrap3 dir.

ReStructuredText references
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* http://docutils.sourceforge.net/rst.html
* http://docutils.sourceforge.net/docs/ref/rst/roles.html

Markdown references
~~~~~~~~~~~~~~~~~~~

* https://daringfireball.net/projects/markdown/basics
* http://daringfireball.net/projects/markdown/syntax


Example Workflow for Adding/Modifying Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* cd into your local clone of source content
* clone a theme repository

  * all themes in `one repo`_ (submodules optional)
  * `single theme`_ for speed (mainly for CI)

* make your changes using your favorite editor

  * edit one of the static .rst files or add a new one -or-
  * make a new article file (using the default template, article_template.rst)

    + tags are the typical "cloud" so more is better (up to a point)
    + categories get menu entries, so think carefully about what you want

  * update/check the metadata and verify correctness
  * save your changes, check with "git diff", view with local server/editor
    (repeat as needed)
  * clean and build "pelican -s pelicanconf.py" (if errors, fix them and repeat)

.. _one repo: https://github.com/getpelican/pelican-themes
.. _single theme: https://github.com/sarnold/tuxlite_tbs

It actually goes pretty quick once you've done it a few times; not sure if
vi has an rSt mode, but ReText is a decent little gtk-based .rst editor with
a view mode (among other things).

Example commands
----------------

After making changes, generate output::

  $ pelican content -s pelicanconf.py

Command-line args override config options::

  $ pelican content -s pelicanconf.py -t tuxlite_tbs

Run builtin HTTP server to view ``output`` folder::

  $ pelican --listen

The Github pages workflow publish command::

  $ pelican --settings publishconf.py --extra-settings SITEURL='"https://sarnold.github.io/me"' FEED_DOMAIN='"https://sarnold.github.io/me"' --output output/ --theme-path tuxlite_tbs
