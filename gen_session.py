import asyncio
from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nDISINI OY, SALIN AJA,JNGN DI SEBAR!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
