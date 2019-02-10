from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
client = PIWebApiClient("https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi", useKerberos=False, username="username", password="password", verifySsl=True)
print(client)