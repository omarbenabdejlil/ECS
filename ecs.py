from __future__ import print_function

import requests
import sys
import warnings
import re
import argparse
from common.color import run,good,bad,info,red,end,que,W,R,G,Y,B

warnings.filterwarnings('ignore')
headers={'Accept': 'text/html',
        'Connection': 'keep-alive',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)'}

def banner():
    print("""
%s                                      .                                         
                                     cX;    :O.                                 
                                   '0MMl .c0MN.                                 
                                 .xWWWMkxNWNM0                                  
                               'kWWNXMMMWXKNM0c'                                
                     .:dkkxl,;OWMNNXXXXKKKXWWMMMXk:,oxkkd:.                     
                   :0WMWWWMMMMMNNNXKKKKKKKKKXXNNWMMMMMWWWMW0:                   
                  kMWNNNNNNNWMMNNWXKKKKKKKKKKXWNNMMWNNNNNNNMMk                  
                 dMWNNWWWNNNNNWMNNNKKKKKKKKKKNNNMWNNNNNNWNNNWMd                 
                'WWNNNNNWNXKXXXNMNNXKKKKKKKKXNNMNXXKKXNWNNNWNWW'                
                dMMMNNWWWNXKKKKXNMXNKKKKKKKKNNMNXKKKKXNWWNNNMMMd                
                xOMWNNNNNNWNXKKKKNWNKKKKKKKKNWNKKKKKNWNNNNNNWMOd                
                 lMNNWMMMWWNNXKKKKWNKKKKKKKKNWKKKKXNNWWMMMWNNMl.                
                 dMWWXWMMxxWNNNKKKNWXKKKKKKXNNKKKNNNWkxMMWXWWMo                 
                 lMMNXWMk%sAA%s'KWNNKKKWXKKKKKKXWKKKNNWK'%sAA%skMWXNMMl                 
                 lMWNXWMc%sAAAA%sdWNNKKNXKKKKKKXNKKNNWd%sAAAA%scMWXNWMl                 
                 kMNNNWMl%sAAAAA%s;NWNKXNKKKKKKNXKXWN;%sAAAAA%slMWNNNMk                 
                 0MNNNNMk%sAAAAAA%s.KWXKXXKKKKXXKXWX.%sAAAAAA%skMNNNNM0                 
                 0MMNWXMW.%sAAAAA%s..xMNKKKKKKKKXWx..%sAAAAA%s.WMXWNMM0                 
                 OMMNWNNMd%sAAAAA%s0O%sA%s,ONXXNNXXNO,%sA%sO0%sAAAAA%sdMNNWNMMO                 
                 ,0MNWWNNMc%sAAAA%skO%sAAA%sxMx',xMx%sAAA%sOO%sAAAA%scMNNNWNMO,                 
                  cMWXNNNWMx.%sAAAAA%s,00,....,00,%sAAAAA%s.xMWNNNXWMc                  
                  ,WMKdclokXW0doxKO:.'....'.:OKxod0WXkolcdXMW,                  
                 :WWo.......':cc:....,....,....:cc:'.......oWN;                 
                ;WN;........................................;NN;                
               'NW;....,;:::........................:c:;'....;WN'               
               kMd..';:;cxd,........................,dkc::;'..dMk               
              .NW'.':dkkl..........';:cclc:;'..........lkkdc'.'WN.              
              .XMOKMMXl.........'',,'......',,'..........lXMMKOMX.              
               'xOWMO..............,;:cccc:;,..............OMWOx'               
                 .MN........':oddddl::;,,;::lddddoc'........NM.                 
                 .WW;...;odol;..;coxkOOOOOOkxoc;..;lodo;...;WW.                 
                  cWMNNWMx.,lkKMMWX0OkxxxxkO0XWMMKkc'.xMWNNMNc                  
                   .:oodWWNMMXkc,.            .'ckXMMNWWdoo:.                   
                        .cl:.                      .;cc.                        
                                                                                
    %s-------------------------- Exploit Consult Sale ------------------------
                %s Authors : AnouarBenSaad , OmarBenAbdejlil
    --------------------------------------------------------------------------
""" % (R,
G,R,G,R,
G,R,G,R,
G,R,G,R,
G,R,G,R,
G,R,G,R,
G,R,G,R,G,R,G,R,
G,R,G,R,G,R,G,R,
G,R,G,R,
Y,Y))

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()
def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "\nOPTIONS"
    parser.add_argument('-s', '--search', help="put the exploit you search it for")
    parser.add_argument('-t', '--type', help="put the type of your search")
    parser.add_argument('-p', '--page', help="put the number of search")
    return parser.parse_args()
args = parse_args()
type_e = args.type or "nexpose"
page_e = args.page or 1
search_e = args.search or "wordpress"
def getexploits(search_e,type_e,page_e):
    print("%s Searching for %s%s%s Exploits Type %s%s%s " %(run , Y,search_e,W ,Y,type_e,W) )
    for page_n in range(int(page_e)):
        page_ntostr = str(page_n)
        url="https://www.rapid7.com/db/?q="+search_e+"&type="+type_e+"&page="+page_ntostr+""
        result=requests.get(url,headers).text
        vulntab=[]
        regx = r'<div class=\"resultblock__info-title\">\r\n.+'
        regx_date = r'<div class=\"resultblock__info-meta\">\r\n.+'
        regx_match = r'<div class=\"resultblock__info-title\">\r\n\                                    (.+)' 
        regx_date_match = r'<div class=\"resultblock__info-meta\">\r\n                                    Published: (.+)'
        regx_url = r'<a href=\".+\" class="vulndb__result resultblock\">'
        match_url = r'<a href=\"(.+)\" class="vulndb__result resultblock\">'
        recompile=re.compile(regx)
        recompile_date = re.compile(regx_date)
        vulntitle=re.findall(recompile,result)
        vulndate=re.findall(recompile_date,result)
        vulnurl=re.findall(re.compile(regx_url),result)
        if len(vulntitle)>0:
            print("%s\n---------------------------\n **** PAGE %i **** \n----------------------------\n" % (B,page_n+1))
            for vuln in vulntitle:
                if vuln not in vulntab:         
                    vulntab.append(vuln)
            for i in range(len(vulntab)):
                datematch = re.match(regx_date_match,vulndate[i]).group(1)
                vulnmatch = re.match(regx_match,vulntab[i]).group(1)
                urlmatch  = re.match(match_url,vulnurl[i]).group(1)
                exploiturl = "https://www.rapid7.com"+urlmatch
                print(" %s Exploit NAME : %s " % (good,vulnmatch))
                print(" %s Exploit DATE : %s " % (good,datematch))
                print(" %s Exploit URL  : %s " % (good,exploiturl))


                print("--------------------------------")
        else:
            print("[-]--NOT FOUNDED--------------")

banner()
getexploits(search_e,type_e,page_e)