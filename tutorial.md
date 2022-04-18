# Tutorial 

## Plotting Graphs
### Basic Graphs

Essentially graphs are different Features that we apply to a svg. Features are things like backgrounds, axes, curves and shapes.
They are applied in the order they are called, we first apply the background then work our way up to the feaures we want on top. 
Once we are done we simply save the file.
 
To create a plot we start by creating a `Graph` Object

```
g = Graph(width, height, xlim, ylim, filename, origin)
```
* The filename should have the format of svg.
 * `width` and `height` define the resolution of the `Graph` in pixels.
 * `xlim` and `ylim` sets the units of the plot from the centre to the edges in the x and y directions.
 * `origin` is a optional argument that defines the location of the origin relative to the centre of the plot
 A schematic is shown below
 
 ![Banner](https://github.com/tghira16/GiraFix/blob/master/res/schematic.svg?raw=true=250x)

We may then start adding features to plot. 
* `Graph.bg()` adds a black background by default but takes and optional argument
`colour` that takes colour names or hexadecimal
* `Graph.plot(f)` takes a function `f` as input and plots it. It takes optional arguments for `colour`, `strokewidth` , `opac` (opacity)
and resolution `n`.
* `Graph.plot_points(X,Y)` is the sames as `plot()` except it plots the lists `X` and `Y`
* `Graph.scatter(X,Y)`  scatter plots the lists `X` and `Y`.
* `Graph.axes()` plots a set of x and y axes. It takes optional arguments of `colour`, `strokewidth`, `opac` and 
whether to add `arrows`.
* `Graph.grid()` adds grids to the plot. It takes optional arguments for `colour`,  `strokewidth`, `opac` and `grid_int` that
sets the number of grid lines horizontallly and vertically.

Once we are done adding features we save the plot with `Graph.save()` and if we want to display it in the browser we first save and then use `Graph.display()`. 

Here is an example,

```
from giraphics.graphing.plot import Graph


def func(x):
    return (x-3)*(x+2)*x*0.2

g = Graph(800,600,8,6, 'example1.svg')

g.bg()
g.grid()
g.axes()
g.plot(func)

g.save()
g.display()
```
#### Constructions

* rect
* circl
* line
* text 
* etc
## Fancy Graphs

The `FancyGraphs` class is an extension of the `Graph` class that adds automated special plots
like vectorfields, linear transformations, complex plots, density plots and histograms.

## Animations

### Basic Animations
We start by creating frame-by-frame animations. To do this we start by importing

```
from giraphics.animate.animation import Animation
```

Then we create the `Animation` object. This takes name, number of frames, width, height, xlim and ylim as positional arguments and frame rate and origin are optional arguments with defualt values of 60 fps and [0, 0].

We interact with the object by writing to the `Animation.plate` which is an instance of the `Graph` object. Once we are done with a plate we call `press()`. Usually this all fits in a `for` loop and the iterate over time.  Finally we develop the animation by calling `develop()`. `develop()` has optional argument for `cleanup` which  removes the temporary files. For exmaple,

```
A  = Animation('hello_world.mp4', frames, width, height, xlim, ylim)
for t in range(frames):
    A.plate.bg(colour="black")
    A.plate.draw_circle(x, y, t, colour="white")
    # Other features
    # .
    # .
    A.plate.press()

A.develop()
```



### Special Animations 

### Scenes

## 3D Graphing & Animation

## Giraphics+Jupyter
We can use `Gaph.jdisplay()` to display the graph in Jupyter and use `Animation.display` for videos.

Coming soon!
