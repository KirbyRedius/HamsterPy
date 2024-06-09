# HamsterPy

**HamsterPy** is created for auto-farming coins in **Hamster Kombat** (Telegram game)

# Instruction
## Add your user data

1.  Login to Telegram Web from your browser on PC
2.  Launch Hamster (you will receive an error asking you to log in from your phone)
3. Open **Inspect Element** -> go to the **Application** tab -> open **session storage** -> open sessions "https://hamsterkombat.io" -> click on the element **"__telegram__initParams"** -> copy the value **"tgWebAppData"**
> the result looks like **"user=%7B%22id%22%3A17599916624%2C%22first_name%22%3A%22KIRBY%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22KIRBYYY% 22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=906196156151&chat_type=private&start_param=kentId99999999999&auth_date=1665666&hash=3b6c05a 3733d4cdd0ece767477848e90d176141d5916f12ba0e8a65e07b8"**

4. copy the result and paste it into the **user.txt** file

## Start coding

> pip install hamsterpy

    from  hamsterpy  import  HamsterClient
    client  =  HamsterClient()
    client.auth()
    client.autofarm(taps=True, print_info=True)

# TODO
Soon it is planned to add auto-pumping of items
