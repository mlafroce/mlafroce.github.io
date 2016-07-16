---
layout: post
title: Hello jekyll
description: A guide to install jekyll, create your new site, and host it.
tags: hello jekyll blog docker
---

Hello jekyll
============

Every time we learn a new programming language, framework, toolbox, or whatever,
we start with our classic greeting "Hello world!", so, how do we do a "hello *jekyll*"

Jekyll is a static site generator, a really nice one. It uses markdown for content generation, and I really love markdown!
So I decided to write this tutorial on how to start a new *github pages* site with Jekyll


Installing Jekyll
-----------------

You can install Jekyll in a few steps

{% highlight shell %}
sudo apt-get install ruby ruby-dev nodejs
sudo gem install jekyll
{% endhighlight %}

(Not) installing Jekyll
-----------------------

I was about to install Jekyll on my pc, but I didn't even have Ruby installed!
However, there is an official docker image with the server ready for running.
You can read instructions [here](https://github.com/jekyll/docker/wiki/Usage:-Running)
for downloading and running Jekyll server.

If you have never used Docker before, I'll post some docker tutorials and examples as soon as posible.


Creating a site from scratch
----------------------------

* If You are using docker, You can create a new blog structure with just one not so easy step:

{% highlight shell %}
$ docker run --rm --volume=$(pwd):/srv/jekyll jekyll/jekyll jekyll new <blog-name>
{% endhighlight %}

* If jekyll is on your system, just run

{% highlight shell %}
$ jekyll new <blog-name>
{% endhighlight %}

This command will create a new folder named *blog-name* with Jekyll basic structure.

### Docker command description

* *--rm*: remove container after execution

* *--volume=$(pwd):/srv/jekyll*: mount current working directory in container's /srv/jekyll (where the new blog will be created and hosted), replace *$(pwd)* with your custom path if desired.

* *jekyll/jekyll*: run the official docker Jekyll image

* *jekyll new blog-name*: run Jekyll command *new* to create the blog in /srv/jekyll (which is linked to $PWD)


### Site structure

As described in the [official site](https://jekyllrb.com/docs/structure/),
we will place our hello jekyll under *_posts* directory.

We should also edit the *_config.yml* configuration file at the site root.


### Themes

Theming a site from scratch it's a hard task, fortunately, there are many people who share their themes for free.
You can fork/clone/download many themes from [here](https://github.com/jekyll/jekyll/wiki/themes). For example, this blog uses Pahvel Markov's [Clean dark theme](https://github.com/streetturtle/jekyll-clean-dark).
If you are cloning a themed blog, remember edit _config.yml file.


Running the server
------------------

* If You are using docker, just start a new container with the default options:

{% highlight shell %}
$ docker run --rm --volume=<blog-path>:/srv/jekyll jekyll/jekyll
{% endhighlight %}

* If installed locally:

{% highlight shell %}
$ jekyll serve -s <blog-path> -d <build-path>
{% endhighlight %}

If -s (--source) is not provided, current dir is used as blog path.
If -d (--destination) is not provided, current dir is used as build destination (_site location)


Uploading to github pages
-------------------------

If you want to upload your site in github-pages, create a new repository named *username*.github.io (*username* will be your github user).
Create a .gitignore file in your site folder with the following content:

{% highlight text %}
_site
.sass-cache
.jekyll-metadata
{% endhighlight %}

Initialize a local repository, commit your changes and push them to your github repo:

{% highlight shell %}
git init
git add .
git commit -m 'initial commit comment'
git remote add origin <Remote URL>
git push origin master
{% endhighlight %}

Remember to configure your local URL and github URL in the _config.yml file when testing local and before pushing remote.
