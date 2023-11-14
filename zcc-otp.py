#!/usr/bin/python3

import requests
import argparse
import sys
import urllib3
urllib3.disable_warnings()

session = requests.Session()
base_url = 'https://<ZSCALER CLOUD TENANT>'
base_headers = {
    'Content-Type': 'application/json'
}


def parse_data():
    """ Parse username """
    parser = argparse.ArgumentParser(description='Enter Username')
    parser.add_argument('Username', metavar='Username',
                        type=str, help='Enter the username found in the user\'s ZCC')
    args = parser.parse_args()
    user = args.Username
    
    return user


def auth():
    """ Authentication Function """
    payload = {"apiKey": "<API KEY>",
               "secretKey": "<API SECRET>"}
    response = requests.post(
        f'{base_url}/papi/auth/v1/login', headers=base_headers, json=payload, verify=False)
    json_data = response.json()
    token = json_data.get('jwtToken')

    return token


def get_otp(key, sort_details):
    """ Get OTP function for the user """
    for items in sort_details:
        if sort_details:
            udid = items['udid']
            policyName = items['policyName']
            detail = items['detail']
            machineHostname = items['machineHostname']
            registrationState = items['registrationState']
            url = f"{base_url}/papi/public/v1/getOtp"
            parameters = {"udid": f"{udid}"}
            headers = {"auth-token": key}
            response = session.get(url, params=parameters,
                                   headers=headers, verify=False)

            json_response = response.json()
            for otp_val in json_response.items():
                print('Policy Name:', policyName,
                      '|| Device:', detail, '|| Hostname:', machineHostname, '|| State:', registrationState, '||', otp_val)
        else:
            pass


def retrieved_info(dl_key, user):
    """ Retrieved user information """
    user_data = []
    headers = {"auth-token": dl_key, "Content-Type": "*/*"}
    try:
        parameters = {
            "username": f"{user}"
        }
        dl_response = requests.get(
            f'{base_url}/papi/public/v1/getDevices', params=parameters, headers=headers, verify=False)
        json_data = dl_response.json()
        for data in json_data:
            user_data.append(data)
    except:
        print('\nNo Username Found. Please check the username in ZCC')
    return user_data


if __name__ == '__main__':
    try:
        token = auth()
        parse_user = parse_data()
        user_details = retrieved_info(dl_key=token, user=parse_user)
        get_otp(key=token, sort_details=user_details)

    except KeyboardInterrupt:
        print('Quiting!!')
        sys.exit()
