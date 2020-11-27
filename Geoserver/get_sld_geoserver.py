from geoserver.catalog import Catalog

# Connect to Catalog, with REST URL, user and password
cat = Catalog("http://tethys.icimod.org:8080/geoserver/rest/", "admin", "mapserver109#")
globalsetting = Catalog("http://tethys.icimod.org:8080/geoserver/rest/settings[HTML]", "admin", "mapserver109#")
# layerlist = cat.get_layers()


print(globalsetting.status_code)
