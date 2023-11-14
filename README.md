# zscaler-zcc-otp

This API is to retrieve the OTPs of the following; logoutOtp, revertOtp, uninstallOtp, exitOtp, ziaDisableOtp, zpaDisableOtp, zdxDisableOtp, and deceptionSettingsOtp.

Make sure that requests module is installed. You may use the command to install requests.
> pip install request

Sample in running the script.
pyhton3 zcc-otp.py username@sample.com


***
Please changed the "API KEY", "API SECRET", and "ZSCALER CLOUD TENANT" on the script.
Sample:
base_url = 'https://api-mobile.zscalerbeta.net'

Sample:
payload = {
  "apiKey": "aaaaaaaa-aaaa-aaaa-aaaa-bbbbbbbbbbbb",
  "secretKey": "aaaaaaaa-aaaa-aaaa-aaaa-cccccccccccc"
}
***

Zscaler API documentation link:
https://help.zscaler.com/client-connector/about-zscaler-client-connector-api

Author:
Jeffrey Oppuer
