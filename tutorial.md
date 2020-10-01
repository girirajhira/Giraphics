# Tutorial 
We will go into the workings of Graphics. 

Lets start with the basics of how Graphics works. Graphics is essentially something that automates writing an SVG. For every

The most basic example of Giraphics is the Graph object. Graph has a canvas which it applies all the features like curves, grids, axes etc.
Lets look at an example where the
```
width = 600
height = 600
xlim = 12
ylim = 10
G = Graph(width, height, 12, 10, 'firstgraph.svg')

G.bg(colour="black")

```
