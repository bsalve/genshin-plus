import genshin
import asyncio
import sys
import subprocess

# Replace 0 and 1 with your ltuid and ltoken, respectively. 
client = genshin.Client({"ltuid": 0, "ltoken": "1"})

# Replace with your path to genshinimpact.exe
genshin_path = (r"PATH_GOES_HERE")

# Function for claiming daily checkin rewards with client cookies
async def claim_daily_checkin(client):
    client.default_game = genshin.Game.GENSHIN
    client.region = genshin.Region.OVERSEAS

    try: 
        await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        return
    except genshin.InvalidCookies:
        sys.stdout.write("Cookies are invalid. Please double check everything is correct.")

# Opens Genshin game and attempts to claim daily checkin
async def main():
    await claim_daily_checkin(client)

    subprocess.Popen(genshin_path, shell=True)

asyncio.run(main())