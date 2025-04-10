import requests
import random
import time
import threading
from tqdm import tqdm
from colorama import Fore, Style, init

# HARIMAU JAMBI TUNG TUNG
init(autoreset=True)

# AUTO GET PROXY
proxy_sources = [
"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all",
"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
"https://www.proxy-list.download/api/v1/get?type=http",
"https://www.proxy-list.download/api/v1/get?type=https",
"https://www.proxy-list.download/api/v1/get?type=socks4",
"https://www.proxy-list.download/api/v1/get?type=socks5",
"https://spys.me/proxy.txt",
"https://www.free-proxy-list.net/",
"https://proxy-daily.com/",
"https://premproxy.com/list/",
"https://advanced.name/freeproxy",
"https://ghostealth.com/proxy-scraper",
"https://iproyal.com/free-proxy-list/",
"https://hide.mn/en/proxy-list/",
"https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
"https://www.proxyscan.io/download?type=http",
"https://www.proxyscan.io/download?type=https",
"https://www.proxyscan.io/download?type=socks4",
"https://www.proxyscan.io/download?type=socks5",
"https://openproxy.space/list/http",
"https://openproxy.space/list/https",
"https://openproxy.space/list/socks4",
"https://openproxy.space/list/socks5",
"https://www.geonode.com/free-proxy-list/",
"https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc",
"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
"https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt",
"https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks4.txt",
"https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks5.txt",
"https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt",
"https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/http_proxies.txt",
"https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/socks4_proxies.txt",
"https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/socks5_proxies.txt",
"https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/main/socks5.txt",
"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
"https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/test/proxy.txt",
"https://www.sslproxies.org/",
"https://www.us-proxy.org/",
"https://www.socks-proxy.net/",
"https://www.proxynova.com/proxy-server-list/",
"https://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc",
"https://www.my-proxy.com/free-proxy-list.html",
"https://www.proxy-listen.de/Proxy/Proxyliste.html",
"https://www.proxylists.net/",
"https://www.proxynova.com/proxy-server-list/country-us/",
"https://www.proxynova.com/proxy-server-list/country-de/",
"https://www.proxynova.com/proxy-server-list/country-fr/",
"https://www.proxynova.com/proxy-server-list/country-gb/",
"https://www.proxynova.com/proxy-server-list/country-ca/",
"https://www.proxynova.com/proxy-server-list/country-au/",
"https://www.proxynova.com/proxy-server-list/country-jp/",
"https://www.proxynova.com/proxy-server-list/country-cn/",
"https://www.freeproxy.world/",
"https://www.proxy-list.org/english/index.php",
"https://www.proxynova.com/proxy-server-list/country-br/",
"https://www.proxynova.com/proxy-server-list/country-in/",
"https://www.proxynova.com/proxy-server-list/country-ru/",
"https://www.proxydocker.com/en/proxylist/country/US",
"https://www.proxydocker.com/en/proxylist/country/DE",
"https://www.proxydocker.com/en/proxylist/country/FR",
"https://www.proxydocker.com/en/proxylist/country/GB",
"https://www.proxydocker.com/en/proxylist/country/CA",
"https://www.proxydocker.com/en/proxylist/country/AU",
"https://www.proxydocker.com/en/proxylist/country/JP",
"https://www.proxydocker.com/en/proxylist/country/CN",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
"https://proxy-spider.com/api/proxies.example",
"https://www.freeproxylists.net/",
"https://proxylist.me/",
"https://www.cool-proxy.net/",
"https://www.proxies24.com/",
"https://www.advanced-proxy.com/",
"https://www.getproxylist.com/api/proxy",
"https://multiproxy.org/txt_all/proxy.txt",
"https://www.proxyserverlist24.top/",
"https://proxyhub.me/en/free-proxy-list.html",
"https://free-proxy-list.net/",
"https://www.proxy-list.download/HTTP",
"https://www.proxy-list.download/HTTPS",
"https://www.proxy-list.download/SOCKS4",
"https://www.proxy-list.download/SOCKS5",
"https://spys.one/en/free-proxy-list/",
"https://www.proxylists.net/http_highanon.txt",
"https://www.proxylists.net/https_highanon.txt",
"https://www.proxylists.net/socks4.txt",
"https://www.proxylists.net/socks5.txt",
"https://www.my-proxy.com/free-anonymous-proxy.html",
"https://www.my-proxy.com/free-elite-proxy.html",
"https://www.my-proxy.com/free-transparent-proxy.html",
"https://www.my-proxy.com/free-socks-4-proxy.html",
"https://www.my-proxy.com/free-socks-5-proxy.html",
"https://www.my-proxy.com/free-proxy-list-1.html",
"https://www.my-proxy.com/free-proxy-list-2.html",
"https://www.my-proxy.com/free-proxy-list-3.html",
"https://www.my-proxy.com/free-proxy-list-4.html",
"https://www.my-proxy.com/free-proxy-list-5.html",
"https://www.my-proxy.com/free-proxy-list-6.html",
"https://www.my-proxy.com/free-proxy-list-7.html",
"https://www.my-proxy.com/free-proxy-list-8.html",
"https://www.my-proxy.com/free-proxy-list-9.html",
"https://www.my-proxy.com/free-proxy-list-10.html",
"https://www.my-proxy.com/free-proxy-list-11.html",
"https://www.my-proxy.com/free-proxy-list-12.html",
"https://www.my-proxy.com/free-proxy-list-13.html",
"https://www.my-proxy.com/free-proxy-list-14.html",
"https://www.my-proxy.com/free-proxy-list-15.html",
"https://www.my-proxy.com/free-proxy-list-16.html",
"https://www.my-proxy.com/free-proxy-list-17.html",
"https://www.my-proxy.com/free-proxy-list-18.html",
"https://www.my-proxy.com/free-proxy-list-19.html",
"https://www.my-proxy.com/free-proxy-list-20.html",
"https://www.my-proxy.com/free-proxy-list-21.html",
"https://www.my-proxy.com/free-proxy-list-22.html",
"https://www.my-proxy.com/free-proxy-list-23.html",
"https://www.my-proxy.com/free-proxy-list-24.html",
"https://www.my-proxy.com/free-proxy-list-25.html",
"https://www.my-proxy.com/free-proxy-list-26.html",
"https://www.my-proxy.com/free-proxy-list-27.html",
"https://www.my-proxy.com/free-proxy-list-28.html",
"https://www.my-proxy.com/free-proxy-list-29.html",
"https://www.my-proxy.com/free-proxy-list-30.html",
"https://www.my-proxy.com/free-proxy-list-31.html",
"https://www.my-proxy.com/free-proxy-list-32.html",
"https://www.my-proxy.com/free-proxy-list-33.html",
"https://www.my-proxy.com/free-proxy-list-34.html",
"https://www.my-proxy.com/free-proxy-list-35.html",
"https://www.my-proxy.com/free-proxy-list-36.html",
"https://www.my-proxy.com/free-proxy-list-37.html",
"https://www.my-proxy.com/free-proxy-list-38.html",
"https://www.my-proxy.com/free-proxy-list-39.html",
"https://www.my-proxy.com/free-proxy-list-40.html",
"https://www.my-proxy.com/free-proxy-list-41.html",
"https://www.my-proxy.com/free-proxy-list-42.html",
"https://www.my-proxy.com/free-proxy-list-43.html",
"https://www.my-proxy.com/free-proxy-list-44.html",
"https://www.my-proxy.com/free-proxy-list-45.html",
"https://www.my-proxy.com/free-proxy-list-46.html",
"https://www.my-proxy.com/free-proxy-list-47.html",
"https://www.my-proxy.com/free-proxy-list-48.html",
"https://www.my-proxy.com/free-proxy-list-49.html",
"https://www.my-proxy.com/free-proxy-list-50.html",
"https://www.my-proxy.com/free-proxy-list-51.html",
"https://www.my-proxy.com/free-proxy-list-52.html",
"https://www.my-proxy.com/free-proxy-list-53.html",
"https://www.my-proxy.com/free-proxy-list-54.html",
"https://www.my-proxy.com/free-proxy-list-55.html",
"https://www.my-proxy.com/free-proxy-list-56.html",
"https://www.my-proxy.com/free-proxy-list-57.html",
"https://www.my-proxy.com/free-proxy-list-58.html",
"https://www.my-proxy.com/free-proxy-list-59.html",
"https://www.my-proxy.com/free-proxy-list-60.html",
"https://www.my-proxy.com/free-proxy-list-61.html",
"https://www.my-proxy.com/free-proxy-list-62.html",
"https://www.my-proxy.com/free-proxy-list-63.html",
"https://www.my-proxy.com/free-proxy-list-64.html",
"https://www.my-proxy.com/free-proxy-list-65.html",
"https://www.my-proxy.com/free-proxy-list-66.html",
]

url_vote = "https://disqus.com/api/3.0/threadReactions/vote"
thread_id = input(Fore.CYAN + "𝗜𝗡𝗣𝗨𝗧 𝗜𝗗 𝗧𝗨𝗝𝗨𝗔𝗡: " + Style.RESET_ALL).strip()
loop_count = int(input(Fore.YELLOW + "𝗜𝗡𝗣𝗨𝗧 𝗝𝗨𝗠𝗟𝗔𝗛 𝗦𝗘𝗦𝗜 (berapa kali loop): " + Style.RESET_ALL))

user_agents = [
    # Android
    "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",

    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/115.0",
]

payload = {
    "thread": thread_id,
    "reaction": "3860160",
    "api_key": "E8Uh5l5fHZ6gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F"
}

vote_success = 0
vote_failed = 0

def get_fresh_proxies():
    all_proxies = set()
    threads = []

    def fetch_proxies(url):
        try:
            response = requests.get(url, timeout=8)
            if response.status_code == 200:
                for proxy in response.text.split("\n"):
                    proxy = proxy.strip()
                    if proxy and ":" in proxy:
                        all_proxies.add(proxy)
        except:
            pass

    print(Style.BRIGHT + Fore.WHITE + "🔹 Mengambil proxy terbaru..." + Style.RESET_ALL)

    for url in proxy_sources:
        t = threading.Thread(target=fetch_proxies, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return list(all_proxies)

def vote(proxy, pbar):
    global vote_success, vote_failed

    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": "https://disqus.com/embed/comments/",
    }
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

    try:
        response = requests.post(url_vote, data=payload, headers=headers, proxies=proxies, timeout=5)
        if response.status_code == 200 and '"code":0' in response.text:
            vote_success += 1
        else:
            vote_failed += 1
    except:
        vote_failed += 1

    pbar.set_description(f"{Style.BRIGHT}{Fore.BLUE}• {Style.BRIGHT}{Fore.WHITE}Voting | {Style.BRIGHT}{Fore.GREEN}BERHASIL : {vote_success}{Style.RESET_ALL} | {Style.BRIGHT}{Fore.RED}GAGAL : {vote_failed}{Style.RESET_ALL}")
    pbar.update(1)

def main():
    for i in range(loop_count):
        print(Fore.MAGENTA + f"\n🔄 Memulai sesi ke-{i+1} dari {loop_count}..." + Style.RESET_ALL)
        
        start_time = time.time()
        proxies_list = get_fresh_proxies()
        if not proxies_list:
            print(Fore.RED + "⛔ Tidak ada proxy yang tersedia. Menunggu 30 detik sebelum mencoba lagi..." + Style.RESET_ALL)
            time.sleep(30)
            continue

        print(Fore.GREEN + f"✅ Dapat {len(proxies_list)} proxy fresh! Langsung voting..." + Style.RESET_ALL)

        num_threads = 5000  
        with tqdm(total=len(proxies_list), desc="🗳️ Voting...", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} [{elapsed}]") as pbar:
            for j in range(0, len(proxies_list), num_threads):
                threads = []
                for proxy in proxies_list[j:j + num_threads]:
                    t = threading.Thread(target=vote, args=(proxy, pbar))
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()

                time.sleep(random.uniform(0, 1))  

        print(Fore.CYAN + f"⏳ Sesi ke-{i+1} selesai dalam {round(time.time() - start_time, 2)} detik." + Style.RESET_ALL)
        time.sleep(5)

    print(Fore.GREEN + "🎉 Semua sesi selesai! Program berhenti." + Style.RESET_ALL)

if __name__ == "__main__":
    main()