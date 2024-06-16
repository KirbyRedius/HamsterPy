import requests
import time
from threading import Thread

class HamsterClient:
	def __init__(self):
		self.user_data = open("user.txt").read().stripe()
		self.api = "https://api.hamsterkombat.io/"
		self.token = ""
		self.balance_coins = None
		self.level = None
		self.available_taps = None
		self.max_taps = None
		self.headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': f'Bearer {self.token}',
        'Connection': 'keep-alive',
        'Origin': 'https://hamsterkombat.io',
        'Referer': 'https://hamsterkombat.io/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
   
    }

	def request(self, path, data = None, headers = None):
		url = f"{self.api}/{path}"
		headers = headers if headers else self.headers
		response = requests.post(url, headers=headers, json=data)
		return response.json()
	
	def set_token(self, token):
		self.token = token
		self.headers["Authorization"] = f"Bearer {self.token}"
	
	def gen_token(self):
		data = {"initDataRaw": self.user_data}
		headers = {
			'Accept-Language': 'en-US,en;q=0.9',
			'Authorization' : 'authToken is empty, store token null',
			'Connection': 'keep-alive',
			'Origin': 'https://hamsterkombat.io',
			'Referer': 'https://hamsterkombat.io/',
			"User-Agent": "Mozilla/5.0 (Linux; Android 12; MR91GPAQ Build/GH2S.20514.244; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.172 Mobile Safari/537.36",
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-site',
		}
		response = self.request("auth/auth-by-telegram-webapp", data=data, headers=headers)
		self.set_token(response["authToken"])
		return response
	
	def auth(self):
		self.gen_token()
		return self.request("auth/me-telegram")
	
	def sync_clicker(self):
		response =  self.request("clicker/sync")
		self.available_taps = response['clickerUser']["availableTaps"]
		self.max_taps = response['clickerUser']["maxTaps"]
		self.balance_coins = response['clickerUser']["balanceCoins"]
		return response
		
	def tap(self, max_taps, available_taps):
		data = {"count": max_taps, "availableTaps": available_taps, "timestamp": int(time.time())}
		return self.request("clicker/tap", data=data)
	
	def upgrade(self, upgrade_type):
		data = {"boostId": upgrade_type, "timestamp": int(time.time())}
		return self.request("clicker/buy-boost", data=data)
	
	def boost_max_taps(self):
		return self.upgrade("BoostMaxTaps")
	
	def autoclick(self):
		while True:
			data = self.sync_clicker()['clickerUser']
			available_taps = data["availableTaps"]
			if available_taps >= 10:
				time.sleep(1)
				self.tap(data["maxTaps"], data["availableTaps"])
			time.sleep(1)

	def autoprint(self):
		while True:
			print(f"{'='*10}\nCoins: {self.balance_coins}\nTaps: {self.available_taps} / {self.max_taps}")
			time.sleep(2)
	
	def autofarm(self, taps: bool = True, upgrades: bool = False, print_info: bool = True):
		if taps:
			Thread(target=self.autoclick, args=()).start()
		if upgrades:
			print("Upgrades will be added soon!")
		if print_info:
			time.sleep(2)
			Thread(target=self.autoprint, args=()).start()

if __name__ == "__main__":
	client = HamsterClient()
	client.auth()
	client.autofarm(taps=True, print_info=True)
