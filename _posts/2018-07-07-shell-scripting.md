---
layout: post
title: shell scripting
subtitle: use cases and minutiae
css: /css/prt.css
---

check out scripting in shell.
CURL is used pretty extensively and interfacing with it through cli is pretty freakin easy.
If you want to have, for example, a file get all of its new line characters striped away, and then passed in as a string to the curl argument on your command line, do something like this  
I wrote a python script that was bascially this.




flatten\_my\_file.py

```python
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_arugment("filename",type=str)
    filename = parser.parse_args().filename
      
	with open(filename,"r") as fl:
      with open("flattened_document.txt","w") as out:
        out.write(fl.read().replace(" ","").replace("\n",""))
```

push.sh
```shell
#!/bin/sh
python flatten.py $1
source ./flat.sh
curl "$2" 'server_location/"$3"' -d "$J" 
```
 
 flat.sh
```shell
#!/bin/sh
export J="$(cat flattened.txt)"
```  

So theres a lot thats going on here, but I think the python is pretty straight forward, so I am going to skip that part (Except for the "replaces" as opposed to the strip function... That's just the way that worked for spacing characters, and while it was kind of hacky, sometimes you need to get hacky)  
The second function is what is called by push.
The syntax here is extremely important.
First, the paraentheses wrapping 'cat flattened.txt' actually means ___fork this process___.
The _$_ outside means ___capture the output as a local variable___.
 The _quotations wrapping that whole command_ means, finally, ___it is a string type___.
 Notably, there is an important difference between _single_ and  _double_ quotes. 
Single quotes will treat the wrapped text as a _string literal_, while the double quotes will ___allow the function to be called and then have its output cast as a string___.
 After all of that, we export J to be used by our parent program.


push.sh calls our python function, which will always write to that specific file name.  
We want this for a deterministic interprocess communication. 
I haven't found a very nice work around for setting the output to an environment variable, but you can just catch the variable too.  
I was pretty bent on creating an environment variable because it's nice to know these things (which is also the reason I did an intercomm between python and bash scripting).  
Anyway, the final line is __using curl to push $J to a location using curl function $2 and final index location $3__.  
These numbers actually are command line arguments for a shell script, i.e., $1 corresponds to the first argument following the script name, $2, the second, and so on.
$0 is the file name, or it can be considered the zero-th command line argument. 
Anyways, it ends up working like a charm and is a pretty useful script given that it is the first one i have written.
 Unix gives you a lot to work with, so some of the interactions can be non intuitive while others make a ton of sense.  
The more you work with it, the easier it gets!
Anyway, hope you enjoyed. There are a ton of resources on the web.  If I come across any other weird combinations of unix stuff for a desired behavior, I'll be sure to share!


