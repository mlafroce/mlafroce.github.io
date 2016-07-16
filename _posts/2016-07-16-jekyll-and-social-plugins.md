---
layout: post
title: Jekyll and Facebook
description: Configure Facebook plugins for social interaction.
tags: jekyll social facebook
---

Last week I wrote my first blog entry and showed it to some friends.
I had some feedback, but then I realised that I had no social plugins in my blog, so I had no comment section, or "Like" button, share, etc...

Today I'm going to write about social plugins, based on [this](https://joshuacox.github.io/jekyll/2015/11/28/facebook-comments-and-jekyll/) and [this](https://joshuacox.github.io/jekyll/2015/11/27/disqus-and-jekyll/) posts.

Facebook plugins
================

If you want to use Facebook plugins, first you need to create a developer account [here](https://developers.facebook.com/).

Login and click on "MyApps -> add new app". Select website, and choose a name for it.

Next, you have to add **Facebook SDK** to your website. Facebook quickstart guide shows how to add it in the body tag. Since this blog uses *jQuery*, I'm going to use a different approach by loading this small script after *jQuery*:

{% highlight javascript %}
$(document).ready(function() {
  $.ajaxSetup({ cache: true });
  $.getScript('//connect.facebook.net/en_US/sdk.js', function(){
    FB.init({
      appId: '<your app id>',
      version: 'v2.6',
      xfbml: true
    });
  });
});
{% endhighlight %}

Please note that *xfbml* option is not docummented, but is needed to display Facebook plugins

### OpenGraph meta tags

If you are going to use *Share* function, you may notice that your post metadata is missing and your post preview is meaningless.
To customize post metadata, use [OpenGraph meta tags](https://developers.facebook.com/docs/sharing/webmasters#markup)

Here is an example of what your *head* section should have

{% highlight html %}
{% raw %}
<meta property="og:url" content="{{site.url | append:page.url}}" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{{page.title}}" />
<meta property="og:description" content="{{page.description}}" />
<meta property="og:image" content="{{site.sharePreview}}" />
{% endraw %}
{% endhighlight %}
