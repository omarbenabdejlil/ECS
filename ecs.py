from __future__ import print_function

import requests
import sys
import warnings
import re
from common.colors import run,good,bad,info,red,end,que,W,R,G

warnings.filterwarnings('ignore')
headers={'Accept': 'text/html',
        'Connection': 'keep-alive',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)'}

def banner():
    print("""
%s             _____  %s  ____ %s  ____  
%s            | ____| %s / ___|%s / ___| 
%s            |  _|   %s| |    %s \___ \ 
%s            | |___  %s| |___ %s  ___) |
%s            |_____| %s \____|%s |____/ 
%s                                    
            %sExploit Consult Strike%s
            ---------------------
    """ %(
W,R,W,W,R,W,W,R,W,W,R,W,W,R,W,W,G,W)
    )

def getexploits():
    url="https://www.cvedetails.com/vulnerability-list/year-2019/vulnerabilities.html"
    result=requests.get(url,headers).text
    regx=r'<td>\d+-\d+-\d+</td>'
    matchre = r'<td>(\d+-\d+-\d+)</td>'
    regx2=r'<td nowrap><a href=\".+ title=\".+\">.+</a>'
    matchre2=r'<td nowrap><a href=\"(.+) title=\"(.+)\">(.+)</a>'
    caption_regex=r'<td class="cvesummarylong" colspan="20">\n.+</td>'
    matchrecaption = r'<td class=\".+\">\n\t+(.+)</td>'
    recompile=re.compile(regx)
    recompile2=re.compile(regx2)

    # Input data in arrays to the reccursivity

    datetab=[]

    vulntitle=re.findall(recompile2,result)
    datefounds=re.findall(recompile,result)
    caption=re.findall(re.compile(caption_regex),result)
    print("%s process Running ... " % (run))
    if len(datefounds)>0:
        print("[+]-OKEY IT'S FOUND------------")
        for date in datefounds:
            if date not in datetab:
            
                datetab.append(date)
        for i in range(len(datetab)):
            datematch = re.match(matchre,datetab[i]).group(1)
            print("%s Exploit DATE : %s " % (que,datematch))
            urlmatch = re.match(matchre2,vulntitle[i]).group(1)
            exploiturl = "https://www.cvedetails.com"+urlmatch
            exploitname = re.match(matchre2,vulntitle[i]).group(2)
            exploitref = re.match(matchre2,vulntitle[i]).group(3)
            print("%s Exploit URL  : %s " % (good,exploiturl))
            print("%s Exploit NAME : %s " % (good,exploitname))
            print("%s Exploit REF  : %s " % (good,exploitref))
            exploitcaption = re.match(matchrecaption,caption[i]).group(1)
            print("%s Exploit DESC : %s " % (good,exploitcaption))
            print("--------------------------------")
    else:
        print("[-]--NOT FOUNDED--------------")
banner()
getexploits()