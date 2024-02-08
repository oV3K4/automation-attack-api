import requests
import json
#from password_generator import PasswordGenerator
import os


#HEADER DA REQUEST | put inside quotation marks
header = {
'Host': '',
'User-Agent': '',
'Accept': '*/*',
'Accept-Language': '',
'Accept-Encoding': '',
'Content-Type': '',
'Content-Length': '',
'Origin': '',
'Connection': '',
'Referer': '',
'Sec-Fetch-Dest': '',
'Sec-Fetch-Mode': '',
'Sec-Fetch-Site': '',
'TE': '',
    }

#REQUEST PAYLOAD
payload = 'request_id: "769f83c6-2504-43bb-8e90-fce739aa8b5a"'

#Replace archive-payload.txt with your file payload 
arquivo1 = open('#archive-payload.txt', 'r')
linhas_payloads = arquivo1.readlines()
for linhas  in linhas_payloads:
    print('Attacking payloads...')
    payload_final = payload + linhas
    #Replace url-attack whit your url
    r = requests.post('url-attack', headers=header, data=json.dumps(payload_final))
    print('################################################')
    print('Attacking with payloads: ' +payload_final)
    print('Response code: '+ str(r.status_code))
    print('#################################################')
    if r.status_code == 200:
        resultado = open('result.txt', 'a')
        resultado.write(linhas)
        resultado.close()
arquivo1.close()

#Attack XSS | Replace xss.txt with your file xss
arquivo2 = open('xss.txt', 'r')
linhas_payloads = arquivo2.readlines()
for linhas  in linhas_payloads:
    print('Attacking payloads XSS')
    payload_final = payload + linhas
    #Replace url-attack whit your url
    r = requests.post('', headers=header, data=json.dumps(payload_final))
    print('################################################')
    print('Attacking with payload: ' +payload_final)
    print('Response code: '+ str(r.status_code))
    print('#################################################')
    if r.status_code == 200:
        resultado = open('result_XSS.txt', 'a')
        resultado.write(linhas)
        resultado.close()
arquivo2.close()
