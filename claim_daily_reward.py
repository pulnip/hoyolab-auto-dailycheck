from genshin import Game, Client, InvalidCookies, AlreadyClaimed

async def claim(ltuid: str, ltoken: str, ltmid: str):
    target_games=[
        Game.GENSHIN, Game.STARRAIL,
        Game.ZZZ
    ]
    client=Client(
        lang="ko-kr",
        cookies={
            "ltuid_v2": ltuid,
            "ltoken_v2": ltoken,
            "ltmid_v2": ltmid
        }
    )

    for g in target_games:
        status="❌"

        try:
            await client.claim_daily_reward(game=g)
            status="✅"
        except(InvalidCookies, AlreadyClaimed) as e:
            status="🟡"
        
        _, day=await client.get_reward_info(game=g)
        rewards=await client.get_monthly_rewards(game=g)
        reward=rewards[day-1]

        print(f"Claimed[{status}]: {reward.name} x{reward.amount}")

if __name__ == "__main__":
    import os
    import asyncio

    ltuid=os.getenv("HOYO_LTUID")
    ltoken=os.getenv("HOYO_LTOKEN")
    ltmid=os.getenv("HOYO_LTMID")

    asyncio.run(claim(ltuid=ltuid, ltoken=ltoken, ltmid=ltmid))
