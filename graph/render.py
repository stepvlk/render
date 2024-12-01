from pyvis.network import Network
from config.config import config
import functions.mongo_api as Mongo
import datetime

class Networks():
    def generate_graph(query):
        ts = int(datetime.datetime.now().timestamp())
        if config['server']['db'] == "LiteSql":
            data = Lite.transform_select(query, config['main_collections']['netserver'], 'netserver')
            nodes = []
            connections = []
            lables = []
            colors = []
            titles = []
            for res in data['data']:
                if res['localAddr']['name'] not in nodes:                
                    lables.append(res['localAddr']['name'])
                    src = int(res['localAddr']['ip'].replace('.',''))
                    nodes.append(src)
                    colors.append("#21b06d"),
                    titles.append(res['localAddr']['ip']) 
                if res['remoteAddr']['name'] not in nodes:
                    lables.append(res['remoteAddr']['name'])
                    dst = int(res['remoteAddr']['ip'].replace('.',''))
                    nodes.append(dst)
                    colors.append("#2b7387")
                    titles.append(res['remoteAddr']['ip'])
                title = f"title={res['relation']['port']}"
                connections.append((src,dst,title))   

            net = Network(height='1080px', width='100%', bgcolor='#222222', font_color='white', filter_menu=False) 
            net.add_nodes(
                nodes, 
                label=lables,
                title=titles,
                color=colors
            )
            net.add_edges(connections)
            net.repulsion()
            net.write_html(f'react_ui/build/graph_{ts}.html')
            return f'react_ui/build/graph_{ts}.html'
        
        if config['server']['db'] == "MongoDB":
            data = Mongo.select_data(query,config['main_collections']['netserver'])
            nodes = []
            connections = []
            lables = []
            colors = []
            titles = []
            for res in data['data']:
                if res['localAddr']['name'] not in nodes:                
                    lables.append(res['localAddr']['name'])
                    src = int(res['localAddr']['ip'].replace('.',''))
                    nodes.append(src)
                    colors.append("#21b06d"),
                    titles.append(res['localAddr']['ip']) 
                if res['remoteAddr']['name'] not in nodes:
                    lables.append(res['remoteAddr']['name'])
                    dst = int(res['remoteAddr']['ip'].replace('.',''))
                    nodes.append(dst)
                    colors.append("#2b7387")
                    titles.append(res['remoteAddr']['ip'])
                title = f"title={res['relation']['port']}"
                connections.append((src,dst,title))   

            net = Network(height='1080px', width='100%', bgcolor='#222222', font_color='white', filter_menu=False) 
            net.add_nodes(
                nodes, 
                label=lables,
                title=titles,
                color=colors
            )
            net.add_edges(connections)
            net.repulsion()
            net.write_html(f'/tmp/graph_{ts}.html')
            return f'/tmp/graph_{ts}.html'


    def generate_png(url_file):

        ts = int(datetime.datetime.now().timestamp())
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            for browser_type in [p.chromium]:
                browser = browser_type.launch()
                page = browser.new_page()
                file = open(url_file, "r").read()
                page.set_content(file, wait_until="load")
                page.screenshot(path=f'/tmp/graph_{ts}.png', full_page=True)
                browser.close()
                return f'/tmp/graph_{ts}.png'
    
    def generate_long_png(url_file):

        ts = int(datetime.datetime.now().timestamp())
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            for browser_type in [p.chromium]:
                browser = browser_type.launch()
                page = browser.new_page()
                file = open(url_file, "r").read()
                page.set_content(file, wait_until="load")
                page.wait_for_timeout(30000)
                page.screenshot(path=f'/tmp/graph_{ts}.png', full_page=True)
                browser.close()
                return f'/tmp/graph_{ts}.png'