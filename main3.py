import time
import base64
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def get_file_content_chrome(driver, uri):
  result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
  # if type(result) == int :
  #   raise Exception("Request failed with status %s" % result)
  return result


def getDriver():
    chrm_options = Options()
    chrm_caps = webdriver.DesiredCapabilities.CHROME.copy()
    chrm_caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    # driver = webdriver.Chrome(executable_path = 'chromedriver.exe', chrome_options=chrm_options,desired_capabilities=chrm_caps) Windows
    return webdriver.Chrome(executable_path='../driver/chromedriver.exe', chrome_options=chrm_options,
                            desired_capabilities=chrm_caps)  # Linux


def login(driver):
    driver.get("https://beetaexch.com/login")


def WebSocketLog():
    arry = []
    while True:
        # print(wsData)
        try:
            wsData = driver.get_log('performance')
            for data in wsData:
                if data not  in arry:
                    a = f"\n{'*'*10}\n{data}\n{'*' * 10}\n"
                    arry.append(data)
                    fs = open("data.txt",'a')
                    fs.write(a)
                    fs.close()
                print("\n","*"*10,"\n",data,"\n","*"*10,"\n")
            print(wsData)
        except:
            continue
        # wsJson = json.loads((wsData['message']))
        # print(wsJson)
        time.sleep(5)
        # # print(wsJson,"\n\n\n\n")
        # if wsJson["message"]["method"] == "Network.webSocketFrameReceived":
        #     result = wsJson["message"]["params"]["response"]["payloadData"]
        #     try:
        #         print(json.loads(result))
        #     except:
        #         pass
        #         print("**"*5,result,"**"*5)
        #     try:
        #         data = base64.b64decode(result)
        #         # data = base64.b64decode(result)
        #         if "AAAAZG1" in result:
        #             open("data.mp4", 'ab').write(data)
        #             # print("\n ************************************  \n", result, "\n\n")
        #             # print("\n\n", data, "\n ************************************  \n")
        #     except Exception as e:
        #         print(e)
        #     # print ("Rx :"+ str(wsJson["message"]["params"]["timestamp"]) + wsJson["message"]["params"]["response"]["payloadData"])
        # if wsJson["message"]["method"] =="Network.webSocketFrameSent":
        #     print ("Tx :"+ wsJson["message"]["params"]["response"]["payloadData"])


if __name__ == '__main__':
    driver = getDriver()
    driver.get("https://www.youtube.com/watch?v=dx4Teh-nv3A&ab_channel=ZeeMusicCompany")
    v = driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video')
    blob = v.get_attribute('src')
    print(blob)
    a = get_file_content_chrome(driver,blob)
    print(a)

# bytes = get_file_content_chrome(driver, "blob:https://developer.mozilla.org/7f9557f4-d8c8-4353-9752-5a49e85058f5")
