import threading
from bddhttp.before.server import server_ipv4, server_ipv6
from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox()
    context.server_ipv4 = server_ipv4
    context.server_ipv6 = server_ipv6
    context.th4 = threading.Thread(target=server_ipv4.serve_forever)
    context.th6 = threading.Thread(target=server_ipv6.serve_forever)
    context.th4.start()
    context.th6.start()


def before_feature(context, feature):
    pass

def before_scenario(context, feature):
    # if "browser" in feature.tags:
    #     context.browser.get("http://google.com")
    pass
    
def after_all(context):
    context.server_ipv4.shutdown()
    context.server_ipv6.shutdown()
