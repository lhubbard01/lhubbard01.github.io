---
layout: post
title: compiler notes
css: /css/prt.css
---

<h3 style="padding-left: 5px; margin-left: 25px; margin-bottom: 10px;"><u>Contents</u></h3>
<div class="Contents-Box" style=" margin-left: 15px; padding-left: 15px; border-radius:10px;background: #FFF; width: 40%; border-color: #999; border-style: solid; border-width: 3px; ">
<ul>
<li style="margin-left: 5px;"><a href="#opencv">OpenCV2 linking</a></li>
<li style="margin-left: 5px;"><a href="#FORTRAN-C">Fortran and C</a></li>
</ul>
</div>

<div id="opencv"> 
<h2 style="font-size:40px; "><strong><u>Compiling OpenCV2 C++</u></strong></h2>
</div>

The following content is taken from an earlier post I wrote on my OpenCV experience.  
That post is sort of home to my other OpenCV work, so [here](/2018-04-30-opencv) is the link.  
installing and getting opencv to work on my macintosh has proven to be far harder than I expected, but this will serve as a quick rundown for some concepts for those suffering from macos induced posix-masquerading hardship.
  use brew! homebrew will take care of a lot of the heavy lifting during install, and will update your linker in sudh a way that you can add the following in to your compilation commands
 
```
g++ $(pkg-config --cflags --libs opencv) *.cpp
    
or in the makefile
g++ $(shell pkg-config --cflags --libs opencv) *.cpp
```

&nbsp;&nbsp;&nbsp;&nbsp;I am a bit worried I will forget these commands, so I created the makefile version, which introduced its own unusual, but easily corrected problems.  
I can refer to this in the future, and it keeps my compilation process easy because I only need to create the compilation script once, instead of having to do it every time.  
&nbsp;&nbsp;&nbsp;&nbsp;Makefiles are their own beast, but I will include some stuff about them here as well.  
Using commands wrapped in () launches another shell process to execute those commands. Specifically, the $(pkg-config --libs opencv) command will launch a __sub-shell process__ which will run what is commanded and return some value.
  If preceded with '$' on the left side, it will be caught as a line-local variable.  
&nbsp;&nbsp;&nbsp;&nbsp;What is being done specifically for our command is the process returns a bunch of locations for file lookups.  '- -cflags' will specifically return '-I' include paths which basically means add these directories to the include-search-paths during compilation; 

<div style="border-bottom: solid; padding-bottom: 15px;">  </div>


<div id="FORTRAN-C">
<h2 style="font-size:40px; "><strong><u>FORTRAN called from C</u></strong></h2>
</div>

linking fortran against gcc is a bit difficult at first run on macos.
I have been able to finally do it though.  here is how it works. 
1. Find the location of your fortran compiler library (for me, it is the GNU Fortran, gfortran)
2. In your ~/.\*shrc, add 'export LIBRARY\_PATH="__location/of/gcc/libs:$LIBRARY\_PATH__"
3. `gcc -lgfortran` will call the lib linker for the compilation process.  
And that is it! Well for the linking against the fortran compiler. 
In order to actually call fortran from C you will need to follow a specific pattern, and compile the files in a specific way.  

<div style="background: #FFF; width: 45%; border-radius: 10px; margin-left: 10px; padding-left: 25px;">
<p style="margin-left:40px;"><strong><u>References</u></strong></p>
<ul>
<li><a href="https://computing.llnl.gov/tutorials/bgq/mixedProgramming2.pdf">C and FORTRAN reference</a></li>
<li><a href="https://orion.math.iastate.edu/keinert/lecture_notes/calling.pdf">C and FORTRAN reference, this one is even better</a></li>
</ul>
</div>


```c
void fortran_subroutine_(int *, double *, double *, int *);

int main()
{
	int i = 5, array_size = 3;
	double pi = 3.14159;
	double array_lf[] = {5.5, 6.6, 7.7};

	fortran_subroutine_(&i, &pi, array_lf, &array_size);
	return 0;
}
```

note the memory address usage. The array is already a pointer, so we don't need to pass in its address.
Note also the convention  in the name of the fortran function, there is an underscore following the last letter of the function name. 
Lastly, fortran subroutines will return the void pointer type to the c function.  
Our program should be written to type cast the returned value as needed.

```fortran
subroutine FORTRAN_SUBROUTINE(i,x,y,ny)
implicit none
integer :: i, ny
double precision :: x
double precision :: y(ny)

end subroutine FORTRAN_SUBROUTINE
```

Writing fortran subroutines might be useful, but even more useful is taking advantage of the already built subroutines. 
LAPACK is a great example.
The convetion for these is including a variable to write to in the function prototype's arguments.
Obviously, the subroutine will need to write to this location on its end.
Because these are all memory addresses, we can pass around the memory locations between compiled programs.


the makefile
```make
gcc -c file_name.c 
gfortran --ffree-form -c fortran_file_name.f
gcc -o call-fortran-from-c file_name.o fortran_file_name.o -lgfortran
```

we are using the GNU C compiler and the GNU FORTRAN75 compiler. 
I haven't tried it with other compilers, but the convention might be similar.


