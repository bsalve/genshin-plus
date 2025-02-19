import genshin
import asyncio
import subprocess
import json

# Function for claiming daily checkin rewards with client cookies
async def claim_daily_checkin(genshin_config):

    ltuid_v2 = genshin_config["ltuid_v2"]
    ltoken_v2 = genshin_config["ltoken_v2"]

    client = genshin.Client({"ltuid_v2": ltuid_v2, "ltoken_v2": ltoken_v2})

    client.default_game = genshin.Game.GENSHIN
    client.region = genshin.Region.OVERSEAS

    try: 
        await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        print("Already claimed dailies for today! Check again tomorrow.")
        return
    except genshin.InvalidCookies:
        print("Cookies are invalid. Please double check everything is correct.")
        return

# Opens Genshin game and attempts to claim daily checkin
async def main():

    try:
        with open("genshin_config.json", "r") as f:
            genshin_config = json.load(f)
            GamePath = genshin_config["GamePath"]
            await claim_daily_checkin(genshin_config)

            if GamePath != "":
                subprocess.Popen(GamePath, shell=True)

    except FileNotFoundError:
        with open("genshin_config.json", "w") as f:
            json.dump({"GamePath": "", "ltuid_v2": "", "ltoken_v2": ""}, f)

asyncio.run(main())