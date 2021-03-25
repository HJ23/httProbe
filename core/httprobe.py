import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from concurrent.futures import ThreadPoolExecutor
from termcolor import cprint


class HttProbe:
    def __init__(self,threads,verbose,output):
        self.threads=threads
        self.verbose=verbose
        self.output=output
        
        self.ports=["81", "300", "591", "593", "832", "981", "1010", "1311", "2082", "2087", "2095", "2096", "2480", "3000", "3128", "3333", "4243", "4567", "4711", "4712", "4993", "5000", "5104", "5108", "5800", "6543", "7000", "7396", "7474", "8000", "8001", "8008", "8014", "8042", "8069", "8080", "8081", "8088", "8090", "8091", "8118", "8123", "8172", "8222", "8243", "8280", "8281", "8333", "8443", "8500", "8834", "8880", "8888", "8983", "9000", "9043", "9060", "9080", "9090", "9091", "9200", "9443", "9800", "9981", "12443", "16080", "18091", "18092", "20720", "28017"]
        self.HEADERS={ "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",\
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                       "Accept-Language": "en-US,en;q=0.8",
                       "Accept-Encoding": "gzip",}
        self.SESSION=requests.Session()
    def save(self,_list):
        crrt_path= os.path.dirname(os.path.realpath(__file__))
        path=os.path.join(crrt_path,"..",self.output)
        with open(path,"w") as file:
            file.writelines(_list)
        return
    
    def read(self,path2file):
        _list=[]
        if(os.path.exists(path2file)):
            with open(path2file,"r") as file:
                _list=file.readlines()
            _list=list(map(lambda x:x.replace("\n",""),_list))
        return _list
    
    def check(self,domain):
        results=[]
        
        for prefix in ["http://","https://"]:
            try:
                url=prefix+domain
                self.SESSION.get(url,headers=self.HEADERS,verify=False,timeout=5)
                cprint(url,"green")
                results.append(url)                    
            except Exception as e:
                if(self.verbose):
                    cprint(str(e),"red")
        
        for prefix in ["http://","https://"]:
            for port in self.ports:
                try:
                    url=prefix+domain+":"+port
                    self.SESSION.get(url,headers=self.HEADERS,verify=False,timeout=5)
                    cprint(url,"green")
                    results.append(url)                    
                except Exception as e:
                    if(self.verbose):
                        cprint(str(e),"red")
        return results     
        
    
    def start(self,domains):
        
        final=[]
        futures=[]
        with ThreadPoolExecutor(self.threads) as thread:
            for domain in domains:
                futures.append(thread.submit(self.check,domain=domain))
        
        for future in futures:
            final+=future.result()
        
        return final
