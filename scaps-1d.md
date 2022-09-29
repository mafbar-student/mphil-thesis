# SCAPS-1D

[SCAPS-1D](https://scaps.elis.ugent.be) or SCAPS for short which stands for Solar Cell Capacitance Simulator (SCAPS-1D) is a programme that can carry out one-dimensional solar cell simulations. It was developed by Marc Burgelman, a professor at the Department of Electronics and Information Systems (ELIS) of the University of Gent, Belgium. All the details of the software can be found in the website. As of writing, the latest version is 3.3.10, and that is the version that I used in this research.

It is a competent simulation software with multiple features and has been employed many times in the field of solar cell research. Searching up the software on Google Scholar will turn up roughly 5000 papers. Originally, the software is used for only a few types of solar cells:

> The (sic) was originally programme is developed for cell structures of the CuInSe2 and the CdTe family. Recent developments make the programme now also applicable to crystalline solar cells (Si and GaAs family) and amorphous cells (a-Si and micromorphous Si).

But it has since been used for many different kinds of solar cells. For example, I use it to simulate perovskite solar cells (PSCs), to varying degrees of success. Because of the numerical approach towards simulation, you can simulate pretty much any kind of solar cell (provided you restrict it to one-dimensional structures) as long as you have each layer's parameters and values, which you can glean from the literature and experimentation. So here I will demonstrate some basic functions of the software, which you can learn from and pretty much conduct your own simulations. This is basically all I have done for the entirety of my research. If you learn what I wrote here, then you can do your own research too.

___

# The Basics, and Only the Basics

In general, the workflow of SCAPS-1D is quite simple. In the most basic sense, this is what you do:

1. Launch application.
2. Set the problem.
3. Give input parameters.
4. Set working conditions.
5. Specify the actions to be measured.
6. Run the simulation.

Now, I will give a rundown on the most basic things that you can do in SCAPS-1D to help you get it up and running and begin to simulate one solar cell. From that, you can then easily simulate loads of different kinds of solar cells. In fact, you can just search "SCAPS-1D" in Google Scholar, and you will see how many papers have employed this software.

It is really simple and if you follow it step-by-step, you should be to do one simulation and understand the basics of it by the end of this note. I will say though that this is *not* nearly an exhaustive and extensive list of all the available features with each and every setting; rather, this is just the way you can start using SCAPS-1D. Despite that, for me, all that I wrote here is enough to be able to publish at least one paper and complete my Master's dissertation.

___

## Interface

First, I shall talk about the SCAPS-1D interface. These are the *important* panels and option buttons that you will face when you run a simulation of any kind. 

### Interface - The Action Panel

### Interface - The Working Point

### Interface - The Action Point

### Interface - Solar Cell Definition Panel

### Interface - Layer Properties Panel

### Interface - Batch Set-up Panel

I place this panel here because typically, in a normal SCAPS-1D workflow, you would have finished inputting all of your values in the layer properties panel and have ensured everything is set correctly in the solar cell definition panel *before* you move into this panel. As the name suggests, this panel is for batch calculation; so you don't have to individually run every single configuration one-by-one, that would just be tedious.

When you open up the panel, it will have the "Add" button on the top left. Once you press it, several things will pop-up:

1. Layer
2. Parameter
3. From
4. To
5. Steps
6. Lin/Log settings

The Layer (1) is simply the layer on which you want to perform the calculation. The Parameter (2) is the specific parameter value of a layer like it's thickness, band gap, defect density, etc. The "From" and "To" (3-4) specify the minimum and the maximum value of your desired range. The Steps (5) determine how many data points you want to have, and I will include the formula to calculate the steps below. The Lin/Log settings determine whether the parameter require linear or logarithmic iterations. This is self-explanatory.

The Steps (5) can be calculated as follows:

$$ steps=\frac{to-from}{interval} $$

The interval is of course the difference between two data points. The bigger the interval, the more data points. What to put in the interval really depends on how smooth you want your graph to look like. In my experience, it always is more beneficial to use bigger intervals first, and then decrease the interval as you see fit. It's up to you though.

### Interface - Results Panel

##