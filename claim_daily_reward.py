from genshin import Game

class AccountInfo:
    id: str
    ltuid: str
    ltoken: str
    ltmid: str
    target_games: list[Game]

    def __init__(self, id: str, ltuid: str, ltoken: str, ltmid: str, games: str):
        self.id=id
        self.ltuid=ltuid
        self.ltoken=ltoken
        self.ltmid=ltmid
        self.target_games=[]

        for s in games.split("+"):
            if(s=="HONKAI"):
                self.target_games.append(Game.HONKAI)
            elif(s=="TOT"):
                self.target_games.append(Game.TOT)
            elif(s=="GENSHIN"):
                self.target_games.append(Game.GENSHIN)
            elif(s=="STARRAIL"):
                self.target_games.append(Game.STARRAIL)
            elif(s=="ZZZ"):
                self.target_games.append(Game.ZZZ)

async def claim(account: AccountInfo, lang: str="ko-kr"):
    from genshin import Client, InvalidCookies, AlreadyClaimed

    client=Client(
        lang=lang,
        cookies={
            "ltuid_v2": account.ltuid,
            "ltoken_v2": account.ltoken,
            "ltmid_v2": account.ltmid
        }
    )

    for game in account.target_games:
        try:
            await client.claim_daily_reward(game=game)
            status="✅"
        except(InvalidCookies, AlreadyClaimed) as e:
            status="🟡"
        
        _, day=await client.get_reward_info(game=game)
        rewards=await client.get_monthly_rewards(game=game)
        reward=rewards[day-1]

        print(f"User{account.id} Claimed[{status}]: {reward.name} x{reward.amount}")

if __name__ == "__main__":
    import os
    import asyncio

    preferred_lang=os.getenv("PREFER_LANG")
    if preferred_lang is None:
        preferred_lang="en-us"

    account_num=os.getenv("HOYO_ACCOUNT_NUM")
    if account_num is None:
        account_num = 1
    else:
        account_num = int(account_num)
    
    accounts=[]

    for i in range(account_num):
        accounts.append(AccountInfo(
            id=str(i),
            ltuid=os.getenv(f"USER{i}_LTUID"),
            ltoken=os.getenv(f"USER{i}_LTOKEN"),
            ltmid=os.getenv(f"USER{i}_LTMID"),
            games=os.getenv(f"USER{i}_TARGET_GAMES")
        ))

    for account in accounts:
        asyncio.run(claim(account, preferred_lang))
