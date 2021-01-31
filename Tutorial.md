# Tutorial 

## Plotting Graphs
### Basic Graphs
To create a graph we start by creating a `Graph` Object

```
g = Graph(width, height, xlim, ylim, filename, origin)
```
* The filename should have the format of svg.
 * `width` and `height` define the resolution of the `Graph` in pixels.
 * `xlim` and `ylim` sets the units of the graph from the centre to the edges in the x and y directions.
 * `origin` is a optional argument that defines the location of the origin relative to the centre of the graph
 
## Animations

### Basic Animations
We start by creating frame-by-frame animations. To do this we start by importing

```
from giraphics.animate.animation import Animation
```

Then we create the `Animation` object. This takes name, number of frames, width, height, xlim and ylim as positional arguments and frame rate and origin are optional arguments with defualt values of 60 fps and [0, 0].

We interact with object by writing to the `Animation.plate` which is an instance `Graph` object. Once we are done with a plate we 
call `press()`. Usually this all fits in a `for` loop and the iterate over time.  Finally we develop the animation by calling `develop()`. `develop()` has optional argument for `cleanup` which  removes the intermediate files. For exmaple,

```
A  = Animation('hello_world.mp4', xlim, ylim, width, height)
for t in range(frames):
    A.bg(colour="black")
    A.plate.draw_circle(x, y, t, colour="white")
    # Other features
    # .
    # .
    A.plate.press()

A.develop()
```









### Special Animations 