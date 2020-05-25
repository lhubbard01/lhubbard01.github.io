---
title: Cloud
layout: post
description: A brief history of cloud computing
image: assets/images/office-building-pretty.png
show_tile_home: false
tile_id: cloudtech
---



























<div id="main">
<section id="one">
	<div class="inner">
		<header class="major">
			<h2>A nice start</h2>
		</header>
	</div>
</section>
<section id="two" class="spotlights">
	<div class="content">
		<div class="inner">
			<p><span class="image left"><img src="{{ site.baseurl }}{% link assets/images/office-building-pretty.png %}" alt="" /></span>
		The cloud refers to the relocation of data or services to remote hardware. For the novice readers in the space, we are all familiar with the software that runs on our computers locally, and perhaps how the internet works in general. We are also likely familiar with the meme-y trope of hackers in Hollywood films referring to mainframes. Mainframes were hardware that a company would run all of their business operations on.This includes both pre internet business activites and nascent or relatively early internet commerce.Pre-internet, the mainframe was where the business operations considering mathematically intensive business operations or data backups were done. 
			</p>
		</div>
		<section>
			<header class="major">
				<h3>The early days</h3>
			</header>
			<p>In the early internet phase, mainframes also were purposed as endpoints for serving customers or clients through web facing applications.  Because such activites are high throughput at peak usage, commonly referred to as peak demand, its hardware was relative to other contemporaneous computing technology, considerably more powerful, and consequentially more expensive.</p>
			<p> Here, there are two inefficiencies that were accepted as necessary.
				<strong>First</strong> was the hardware being purchased to handle peak demand.  This is likely obvious, as there are many real world analogs, but the following example provides a good motivation for cloud.</p>
				<p>Highways are often sparsely speckled with drivers in the middle of the night. However, highways may also be 5 lanes wide, which would look silly if the only commuter activity were to reflect that of midnight transit. Obviously, we know this not to be the case, as it instead is constructed to handle the demand of rush hour, where the majority of commuters all need to share the same road space to commute to work, since most people are expected to arrive at work at similar times.  There are two perspectives through which to view what comes next, and I will address both.</p>
				<p>If I had the ability to scale up and down my physical hardware to match that of my demand, I wouldnt have to have a wasted compute capacity.	 This efficiency is appealing financially, if we assume that the less computationally powerful hardware one has, the less it costs to use it. While physical highways are unable to change their shape to match that of current usage, computers arent limited by physical constraints. This useful term tightly associated with distributed systems now, was elasticity. One could scale a virtual and secure compute instance to match that of their demand!So, effectively, one could have a street turn in to a road, and then a super highway, and then back down again, all based on how much compute a customer needed!</p>
				<br/>
				<p>Secondly, a subscription charge based on usage is likely far cheaper than purchasing physcial hardware. Hardware can become obselete far faster than other technologies, so the recurrent purchasing of rapidly depreciating hardware as computing demands rose was a subpar allocation of financial resources, all other thigs consdiered.  Even worse, much of the compute power would be sitting idle during this depreciation!  To instead have to pay a consistent but cheap fee to outsource the physical hardware your business operations would run on would be far cheaper in the long run.  It seems obvious then why cloud has become such a ubiquitous influence in enterprise software operations.  In short, it just makes the most sense.</p>
	</section>
	<section>
		<header class="major">
			<h3>Better Than Back in my Day</h3>
		</header>
		<p>Now, there are many leaders in the field of not only provisioning remote compute resources, but also the software infrastructure other architectural comonents to enhance enterprise software operationality. 
			<a href="{{ site.baseurl }}{% link AWS.md %}">Amazon Web Services</a> is the most prominent player, whose offerings have expanded far beyond their intital offerings of <a href="https://aws.amazon.com">elastic</a> computing and <a href="https://aws.amazon.com/s3">large data storage(Simple Storage Service)</a>, as it now includes:</p>
		<br/>
		<a href="{{ site.baseurl }}{% link data-stores.md %}">Many database formats </a>
		<ul>
			<li><a href="https://aws.amazon.com/documentdb/">DocumentDB</a> document data store</li>
			<li><a href="https://aws.amazon.com/redshift">Redshift</a> (data warehouse, i.e. a large repository of unstructured data)</li>
			<li> <a href="https://aws.amazon.com/dynamodb">DynamoDB</a> (A document style datastore with NoSQL oriented behavior) )</li>
			</ul>
		<br/>
		<a href="https://aws.amazon.com/architecture">architectural components</a>
		<ul>
			<li> <a href="">SMS</a> and <a href="">SQS</a>, pub and sub respectively
			</li>
			<li><a href=""> Deployment pipelines </a>
			</li>
			</ul>
			<br/>
		  <a href="https://aws.amazon.com/business-applications">Tools for Business Applications and analytics</a>
		  <ul>
		  <li><a href="">Athena</a></li>
		  <li> <a href="">SageMaker</a></li>
		  </ul>
		  <br/>
		<p>alongside many, many more offerings. Some of the lessbusiness savvy may be wondering, why do these preconstructed tools exist with such a variety of abstraction and purpose?  It is simple, and it is distinct from common engineering intuition.  These are there simply to assist in business product agility. One thing that must be recognized is  those in business and those in engineering will find different products and services, and perhaps even goals appealing. For my engineering friends and engineering oriented readers, reflecting on the business use cases and applications will pay large dividends in discovering appeal for new services.</p>
		<p>The world of business has always been intrinsically competitive, and that competition has only been amplified through the pace at which the modern world can communicate. There are so many adversaries to compete against in the modern world of entrepreneurship and business in general, and as such, the ability to rapidly scale with minimal cost for infrastructural development is seen as leverageable advantage maker.</p>
		<p>Obviously, the further abstracted one is away from the codebase their application or operations run atop, the less ability there is to customize a platform for a specific use case.  However, because there is such a variety of demanded operational behaviors, start ups and large cloud providers have competed to offer tools they expect customers to find usefu.  Again, such an investment in time and talent for these products and services is thresholded by the potential payoff. </p>
		<p>If you are interested in exploring the modern idea and importance of data in the world of commerce and ecommerce, I will have a post <a href="{{ site.baseurl }}{% link data-and-business.md %} ">here</a> eventually.
		</p>
		<p>Also prominent players in cloud provisioning are Google Cloud Services and Microsoft Azure, both of which have many similar offerings, but considerably less developed than AWS who was one of the first players in the game of cloud.</p>
		<br/>
	</section>
	<section>
		<header class="major">
			<h3>Transformative for transformatives</h3>
		</header>
		<p>To give some context to how disruptive this has been, aasdfasdf Put asome numbers referring to successful start ups here asdfasdfa. Now, it is viable to create a software startup with orders of magnitude lower capital, specifically due to the now financially available tiers of computing power and the streamlined offerings of these comuting instances.</p> 
	</section>
</div>
