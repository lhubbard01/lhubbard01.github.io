---
layout: post
title: Code
description: resources and links to useful implementations, and explanations of framework basics
tile_id: mll
---




















<div class="content">
  <div class="inner">
    <header class="">
      <h3>A motivation</h3>
    </header>
  </div>
  <p>To start, let's motivate a couple of things.  Machine learning is obviously complicated. As a mathematical framework, it draws upon an electic set of fields that, through their specific insights and recombinations by innovation, endeavoring to automate the search of a hypothesis space and an algorithmic description of the ineffable.  To write out these solutions by hand would be wildly infeasible, let alone a suboptimal allocation of one's resources, to put it professionally. 
  This is obvious but let's consider why we are creating machine learning models in the first place.  We are automating insight and action for, typically, a specific problem or problem space. It should seem natural then that computational instructions are necessary to render this performance. </p>
  <p>Now, above is hopefully obvious. But given this is our operative paradigm, we should aim to make maintenance, readability, extensibily, and efficiency of implementation paramount considerations, only seconded by, of course, the model and its performance. To that end, adopting frameworks that leverage intuitive abstractions, that are well organized, that are quick to write in, and obviously, accomplish our task effectively are the main considerations that require attendance</p>
  <p>I will split this into many separate pages, mainly comprised of design suggestions and tutorials.</p>
  <p> For the time being, here is a useful construct I found while exploring an author's implementation, which I extended and repurposed for my own use cases. PyTorch is based on Lua, and many constructs from Lua have found their way over to implemntations in the python version of the framework. Note that PyTorch is not written in Lua. The original Torch had a Torch Netowrk package that contained, among other useful tools, the Engine.  I am sure the authors of the paper I was exploring, "Prototypical Networks for Few Shot Learning", did not have access to the Pytorch version of Engine, as the process of porting Torch was a bit long. After looking over both, I prefer their implementation due to its modularity. 
    At any rate, the runtime using this device is a lot cleaner and readable. I encourage checking it out.
  </p>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.0/styles/dracula.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.0/highlight.min.js"></script>
  <script>hljs.initHighlightingOnLoad();</script>
  <pre>
  <code>
"""This is a template extended from Jake Snell et al on their prototypical networks for one shot learning,
in turn inspired by Lua's Torch Network framework.
This utilizes a combination of assignable hooks and state machines to make training more modular
and readable.""" 
class Engine:
  def __init__(self, hook_cb):
    hook_names = ["on_start", "on_start_epoch", "on_forward", "on_sample",
      "on_backward", "on_end_epoch", "on_update", "on_end"]
    
    self.hooks = { }
      
    for hook_name in hook_names:
      self.hooks[hook_name] = lambda state: None
    for hook_name in hook_cb.keys():
      if hook_name not in self.hooks.keys():
        raise KeyValueError
      self.hooks[hook_name] = hook_cb[hook_name] 
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
  </code>
  </pre>
  <p> The above is useful in the context of training management through a potentially extensible framework, but is
  notably readable and uncluttered.  The <code>**kwargs</code> is a dictionary that is composed of runtime interpreted argument assignments, if you are unfamiliar. This is useful for keeping the method signature readable, but it comes at the cost of a decreased control over API definition.  At any rate, this collection of key word arguments is composed of parameters for the training runtime. One could opt for passing in a dictionary of hook callbacks at initialization time for the class, or assigning the hooks during setup.   
  </p>
  <p>Now, look at how useful this is!</p>
  <pre>
    <code>
    """... continued from earlier, we are in the scope of Engine.train"""
    self.hooks["on_start"](state)    #the state dictionary is passed around, carrying the state of the objects therein.
    while state['epoch'] < state['max_epoch'] and not state['stop']: #a stop state can be used to set exit conditions prematurely
      state['model'].train()
      self.hooks['on_start_epoch'](state) #note how your callback can handle the model or loader
      # in the state dictionary, allowing a modularized approach to handling logging and saving behavior

      for sample in state["loader"]:
        state["sample"] = sample
        self.hooks["on_sample"](state)
        state["optimizer"].zero_grad() #flush the stored gradients from the previous epoch

        loss, state["output"] = state["model"].loss(state["sample"]) # look how readable and modular this is, super useful
        self.hooks["on_forward"](state)

        loss.backward()
        self.hooks["on_backward"](state)

        state["optimizer"].step()

        state["t"]+=1
        state["batch"] +=1
        self.hooks["on_update"](state)

      state["epoch"] += 1
      state["batch"] = 0

      self.hooks["on_end_epoch"](state)

    </code>
  </pre>


  <p>This is useful through constructing a consistent training environment that has specific behaviors beyond vanilla implementations. Perhaps one could pass through the model to a specific hook given a certain condition met, handling a different set of activations or subnetwork, like an ensemble?</p> 

  <p>Here are the callbacks that were defined for the prototypical networks for few shot learning</p>





  
  <pre>
    <code>
def main(opt):
  """... skipping over all other stuff, just focusing on callbacks. note that they are defined in the scope of main
  so variables defined in main are accessible within these nested functions. opt is the command line parsed args"""
 
  engine = Engine() 
  def on_start(state):
    if os.path.isfile(trace_file):
      os.remove(trace_File)
    state['scheduler'] = lr_sceduler.stepLR(state['optimizer'], opt['train.decay_every'])
  engine.hooks["on_start"] = on_start

  def on_start_epoch(state):


    for split, split_meters in meters.items():
      for field, meter in split_meters.items():
        meter.reset()
    state["scheduler"].step()
  engine.hooks["on_start_epoch"] = on_start_epoch

  def on_update(state):
    for field, meter in meters["train"].items():
      meter.add(state["output"][field])
  engine.hooks["on_update"] = on_update

  def on_end_epoch( state):
    if var_loader is not None:
        model_utils.evaluate(state['model'],
          val_loader,
          meters['val'],
          desc="Epoch {:d} valid".format(state['epoch']))
    
    meter_vals = log_utils.extract_meter_values(meters)
    print("Epoch {:02d}: {:s}".format(state['epoch'], log_utils.render_meter_values(meter_vals)))
    with open(trace_file, "a") as f:
      json.dump(meter_vals, f)
      f.write('\n')
    state["model"].cpu()
    torch.save(state["model"], os.path.join(opt["log.exp_dir"], "best_model.pt"))
    if opt["data.cuda"]:
      state["model"].cuda()
  engine.hooks["on_end_epoch"] = on_end_epoch

  </code>
  </pre>
  <p>Obviously, it is up to your discretion on how to implement the callbacks, these are just useful starting points for how they may be used in practice.</p>

</div>



