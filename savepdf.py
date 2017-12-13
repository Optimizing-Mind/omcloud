from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plot
from scipy.misc import imread
import numpy as np

def plotText(title):
    in_file_name = 'saved_output.txt'
    with open(in_file_name, 'r') as infile:
        output = infile.read()

    font1 = {'family': 'serif',
            'color':  'darkblue',
            'weight': 'heavy',
            'size': 10,
            }

    font2 = {'family': 'serif',
             'color':  'blue',
             'weight': 'normal',
             'size': 8,
             'wrap': True,
             }
    plot.axis([0, 10, 0, 10])
    plot.text(0.3, 9, title, fontdict=font1)
    plot.text(0.5, 0.5, output, fontdict=font2, wrap=True)
    _setAxisVisible(False)

def plotImg(img_file_name):
    img = imread(img_file_name).astype(np.float32) / 255
    plot.imshow(img)
    # ax = plot.gca()
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    _setAxisVisible(False)

def _setAxisVisible(vis):
    ax = plot.gca()
    ax.get_xaxis().set_visible(vis)
    ax.get_yaxis().set_visible(vis)

def save_report_pdf(fname='saved.pdf'):
    pdfpage = PdfPages(fname)
    # plot.subplot(121)

    plotText("Report for Customer from OptMind")
    pdfpage.savefig(plot.gcf())
    plot.clf()

    # plot.subplot(122)

    plotImg("saved.png")
    pdfpage.savefig(plot.gcf())
    pdfpage.close()


if __name__ == '__main__':
    save_report_pdf()
