---
layout: post
title: Page Frameworks
description: a page dedicated to all the stuff applied to accomplishing a more involved and hands on personal site
shorthand: blog
image: null
show_tile_home: true
---















<div id="main">
	<section>
		<header class="major">
			<h3>A Summary</h3>
		</header>
	<p>What started out as a disappointment with a bland aesthetic kind of evolved into something a lot more edifying and intensive than I originally intended and perhaps understood it could be when I started.
	</p>
	<p>I discovered not only the flexibility of the Jekyll framework (its a static site building tool, which they call also "blog aware"), but also some other powerful frameworks for streamlining dev for the internet front end. 
	</p>
	<p> SCSS, Jekyll, Liquid, bootstrap, etc, all tremendously useful for iterating over a seemingly intricate website.  Granted, a ground up development for all of the frameworks and the merrying of them to construct the page as is, would be. Thankfully, the open source community enjoys sharing what they can for building an app on the shoulders of giants. At any rate, I will try and do the development and debugging justice, and hopefully help others avoid the pitfalls I encountered along the way. </p>
</section>
<section>
	<header class="major">
		<h5>First: Jekyll</h5>
	</header>
	<p> Jekyll is a useful project tool for rendering a procedural and object oriented approach to html. the Liquid DSL developed and maintained by Shopify (I didn't know they actually built it! pretty cool).  Jekyll itself is built atop ruby, and I got to see some pretty nifty optimized ruby during my whole debugging endeavor with Jekyll. <strong>Turns out, github pages uses Jekyll 3.8.5 as of the time of this writing! Templates built atop Jekyll >= 4.0.1 may use an implicit relative path for asset fetching at build time!</strong>
	In order to solve this discrepancy, we must default to jekyll 3.8.5 and incorporate this style of path declaration for linking within the jekyll project. 
	{% raw %}
	 <code>
	 	\<img src="{{ site.baseurl }} {% link assets/images/pic01.jpg %}" \/>
	 </code>
	{% endraw %}
</p>
<p>Using jekyll >=4.0.1 can implicitly include the site.baseurl tag, so only the link portion is required when writing the resource into your document.  This caused some confusion during a couple of slightly upsetting debugging sessions, but github pages has their reasons for not including the most recent version into their gem.
</p>
<p>Another cool part of the jekyll framework is the builtin reusability of html snippits.  The framework is built around a general structure, and build behaviors are related through the _config.yml file. </p>
<p>The file structure for a Jekyll project expects the following</p>
<div class="inner">
	<h3>File Structure</h3>
	<dl>
	<dt>_include</dt>
		<dd> 
			<p>This contains portions of html that can be referenced from either a specific layout extension (like even your own post through markdown!) or the files contained in the layout folder</p>
		</dd>
	<dt>_layout</dt>
	<dd>
		<p>Entire pages that can be referred to inside the <strong>front matter</strong> of pages or other layouts.  This sort of constitutes an inheritance pattern for html, which is obviously very useful if you are using a consistent style for your website </p>
	</dd>
	<dt>_posts</dt>
	<dd>
		<p>Files with a naming format corresponding to a user defined string pattern. Beautiful jekyll, my previous blog framework of choice, used a %yyyy-%mm-%dd-.*\.md pattern, which would correspond to the order it was displayed in the blog. This corresponds to the year, month, and day it was posted, and then a unique name, relative to the project, of your choosing.  Inside this websites structure, I opted to have a separate page dedicated to blog posts, which can be found <a href="{{ site.baseurl }}{% link all_posts.md %}">here</a></p>
	</dd>
	<dt>_sass</dt>
	<dd>
		<p>A pretty useful streamlining object oriented approach to CSS, insofar as inheritance is applicable to classes and ids</p>
	</dd>
</dl>
</div>
</section>
<section>
<p> <strong> should be in another section</strong> Notably, you can also iterate locally over different site generations via bundler. I was pushing my updates to my github page on a per iteration basis, and the commits applied were distractingl superfluous. This ability to locally test is super useful, and I encourage at least two branchs for development, namely one in which jekyll options and bundler gems can be built around a localhost server, 	and one for the actual github pages or other site hosting.</p>
<p>An obvious further extension of liquid could also be applied via the similar python oriented html framework, using it as a preprocessing step before being fed into jekyll.  I might plan on doing that? It really depends on how useful I can find it being, if I run into any pitfalls. </p>
</section>
<section>
	<header class="major">
		<h4>The Pleasant Ease of _include</h4>
	</header>
	<p>Let's say you have a useful component you would like to reuse across many pages, and writing it is kind of an involved task. This was the case for my extension of the "tiles.html" component, itself similarly laborious. </p>

{% highlight html %}
	{% raw %}
	{% assign tiles = site.html_pages %}
	<section id="one" class="tiles">
		{% for tile in tiles %}
		{% if tile.tile_id == include.content %}
		<article>
			<span class="image">
				<img src="{{ tile.image }}" alt="" />
			</span>
			<header class="major">
				<h3><a href="{{ tile.url | relative_url }}" class="link" >{{tile.title}}</a></h3>
				<p>{{ tile.description}}</p>
			</header>
		</article>
		{% endif %}
		{% endfor %}
	</section>
{% endraw %}
{% endhighlight %}
</section>
<br/>
<section>
	<div class="inner">
		<header class="main">
			<h3>An explanation</h3>
		</header>
		<p>This itself is actually a useful bit of extend Liquid for incorporating a pretty tile pattern of windows and pictures that link elsewhere in the site. The {% raw %}<code>{% assign tiles = site.html_pages %} </code>{% endraw %} statement interfaces with a site object that corresponds to the ruby underlying the coordination of rendering the liquid and html and other components into a self contained static website. The object comes with its pages it is in charge of, which each have their own attributes, defined in their <a  target="_blank" rel="noopener noreferrer"  href="https://jekyllrb.com/docs/front-matter/">front matter</a>, and further defined in the project's corresponding _config.yml file.  Since Liquid is not too powerful of a DSL, and its original usecase was for streamlining webistes for Shopify's customers and theose customers' respective developers, there are some shortcomings associated with it. But its too easy to forget just how convenient Liquid is as a web building html extension! I find it has a relatively shallow learning curve, and the customization that can come along with it absolutely makes it a worthy use of time for any developer working with easy web projects.</p>
		<p>The next line of Liquid is a pretty self explanatory for loop. But after that, we see some useful content. 
			{% raw %}<code>{% if tile.tile_id == include.content %}</code>{% endraw %} is a way to relate the calling page's passed in parameter to the include <a  target="_blank" rel="noopener noreferrer"  href="https://shopify.github.io/liquid/basics/introduction/#tags">tag</a> that allows for a user specified parameterization of included html components! Here, I used this to specify which class of posts or pages I would like to include in the tile to be generated. The calling page would simply use {% raw %}<code>{% include tile_id.html content="cloud tech" %}</code>which would then correspond to this behavior in the liquid runtime <code>{% if tile.tile_id == "cloud tech" %}</code> which would then let me render only the pages containing the content I designate.{% endraw %} This is obviously super convenient, since now I don't have to write each portion of my page individually, but I can instead offload that to a loop to generate the html, since I already have created the organization of the markup and css I desire for this portion of the document.</p>
			<br/>
			<br/>
			<p>The rest of it is pretty self explanatory, save for the <code>|</code> syntax.  This is a <a  rel="noopener noreferrer"  target="_blank"  href="https://shopify.github.io/liquid/basics/introduction/#filters">filter</a>, which is a mutation on the data being referred to, with the corresponding transformation referenced on the right side. Usefully, filters can be strung together, so we can consider the leftmost as our originall input to this set of data transformations</p>
			<p>If you refer to the <a  target="_blank" rel="noopener noreferrer" href="https://github.com/lhubbard01/lhubbard01.github.io">github repo for this project </a> you can explore the _include and _layout directories for fruther examples of how the templates interface with each other and contribute to the eventual generated site.</p>
		</div>
	</section>
	<section>
		<p>One of the most useful additions to the web development toolset I discovered through this redesign was SCSS, or rather, SASS. It streamlines a ton of unnecessary overhead in design, mapping it to useable CSS after compilation. </p>
		<ul>
			<li>It is useful from letting variables abstract away complex CSS that would otherwise be unwiedly.</li>
			<li> It also supports nesting of elements in their definition.</li>
			<li>Partials, akin to <code>/_include/</code>'s from the Jekyll project template</li>
			<li>It is also modular! </li>
			<li>It allows for "functions" of sorts, termed "mixins"</li>
			<li>Inheritance!</li>
			<li>It even lets you perform computations to adjust visual parameters, i.e. their operators compute values before being rendered.</li>
		</ul>
		<p>The syntax necessary to employ these features are trivial to get up to speed with. This will be included further down the page, or perhaps on a separate page if I end up describing the stuff involved with this site more deeply.</p>
	</section>
</div>