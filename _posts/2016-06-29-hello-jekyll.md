---
layout: post
title: Hello jekyll
---

Hello jekyll
============

Every time we learn a new programming language, framework, toolbox, or whatever,
we start with our classic greeting "Hello world!", so, how do we do a "hello jekyll"

Jekyll is a static site generator, a really nice one. It uses markdown for content generation, and I really love markdown!
So I decided to write this tutorial on how to start a new *github* site pages with Jekyll


(Not) installing Jekyll
-----------------------

I was about to install Jekyll on my pc, but I didn't even have Ruby installed!
However, there is an official docker image with the server ready for running.
You can read instructions [here](https://github.com/jekyll/docker/wiki/Usage:-Running)
for downloading and running Jekyll server.

If you have never used Docker before, I'll post some docker tutorials and examples as soon as posible.


Creating the blog
-----------------

You can create a new blog structure with just one not so easy step:

    docker run --rm --volume=$(pwd):/srv/jekyll jekyll/jekyll jekyll new *<blog-name>*

This command will create a new folder named *blog-name* with Jekyll basic structure.

* *--rm*: remove container after execution

* *--volume=$(pwd):/srv/jekyll*: mount current working directory in container's /srv/jekyll (where the new blog will be created and hosted)

* *jekyll/jekyll*: run the official docker Jekyll image

* *jekyll new blog-name*: run Jekyll command *new* to create the blog in /srv/jekyll (which is linked to $PWD)


### Site structure

As described in the [official site](https://jekyllrb.com/docs/structure/), we will place our hello jekyll under *_posts* directory.

We should also edit the *_config.yml* configuration file at the site root.


Theming
-------

stuff....
