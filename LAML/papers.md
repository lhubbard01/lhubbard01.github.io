---
layout: post
title: Papers
description: important papers and foundational descriptions and reviews
tile_id: mll
---
















I will try to synopsize all the papers listed with an expanding window once I figure out how those work, and when I have the time for each. 
Foundational Papers
These papers are some that I consider, likely among many others, as fundamentally important to defining modern machine and deep learning.
<section>
	<div class="content">
		<div class="inner">
			<dl>
				<dt><a href="http://www2.math.technion.ac.il/~pinkus/papers/neural.pdf">Multilayer Feedforward Networks with a Nonpolynomial Activation Function Can Approximate Any Function</a></dt>
				<dd>
					<p>Perhaps the foundational proof supplying reason for its tremendous and unprecedented interest.</p>
					<p>Perhaps similarly important but underrecognized, is this paper, <a href="https://arxiv.org/abs/1901.03429">On the Turing Completeness of Modern Neural Network Architectures</a> which demonstrates the capacity of internal dense representations for furnishing Turing completeness</p>
				</dd>
				<dt><a href="https://arxiv.org/abs/1406.2661">Generative Adversarial Networks</a></dt>
				<dd>
					<p>Foundationally important in highly complex generative distributions, achieved through a clever application of Game Theory. Specifically, two models compete against each other, through training towards different ends.  A generator creates data that a discriminator is tasked on discerning its either synthetic or true nature.  A generator aims to get better at tricking the discriminator, while the discriminator aims to minimize its error in its classification. Generative models are useful for many reasons, but to be succinct, they allow for data generation and dataset augmentation.  As neural networks require a data rich training regime, a scarcity of data yields an underdetermined system, thereby failing to be useful in generalization.  This space is notably teeming with research, and the state of the art is being improved daily.</p></dd>
				<dt><a href="https://www.ams.org/journals/jams/2016-29-04/S0894-0347-2016-00852-4/home.html">Sample Complexity of Testing the Manifold Hypothesis</a></dt>
				<dd><p></p></dd>
			</dl>
		</div>
	</div>
</section>

<section>
<div class="content">
	<header class="major">
		<h3>Newer Papers</h3>
	</header>
	<header class="major">
		<h4>Network Functional Qualities</h4>
	</header>
	<div class="inner">
		<dl>
			<dt><a href="https://arxiv.org/abs/1703.06114">Deep Sets</a></dt>
			<dd><p>This paper accomplished many impressives feats.  To give them context, let's describe what this paper attends to. To start, a set is a mathematical object that contains other pbjects. However, reardless of the way in which you order members of the set, the set is still the same set, i.e. the set as a whole is the same under any permutation of its constituent elements.  This is termed, unsurprisingly, permutation invariance. Neural networks have struggled in problem spaces where data are inordinal, i.e. to apply order to them would corrupt the nature of the data. A salient example is a point cloud. </p>
			<p>Deep sets induce permutation invariance on the tensors comprising the data of a set. The way it is done is actually very clever, and frustratingly obvious. Consider two networks, phi and rho.  Between them, there exists the output of phi and the entry to rho. At this location, all of their data are summed together into a single tensor. <a href="https://github.com/lhubbard01/DeepSets">Here</a> is my implementation of a deep sets network on mnist data, where one can sum together the numbers in images, and regress upon their label sum. This outperformed the state-of-the-art in 2017, beating LSTMs on their inference ability by an order of magnitude on unseen data! </p>
			<p>Not only does this paper introduce a simple mechanism thorugh which toi induce permutation invariance, it also proves that every network that has this quality must be able to be written in this form. </p></dd>
			<dt><a href="https://iclr.cc/virtual_2020/poster_Skey4eBYPS.html">Convolutional Conditional Neural Processes</a></dt>
			<dd><p>Here, the idea of permutation invariance is leveraged once more, in terms of it being the shoulder of a giant, so to speak. It is noted by the authors that while permutation invariance is useful, it applies to vectors in a vector space, but fails to capture translation invariance. Translation invariance is the ability to map to the same output, regardless of where the function is translated. Specifically, this is useful when considered in terms of Gaussian Processes or Conditional Neural Processes, where the latter's regression is entirely corrupted through the translation of the data. </p>
			<p>To solve this, the authors demonstrate that applying the same idea of invariance instead to function spaces offers this translation invariant behavior! There is a wildly robust in demonstration of this in the domain of face image generation in their video</p></dd>
			<dt><a href="https://iclr.cc/virtual_2020/poster_HJgpugrKPS.html">Scale-Equivariant Steerable Networks</a></dt>
			<dd><p>Consider the issue of the semantic embedding of an object. As one moves an object between an observer across a variety of physical distances, the observer maintains their capacity to accurately identify the object at all locations. This is a demonstration of equivariance. more to come on the diuscussion of this paper, as I have only watched thier video, which seemed very promising.</p></dd>
		</dl>
	</div>
</div>
</section>

