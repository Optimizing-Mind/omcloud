import Algorithmia
from Algorithmia.acl import ReadAcl, AclType
import matplotlib.pyplot as plot
import matplotlib.image as mpimg
from PIL import Image
import io
import argparse
from matplotlib.backends.backend_pdf import PdfPages

algo_path = 'maxkukartsev/testoptmind/f3e3e29d6e83c31bc0f078b1c1807ce9f0640458'

algo_paras = {"threshold": 1,
              "weights": [
                  [-0.008516], [0.001604], [0.009076],
                  [0.011881], [-0.010668], [0.00584],
                  [-0.007716], [0.002753], [0.003881]]}

def getClient(apiKey):
    # Create the Algorithmia client
    client = Algorithmia.client(apiKey)
    return client

def convert_uri_algo_data(algo_uri):
    ind = algo_uri.find('/.algo/')
    return 'data:/' + algo_uri[ind:]

def algo_post(client, algo_paras=algo_paras, algo_path=algo_path):
    algo = client.algo(algo_path)
    return algo.pipe(algo_paras).result

def _disable_axis():
    ax = plot.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

def plot_text_from_result(result, save=False):
    output = result["output"]
    if save:
        out_name = 'saved_output.txt'
        with open(out_name, 'w') as outf:
            outf.write(output)
    plot.text(.5, .2, output)
    _disable_axis()

def plot_image_from_result(client, result, save=False, show_img=False, show_plot=False):
    uri = result['files'][0]
    img_uri = convert_uri_algo_data(uri)
    if client.file(img_uri).exists() is True:
        img_bytes = client.file(img_uri).getBytes()
        img = Image.open(io.BytesIO(img_bytes))
        if save:
            img.save("saved.png")
        if show_img:
            img.show()
        if show_plot:
            plot.imshow(img)
    else:
        print ("No file exists:", img_uri)

    _disable_axis()



def save_pdf():
    pdfpage = PdfPages('saved.pdf')
    pdfpage.savefig(plot.gcf())
    pdfpage.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', help='API key for using Algorithmia service',
                        required=True)
    parser.add_argument('--api_path', help='API Path for using Algorithmia service')
    args = parser.parse_args()
    api_key = args.api_key
    api_path = args.api_path
    if api_path is None:
        api_path = algo_path
    client = getClient(api_key)
    result = algo_post(client, algo_path=api_path)
    print(result["files"])
    print(result["output"])
    plot_text_from_result(result, save=True)
    plot_image_from_result(client, result, show_img=True, show_plot=True)
    save_pdf()

if __name__ == "__main__":
    main()
