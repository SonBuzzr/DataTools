import requests
import json

workspace_url = 'http://tethys.icimod.org:8080/geoserver/rest/workspaces'

workspace_name = "watershed"
files = 'sld_file/'

headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
}

sld_headers = {
    'accept': 'application/vnd.ogc.sld+xml',
    'content-type': 'application/json',
}

auth = ("admin", "mapserver109#")

layer_list = []
style_list = []


def get_sld(*args):
    return requests.get(args[0], headers=args[1], auth=auth)


def get_request(*args):
    return requests.get(args[0], headers=args[1], auth=auth).json()


w_json = get_request(workspace_url, headers)
# print(json.dumps(r_json, indent=2))

# print("List of Workspaces:")
for workspace in w_json['workspaces']['workspace']:
    # print("-", workspace['name'])
    if workspace['name'] == workspace_name:
        layer_url = workspace_url + "/" + workspace_name + "/layers"
        # print(layer_url)
        l_json = get_request(layer_url, headers)
        # print(l_json)

        for layer in l_json['layers']['layer']:
            layer_list.append(layer['name'])
            # print(layer_url+"/"+layer['name'])

for layer in layer_list:
    detail_url = layer_url + "/" + layer
    # print(detail_url)

    style_json = get_request(detail_url, headers)
    # print(json.dumps(style_json, indent=2))
    default_style = style_json['layer']['defaultStyle']['name']
    index = default_style.find(':')
    style_name = default_style[index + 1:]
    style_list.append(style_name)

for style in style_list:
    # print(style)
    style_url = workspace_url + "/watershed/styles/" + style
    # print(style_url)
    sld_text = get_sld(style_url, sld_headers)
    print(sld_text.text)
    with open(files+style+'.sld', 'w')as f:
        f.write(sld_text.text)

