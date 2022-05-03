import requests
import pystyle
import colorama
import os
from pystyle import Colors, Colorate

banner = """

      %%% %%%%%%%            |#|
    %%%% %%%%%%%%%%%        |#|####
  %%%%% %         %%%       |#|=#####
 %%%%% %   @    @   %%      | | ==####
%%%%%% % (_  ()  )  %%     | |    ===##
%%  %%% %  \_    | %%      | |       =##
%    %%%% %  u^uuu %%     | |         ==#
      %%%% %%%%%%%%%      | |           V

        PyIP
"""

print(Colorate.Horizontal(Colors.purple_to_red, banner, 1))

print("Welcome to PyIP, an IP address tracker...")
print("Made by Woox")
print("Enter IP")
ipaddr = input("> ")

r = requests.get(f"http://ip-api.com/json/{ipaddr}").json()

ip = r["query"]
status = r['status']
city = r["city"]
country = r["country"]
countrycode = r["countryCode"]
region = r["region"]
regionname = r["regionName"]
timezone = r["timezone"]
zip = r["zip"]
lat = r['lat']
lon = r["lon"]
isp = r["isp"]
org = r["org"]

print(Colorate.Horizontal(Colors.purple_to_red, banner, 1))
print(Colorate.Horizontal(Colors.red_to_purple, f"""TARGET LOCKED
STATUS: {status}

IP: {ip}
COUNTRY: {country}
COUNTRY CODE: {countrycode}
REGION: {region}
REGION NAME: {regionname}
CITY: {city}
ZIP: {zip}
TIMEZONE: {timezone}
ISP: {isp}

LAT: {lat}
LON: {lon}
"""))

