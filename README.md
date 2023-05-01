# Giraphics
<p align="center">
  <img src="https://github.com/tghira16/GiraFix/blob/master/res/banner.svg?raw=true=250x" width="600" title="Giraphics">
  <br></br>
  <a href="https://pypi.org/project/giraphics/"><img src="https://img.shields.io/pypi/v/giraphics.svg?style=flat&logo=pypi" alt="PyPI Latest Release"></a>
      <a href="http://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/license-MIT-red.svg?style=flat" alt="MIT License"></a>

</p>

Giraphics is graphing and animation library designed to fast and simple to use. The library is inspired by [3b1b]'s [manim] library, but built independently.

## Features
Giraphics offers a wide range of features to make your graphing and animation experience as smooth and easy as possible. Here are some of the highlights:

- Easy-to-use syntax: Giraphics was designed with simplicity in mind, so you can focus on your ideas, not the code.
- Customizability: With Giraphics, you can customize every aspect of your graphs and animations, from colors and shapes to animation speeds and styles.
- LaTeX support: You can render LaTeX expressions with Giraphics, making it easy to add complex mathematical formulas to your visualizations.

## Installation
The core package can be installed with `pip`.

```
pip install giraphics
```

Basic graphing and plotting can be done without any other software, however, the following packages are required for full functionality.
* [librsvg]: Used to convert SVG to other image formats
* [ffmpeg]: Used to convert images into a video 
* [tex2svg]: Used to render LaTex

Individual packages can be installed for specific functionality, but installation of all packages is reccomended.
## Examples
Here are some example with what can be made with the `Giraphics`

### Animations

<table padding="0" border="0">
 <tr> 
 <td>
  <p align="center">
  <img src="https://github.com/tghira16/Giraphics/blob/2ee931665e40ac08abc7c3d5c1e786850b206071/Examples/TaylorSeriesSine.gif" width="405" title="Giraphics">
</p>
 </td>
  <td>
   <p align="center">
  <img src="https://github.com/tghira16/Giraphics/blob/3954109a0ce0ad0f6c1dd7b809207faeb3f10d79/Examples/SquareTransform.gif" width="405" title="Giraphics">
</p>
  </td>
 </tr>
  <tr> 
 <td>
     <p align="center">
  <img src="https://github.com/tghira16/Giraphics/blob/3954109a0ce0ad0f6c1dd7b809207faeb3f10d79/Examples/LinTrans02.gif" width="405" title="Giraphics">
</p>
 </td>
  <td>
  <p align="center">
  <img src="https://github.com/tghira16/Giraphics/blob/master/res/DoublePendulum.gif" width="405" title="Giraphics">
</p>
  </td>
 </tr>
 </table>
 
<!-- 

* Here is an example of the Sine series, every second we add a new term the Taylor expansion of Sine.
<p align="center">
  <img src="https://github.com/tghira16/Giraphics/blob/2ee931665e40ac08abc7c3d5c1e786850b206071/Examples/TaylorSeriesSine.gif" width="405" title="Giraphics">
</p>
* Here is a stationary phase approximation to a Quantum Anharmonic Oscillator. This particular approximation relies on evolving under classical evolution. 
The red curve represents numerical solution of Schroedingers equation, while the blue curve represents the approximation. Lines below the plot show where the grid gets evolved to. The approximation manages to get the expectation of the postion and the phase reasonably well.
![qho](https://github.com/tghira16/Giraphics/blob/9fadce9292134ad908eae19e52d6eb01a59e254d/Examples/QHO_kick_eigen22%20copy.gif)
 * This is the conformal map that takes `z -> z^2`.
 * 
 ![Conformal Map](https://github.com/tghira16/Giraphics/blob/3954109a0ce0ad0f6c1dd7b809207faeb3f10d79/Examples/SquareTransform.gif)
 * This is a linear transformation that visualised as a transformation of the grid.
 ![Linear Transformation](https://github.com/tghira16/Giraphics/blob/3954109a0ce0ad0f6c1dd7b809207faeb3f10d79/Examples/LinTrans02.gif)
 * This is a double pendulum with different initial conditions.
 ![Double Pendulum](https://github.com/tghira16/Giraphics/blob/master/res/DoublePendulum.gif)
 * This is a quantum quartic oscillator. 
 
 ![QCO](https://github.com/tghira16/Giraphics/blob/master/res/QuarticOscillator.gif?raw=true)
 * Lorentz attractor

 ![QCO](https://github.com/tghira16/Giraphics/blob/master/res/lorentz.gif?raw=true) -->

## Tutorial 
You can find the tutorial [here]

## Contribution
You can make pull requests.

## Issues 

* The cleanup option does not work in `Animation.develop()`
## License
Mit License

[ffmpeg]: <https://ffmpeg.org/>
[3b1b]: <https://github.com/3b1b>
[manim]: <https://github.com/3b1b/manim>
[librsvg]: <https://github.com/GNOME/librsvg>
[tex2svg]: <https://github.com/mathjax/mathjax-node-cli/blob/master/bin/tex2svg>
[plot]: <https://github.com/tghira16/GiraFix/blob/master/Examples/graph_example.py>
[complexplot]: <https://github.com/tghira16/GiraFix/blob/master/Examples/Complex_Function_Example.py>
[vectorfield]: <https://github.com/tghira16/GiraFix/blob/master/Examples/Vector_field_example.py>
[here]: <https://github.com/tghira16/Giraphics/blob/master/tutorial.md>
