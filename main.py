from hamsterpy import HamsterClient

client = HamsterClient()
client.auth()
client.autofarm(taps=True, print_info=True)