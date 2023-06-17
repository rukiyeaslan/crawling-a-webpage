import threading
import requests
from fastapi import FastAPI
from queue import Queue

app = FastAPI()

base_url = "https://ranking.glassdollar.com/graphql"
cookies = {
    '_gid': 'GA1.2.19690312.1686825226',
    'fpestid': 'yMhIHhCboNrvOUIVDnfxssieipdbO31726hWWCPAgg7tQJPn8PU7q76MLi_72b-ozMUOfw',
    '_cc_id': '7629d44d236c467879c987bbe33cbd0c',
    'panoramaId_expiry': '1687430029653',
    'panoramaId': 'f04d3150c0c5be051657763c035616d53938b6b3f5f785c701837239283b6517',
    'panoramaIdType': 'panoIndiv',
    'pubconsent-v2': 'YAAAAAAAAAAA',
    'euconsent-v2': 'CPtZ00APtZ00AAZACBENDICsAP_AAH_AAAAAJftX_H__bW9r8f7_aft0eY1P9_j77uQzDhfNk-4F3L_W_JwX52E7NF36tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5umxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eX33_79_7_H9-f_876CXYBJhq3EAXYlDgTaBhFCiBGFYQEUCgAgoBhaICABwcFOyMAn1hEgBQCgCMCIEOAKMiAQAAAQBIRABIEWCAAAAQCAAEACARCAAgYBBQAWAgEAAIDoGKIUAAgSECREREKYEBECQQEtlQglBdIaYQBVlgBQCI2CgARAACKwABAWDgGCJASsWCBJiDaIABgBQCiVCtQSemgAWMjYAA.YAAAAAAAAAAA',
    'amp_82cffd': 'r0S_1OT-9FlkifJN2gmPT9...1h31k032h.1h31k032r.2.3.5',
    'ph_phc_lnmZRXk93ClxaDiO57RjaSrzVTbSpNZ3Z7ZQQJSIs3M_posthog': '%7B%22distinct_id%22%3A%22188bff46c6613e-066050c4dc45bc-1c525634-13c680-188bff46c671544%22%2C%22%24device_id%22%3A%22188bff46c6613e-066050c4dc45bc-1c525634-13c680-188bff46c671544%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22%24sesid%22%3A%5B1686902934635%2C%22188c3400c6c1430-03407e5fdb668e-1c525634-13c680-188c3400c6d1613%22%2C1686902934635%5D%2C%22%24session_recording_enabled_server_side%22%3Atrue%2C%22%24console_log_recording_enabled_server_side%22%3Atrue%2C%22%24session_recording_recorder_version_server_side%22%3A%22v1%22%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D',
    '_gat_gtag_UA_102907215_1': '1',
    'lotame_domain_check': 'glassdollar.com',
    '_ga_SX8XLCG27H': 'GS1.1.1686995284.9.1.1686995312.0.0.0',
    '_ga': 'GA1.1.1115221620.1686825226',
}

headers = {
    'authority': 'ranking.glassdollar.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.2.19690312.1686825226; fpestid=yMhIHhCboNrvOUIVDnfxssieipdbO31726hWWCPAgg7tQJPn8PU7q76MLi_72b-ozMUOfw; _cc_id=7629d44d236c467879c987bbe33cbd0c; panoramaId_expiry=1687430029653; panoramaId=f04d3150c0c5be051657763c035616d53938b6b3f5f785c701837239283b6517; panoramaIdType=panoIndiv; pubconsent-v2=YAAAAAAAAAAA; euconsent-v2=CPtZ00APtZ00AAZACBENDICsAP_AAH_AAAAAJftX_H__bW9r8f7_aft0eY1P9_j77uQzDhfNk-4F3L_W_JwX52E7NF36tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5umxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eX33_79_7_H9-f_876CXYBJhq3EAXYlDgTaBhFCiBGFYQEUCgAgoBhaICABwcFOyMAn1hEgBQCgCMCIEOAKMiAQAAAQBIRABIEWCAAAAQCAAEACARCAAgYBBQAWAgEAAIDoGKIUAAgSECREREKYEBECQQEtlQglBdIaYQBVlgBQCI2CgARAACKwABAWDgGCJASsWCBJiDaIABgBQCiVCtQSemgAWMjYAA.YAAAAAAAAAAA; amp_82cffd=r0S_1OT-9FlkifJN2gmPT9...1h31k032h.1h31k032r.2.3.5; ph_phc_lnmZRXk93ClxaDiO57RjaSrzVTbSpNZ3Z7ZQQJSIs3M_posthog=%7B%22distinct_id%22%3A%22188bff46c6613e-066050c4dc45bc-1c525634-13c680-188bff46c671544%22%2C%22%24device_id%22%3A%22188bff46c6613e-066050c4dc45bc-1c525634-13c680-188bff46c671544%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22%24sesid%22%3A%5B1686902934635%2C%22188c3400c6c1430-03407e5fdb668e-1c525634-13c680-188c3400c6d1613%22%2C1686902934635%5D%2C%22%24session_recording_enabled_server_side%22%3Atrue%2C%22%24console_log_recording_enabled_server_side%22%3Atrue%2C%22%24session_recording_recorder_version_server_side%22%3A%22v1%22%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; _gat_gtag_UA_102907215_1=1; lotame_domain_check=glassdollar.com; _ga_SX8XLCG27H=GS1.1.1686995284.9.1.1686995312.0.0.0; _ga=GA1.1.1115221620.1686825226',
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


# Define the function to fetch ids for all enterprises
def fetch_enterprise_data():

    # Define the GraphQL query
    query = '''
    query GetCorporates($filters: CorporateFilters, $page: Int) {
      corporates(filters: $filters, page: $page) {
        rows {
          id
          name
          logo_url
        }
        count
      }
    }
    '''

    # Search filters
    filters = {
        "hq_city": [],
        "industry": []
    }

    # Set the initial page to 1
    page = 1

    # List to store all the corporates
    all_corporates = []

    while True:
        # Define the request payload
        payload = {
            "operationName": "GetCorporates",
            "variables": {
                "filters": filters,
                "page": page
            },
            "query": query
        }

        response = requests.post(base_url, cookies=cookies, headers=headers, json=payload)

        data = response.json().get("data", {})
        corporates = data.get("corporates", {}).get("rows", [])
        count = data.get("corporates", {}).get("count", 0)

        # Add the retrieved corporates to the list
        all_corporates.extend(corporates)

        # Increment the page number
        page += 1

        # Break the loop if all corporates have been retrieved
        if len(all_corporates) >= count:
            break
    # Id list for all corporates
    id_list = [corporate["id"] for corporate in all_corporates]
    return id_list

# Queue to store all the details for each corporate
# Using Queue because it is thread-safe
all_ent = Queue()

# Function to get detailed information for a corporate by using its id
def detailed_enterprise_data( id):
    json_data = {
        'variables': {
            'id': id,
        },
        'query': 'query ($id: String!) {\n  corporate(id: $id) {\n     name\n    description\n    logo_url\n    hq_city\n    hq_country\n    website_url\n    linkedin_url\n    twitter_url\n    startup_partners_count\n    startup_partners {\n         company_name\n      logo_url: logo\n      city\n      website\n      country\n      theme_gd\n         }\n    startup_themes\n  }\n}\n',
    }

    response = requests.post(base_url, cookies=cookies, headers=headers, json=json_data)
    all_ent.put([id, response.json()["data"]["corporate"]])
    return


@app.get("/")
async def crawl_enterprises():
    # Get all ids of enterprises
    enterprise_ids = fetch_enterprise_data()

    # Define the thread function
    def process_enterprises(enterprise_ids):
        for enterprise_id in enterprise_ids:
            detailed_enterprise_data(enterprise_id)

    # Split the list of enterprise IDs into batches
    batch_size = 85
    enterprise_batches = [enterprise_ids[i:i + batch_size] for i in range(0, len(enterprise_ids), batch_size)]

    # Using threads to get the data faster
    # Create the thread pool
    num_threads = 10
    threads = []

    # Assign batches of enterprise IDs to threads and start the threads
    for i in range(num_threads):
        thread = threading.Thread(target=process_enterprises, args=(enterprise_batches[i],))
        threads.append(thread)
        thread.start()

    # Wait for the threads to complete
    for thread in threads:
        thread.join()

    # Return the results
    result = {}
    while not all_ent.empty():
        id, corporate = all_ent.get()
        result[id] = corporate

    return result
