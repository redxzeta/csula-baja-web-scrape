import os
import requests


def folder_save(name):
    try:
        os.mkdir(os.path.join(os.getcwd(), name))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), name))


def image_save(folder_name, alt_name, src):
    domain = os.environ.get('DOMAIN')
    name = alt_name.replace(' ', '_').lower()
    with open(name + '.jpg', 'wb') as f:
        im = requests.get(domain + src)
        f.write(im.content)
