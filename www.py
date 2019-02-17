import certifi
import urllib3


def fetch_html_page(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    response = http.request("GET", url)
    return response.data
