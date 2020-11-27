from sharepoint import SharePointSite, basic_auth_opener

server_url = 'http://sp.icimod.org/'

site_url = server_url + 'sites/icimod/kmc/pout/_layouts/FormServer.aspx?XmlLocation=/sites/icimod/kmc/pout' \
                        '/publication%20tracking%20system/1061.xml%3Fdefaultitemopen=1# '

opener = basic_auth_opener(server_url, "sambajracharya", "M3t@lica%^&")

site = SharePointSite(site_url, opener)

for sp_list in site.lists:
    print(sp_list.id, sp_list.meta['Title'])
