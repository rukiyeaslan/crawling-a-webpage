# get the data from the main page
import requests

cookies = {
    '_gid': 'GA1.2.19690312.1686825226',
    'fpestid': 'yMhIHhCboNrvOUIVDnfxssieipdbO31726hWWCPAgg7tQJPn8PU7q76MLi_72b-ozMUOfw',
    '_cc_id': '7629d44d236c467879c987bbe33cbd0c',
    'panoramaId_expiry': '1687430029653',
    'panoramaId': 'f04d3150c0c5be051657763c035616d53938b6b3f5f785c701837239283b6517',
    'panoramaIdType': 'panoIndiv',
    'pubconsent-v2': 'YAAAAAAAAAAA',
    'euconsent-v2': 'CPtZ00APtZ00AAZACBENDICsAP_AAH_AAAAAJftX_H__bW9r8f7_aft0eY1P9_j77uQzDhfNk-4F3L_W_JwX52E7NF36tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5umxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eX33_79_7_H9-f_876CXYBJhq3EAXYlDgTaBhFCiBGFYQEUCgAgoBhaICABwcFOyMAn1hEgBQCgCMCIEOAKMiAQAAAQBIRABIEWCAAAAQCAAEACARCAAgYBBQAWAgEAAIDoGKIUAAgSECREREKYEBECQQEtlQglBdIaYQBVlgBQCI2CgARAACKwABAWDgGCJASsWCBJiDaIABgBQCiVCtQSemgAWMjYAA.YAAAAAAAAAAA',
    '_ga': 'GA1.2.1115221620.1686825226',
    '_ga_SX8XLCG27H': 'GS1.1.1686829708.2.1.1686830905.0.0.0',
}

headers = {
    'authority': 'ranking.glassdollar.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.2.19690312.1686825226; fpestid=yMhIHhCboNrvOUIVDnfxssieipdbO31726hWWCPAgg7tQJPn8PU7q76MLi_72b-ozMUOfw; _cc_id=7629d44d236c467879c987bbe33cbd0c; panoramaId_expiry=1687430029653; panoramaId=f04d3150c0c5be051657763c035616d53938b6b3f5f785c701837239283b6517; panoramaIdType=panoIndiv; pubconsent-v2=YAAAAAAAAAAA; euconsent-v2=CPtZ00APtZ00AAZACBENDICsAP_AAH_AAAAAJftX_H__bW9r8f7_aft0eY1P9_j77uQzDhfNk-4F3L_W_JwX52E7NF36tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5umxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eX33_79_7_H9-f_876CXYBJhq3EAXYlDgTaBhFCiBGFYQEUCgAgoBhaICABwcFOyMAn1hEgBQCgCMCIEOAKMiAQAAAQBIRABIEWCAAAAQCAAEACARCAAgYBBQAWAgEAAIDoGKIUAAgSECREREKYEBECQQEtlQglBdIaYQBVlgBQCI2CgARAACKwABAWDgGCJASsWCBJiDaIABgBQCiVCtQSemgAWMjYAA.YAAAAAAAAAAA; _ga=GA1.2.1115221620.1686825226; _ga_SX8XLCG27H=GS1.1.1686829708.2.1.1686830905.0.0.0',
    'origin': 'https://ranking.glassdollar.com',
    'referer': 'https://ranking.glassdollar.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

json_data = {
    'operationName': 'TopRankedCorporates',
    'variables': {},
    'query': 'query TopRankedCorporates {\n  topRankedCorporates {\n    id\n    name\n    logo_url\n    industry\n    hq_city\n    startup_partners {\n      company_name\n      logo_url: logo\n      __typename\n    }\n    startup_friendly_badge\n    __typename\n  }\n}\n',
}

response_main_page = requests.post('https://ranking.glassdollar.com/graphql', cookies=cookies, headers=headers, json=json_data)
main_list = response_main_page.json()["data"]["topRankedCorporates"]

#getting id of each enterprises to use in the json_data as variable
id_list_of_enterprises = [enterprise["id"] for enterprise in main_list]

