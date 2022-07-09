import json
import requests

def get_now_price(URL, headers, CODE):
    ''' 지정 종목(code)의 현재 가격 가져오기 '''
    params = {
        "fid_cond_mrkt_div_code":"J",
        "fid_input_iscd":CODE
        }
    
    URI = f"{URL}/uapi/domestic-stock/v1/quotations/inquire-price"
    
    response = requests.get(URI, headers=headers, params=params).json()
    
    return int(response['output']['stck_prpr'])