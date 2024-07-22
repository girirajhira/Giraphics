import giraphics.graphing.graph
from giraphics.graphing.figure import *
import numpy as np

### Default Settings

DEFAULTS = {
    'Background': {
        'colour': 'white',
        'opacity': 'opacity',
    },
    'Origin': [0, 0],
    'Plots': [

    ],
    'Grid': {
        'presence': False,
        'colour': 'grey',
        'opacity': .5,
        'x-grid': None,
        'y-grid': None,
    },
    'Legend': {
        'presence': False,
        'location': 'north east'
    },
    'Ticks': {
        'presence': True,
        'colour': 'black',
        'style': ''
    },
    'Title': {
        'presence': False,
        'text': '',
        'size': 10,
    },
    'xlabel': {
        'presence': False,
        'text': '',
        'size': 10,
    },
    'ylabel': {
        'presence': False,
        'text': '',
        'size': 10,
    }
}
t1 = {
    'X': [1],
    'Y': [2],
    'colour': 'black',
    'opacity': 1,
    'style': 'line',
    'label': '',
}


class Chart:
    def __init__(self, name, width=400, height=300, xlim=None, ylim=None, type='Figure'):
        self.name = name
        self.width = width
        self.height = height
        self.xlim = xlim
        self.ylim = ylim
        self.commands = DEFAULTS
        self.type = type
        ### Need to include border width

    def set_background(self, colour='white', opacity=1):
        self.commands['Background']['colour'] = colour
        self.commands['Background']['opacity'] = opacity

    def plot(self, X=[], Y=[], colour='black', opacity=1, style='line', label='', marker=None, markerSize=1):
        update = {'X': X, 'Y': Y, 'colour': colour, 'opacity': opacity, 'style': style, 'label': label,
                  'marker': marker, 'markerSize': markerSize}
        self.commands['Plots'].append(update)

    def xlabel(self, text, size=None):
        self.commands['xlabel']['presence'] = True
        self.commands['xlabel']['text'] = text
        self.commands['xlabel']['size'] = size if size is not None else .05 * self.width

    def ylabel(self, text, size=None):
        self.commands['ylabel']['presence'] = True
        self.commands['ylabel']['text'] = text
        self.commands['ylabel']['size'] = size if size is not None else .05 * self.width

    def title(self, text, size=None):
        self.commands['Title']['presence'] = True
        self.commands['Title']['text'] = text
        self.commands['Title']['size'] = size if size is not None else .1 * self.width

        # print(self.commands['Plots'])

    def grid(self, colour='grey', y_grid=None, x_grid=None, opacity=0.5):
        self.commands['Grid']['presence'] = True
        self.commands['Grid']['x-grid'] = x_grid
        self.commands['Grid']['y-grid'] = y_grid
        self.commands['Grid']['colour'] = colour
        self.commands['Grid']['opacity'] = opacity

    def complete(self):
        # Settings the limits
        if self.xlim == None and self.ylim == None:
            xmin_vals, xmax_vals = [], []
            ymin_vals, ymax_vals = [], []
            for data in self.commands['Plots']:
                xmax_vals.append(np.max(data['X']))
                xmin_vals.append(np.min(data['X']))
                ymax_vals.append(np.max(data['Y']))
                ymin_vals.append(np.min(data['Y']))
            xmax, xmin = np.max(xmax_vals), np.min(xmin_vals)
            ymax, ymin = np.max(ymax_vals), np.min(ymin_vals)

            xlim = (xmax - xmin) / 2
            ylim = (ymax - ymin) / 2
        elif self.xlim == None:
            xmin_vals, xmax_vals = [], []
            for data in self.commands['Plots']:
                xmax_vals.append(np.max(data['X']))
                xmin_vals.append(np.min(data['X']))
            xmax, xmin = np.max(xmax_vals), np.min(xmin_vals)
            xlim = (xmax - xmin) / 2
            ylim = self.ylim
        elif self.ylim == None:
            ymin_vals, ymax_vals = [], []
            for data in self.commands['Plots']:
                ymax_vals.append(np.max(data['Y']))
                ymin_vals.append(np.min(data['Y']))
            ymax, ymin = np.max(ymax_vals), np.min(ymin_vals)

            xlim = self.xlim
            ylim = (ymax - ymin) / 2
        else:
            xlim = self.xlim
            ylim = self.ylim

        # Creating the figure
        f = Figure(self.width, self.height, xlim, ylim, "f.svg", origin=[-(xlim + xmin), -(ylim + ymin)])
        f.ticks(markers=True)
        # Background
        f.bg(colour=self.commands['Background']['colour'])
        # Do grids

        # Plots
        for data in self.commands['Plots']:
            f.plot_points(data['X'], data['Y'], colour=data['colour'])
            if data['marker'] != None:
                f.scatter(data['X'], data['Y'], colour=data['colour'], opac=data['opacity'],
                          s=6 * data['markerSize'] / xlim)

        # Tile and labels
        if self.commands['Title']['presence']:
            f.title(self.commands['Title']['text'], self.commands['Title']['size'], )
        if self.commands['xlabel']['presence']:
            f.xlabel(self.commands['xlabel']['text'], self.commands['xlabel']['size'])
        if self.commands['ylabel']['presence']:
            f.ylabel(self.commands['ylabel']['text'], self.commands['ylabel']['size'])

        f.save()
        # f.display()


x = np.linspace(-5, 5, 100)
y = x * x
ch = Chart('s')
ch.plot(x, y, colour='red', marker='x')
ch.xlabel('x')
ch.ylabel('y')
ch.title('y = x^2')
ch.plot(x, y * x, colour='blue')
ch.complete()
