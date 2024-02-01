import requests
import urllib3
import base64

urllib3.disable_warnings()

tc = '11111111110'
ASPNET_SessionId = '31313131313131'

headers = {
  "accept": "application/json, text/javascript, /; q=0.01",


  "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",


  "content-type": "application/json; charset=UTF-8",


  "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',


  "sec-ch-ua-mobile": "?0",


  "sec-ch-ua-platform": '"Windows"',


  "sec-fetch-dest": "empty",


  "sec-fetch-mode": "cors",


  "sec-fetch-site": "same-origin",


  "x-requested-with": "XMLHttpRequest"
}

payload1 = {
  "Keys": ["ogrTcNo"],
  "Degerler": [tc]
}

payload2 = {'fotovarmi': '1'}

url1 = "https://e-okul.meb.gov.tr/IlkOgretim/OKL/IOK27007.aspx/ogrenciGetir"

url2 = "https://e-okul.meb.gov.tr/IlkOgretim/OKL/IOK27007.aspx/fotoGetir"

url3 = "https://e-okul.meb.gov.tr/IlkOgretim/OKL/OKLResimGoster.aspx"

cookies = {
  "ASP.NET_SessionId": ASPNET_SessionId
}

requests.post(url1, headers=headers, json=payload1, cookies=cookies, verify=True)

requests.post(url2, headers=headers, json=payload2, cookies=cookies, verify=True)

response = requests.get(url3, headers=headers, cookies=cookies, verify=True)

image_data = response.content

base64_data = base64.b64encode(image_data).decode('utf-8')