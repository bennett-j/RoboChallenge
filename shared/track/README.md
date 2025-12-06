# Working with SVG

SVG has been used to create the graphics for the racetracks. SVG is an XML based language and the graphics can easily be edited in a text editor. In Visual Studio Code (or similar), you might need to force it to open as text by right clicking to edit the SVG.

The racetrack requires large format printing. The sensing sheets are to be printed on A3.

## Converting to PDF

I suggest installing Inkscape (open source) and either using the GUI or the following CLI commands to convert to pdf.
```
inkscape racetrack.svg --export-type=pdf --export-filename=racetrack.pdf
inkscape sensing.svg --export-type=pdf --export-filename=sensing.pdf
```