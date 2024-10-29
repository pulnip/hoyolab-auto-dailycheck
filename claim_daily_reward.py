from genshin import Game, Client, InvalidCookies, AlreadyClaimed

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

    async def claim(self):
        client=Client(
            lang="ko-kr",
            cookies={
                "ltuid_v2": self.ltuid,
                "ltoken_v2": self.ltoken,
                "ltmid_v2": self.ltmid
            }
        )

        for game in self.target_games:
            try:
                await client.claim_daily_reward(game=game)
                status="✅"
            except(InvalidCookies, AlreadyClaimed) as e:
                status="🟡"
            
            _, day=await client.get_reward_info(game=game)
            rewards=await client.get_monthly_rewards(game=game)
            reward=rewards[day-1]

            print(f"User{self.id} Claimed[{status}]: {reward.name} x{reward.amount}")

if __name__ == "__main__":
    import os
    import asyncio

    account_num=int(os.getenv("HOYO_ACCOUNT_NUM"))
    ltuids=os.getenv("USERS_LTUID").split(",")
    ltokens=os.getenv("USERS_LTOKEN").split(",")
    ltmids=os.getenv("USERS_LTMID").split(",")
    users_games=os.getenv("USERS_TARGET_GAMES").split(",")
    accounts=[]

    for i in range(account_num):
        accounts.append(AccountInfo(id=str(i), ltuid=ltuids[i], ltoken=ltokens[i],
                                    ltmid=ltmids[i], games=users_games[i]))

    for account in accounts:
        asyncio.run(account.claim())
