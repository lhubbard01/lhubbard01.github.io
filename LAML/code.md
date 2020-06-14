---
layout: post
title: Code
description: resources and links to useful implementations, and explanations of framework basics
---





















<div class="content">
	<div class="inner">
		<header class="">
			<h3>A motivation</h3>
		</header>
	</div>
	<p>To start, let's motivate a couple of things.  Machine learning is obviously complicated. As a mathematical framework, it draws upon an electic set of fields that, through their specific insights and recombinations by innovation, endeavoring to automate the search of a hypothesis space and an algorithmic description of the ineffable.  To write out these solutions by hand would be wildly infeasible, let alone a suboptimal allocation of one's resources, to put it professionally. 
	This is obvious but let's consider why we are creating machine learning models in the first place.  We are automating insight and action for, typically, a specific problem or problem space. It should seem natural then that computational instructions are necessary to render this performance. </p>
	<p>Now, above is hopefully obvious. But given this is our operative paradigm, we should aim to make maintenance, readability, extensibily, and efficiency of implementation paramount considerations, only seconded by, of course, the model and its performance. To that end, adopting framekworks that leverage intuitive abstractions, that are well organized, that are quick to write in, and obviously, accomplish our task effectively are the main considerations that require attendance</p>
	<p>I will split this into many separate pages, mainly comprised of design suggestions and tutorials.</p>
	<pre><code>
		"""This is a template extended from Jake Snell et al on their prototypical networks for one shot learning,
		in turn inspired by Lua's Torch Network framework.
		This utilizes a combination of assignable hooks and state machines to make training more modular
		and readable.""" 
		class Engine:
			def __init__(self):
				hook_names = ["on_start", "on_start_epoch", "on_forward", "on_sample",
					"on_backward", "on_end_epoch", "on_update", "on_end"]
				self.hooks = { }
				for hook_name in hook_names:
					self.hooks[hook_name] = lambda state: None

			def train(self, **kwargs): #explain **kwargs
				if not self.required_settings:
					self.required_settings = ["model", "loader", "optim_method", "optim_config", "max_epoch"]
				assert([option in kwargs.keys() for option in self.required_settings])

				state = {
					"model"         : kwargs["model"],
					"loader"        : kwargs["loader"],
					"optim_method"  : kwargs["optim_method"],
					"optim_config"  : kwargs["optim_config"],
					"max_epoch"     : kwargs["max_epoch"],
					"t"             : 0,
					"epoch"         : 0,
					"batch"         : 0,
					"stop"          : False
				}
				state["optimizer"] = state["optim_method"](state["model"].parameters(), **state["optim_config"])





