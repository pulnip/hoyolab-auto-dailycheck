# hoyolab-auto-dailycheck

[![Claim Daily Reward](https://github.com/pulnip/hoyolab-auto-dailycheck/actions/workflows/claim-daily-reward.yml/badge.svg)](https://github.com/pulnip/hoyolab-auto-dailycheck/actions/workflows/claim-daily-reward.yml)

## Usage

### 🌐Prerequisite

1. Go to [HoYoLab](https://www.hoyolab.com/) and sign-in your account
2. Find `ltuid_v2`, `ltoken_v2` and `ltmid_v2` in Cookies and Copy somewhere
    - You can find it from **developer tools > Storage > Cookie > `https://www.hoyolab.com`**
    - **NOT** `account_id_v2`, `account_mid_v2` and `cookie_token_v2`

### ⚙️Project Setup

3. Fork this repository
4. Go to **Settings > Secrets and variables > Actions**
5. Add the following environment variables to **Repository secrets**
- HOYO_ACCOUNT_NUM : (optional) the Number of your HoYoLab accounts
  - if you have multiple account, please set this var (2, 3, 4, ... etc)
  - not specified, 1 by default (single account assumed)
- **USER#_LTUID** : `ltuid_v2`, HoYoverse/HoYoLab UID of account number #
  - if you have single account, **USER0_LTUID** should be specified.
  - if you have multiple account, **USER0_LTUID** and **USER1_LTUID** ...(and so on) should be specified.
- **USER#_LTOKEN** : `ltoken_v2`, personal HoYoLab API access token of account number #
- **USER#_LTMID** : `ltmid_v2` Another key value to access API of account number #
- PREFER_LANG : (optional) the Language of the information printed at _Actions_
  - `zh-cn`, `zh-tw`, `de-de`, `en-us`, `es-es`, `fr-fr`, `id-id`, `it-it`, `ja-jp`, `ko-kr`, `pt-pt`, `ru-ru`, `th-th`, `vi-vn`, `tr-tr`
  - not specified, `en-us` by default

### 🎁Claim Result

- Go to **Actions** Tab in your repository.
- There is **Claim Daily Reward** action will be shown on the left
- click the result of the **workflow run** (whether run manually or triggered by a schedule).
![image](https://github.com/user-attachments/assets/307a5614-020f-4ddb-a7dc-b06e9558d3b1)
  - 🟡 for claimed more than once, ✅ for first claim
- Great! Now, you don't need to manually claim daily reward.

### ⚠️Notice

Setting a schedule cron variable as a repository variable is not possible due to GitHub policies.
- By default, it is set to UTC+21(KST+6),
- but if you want to change it, please edit the [workflow.yml](.github/workflows/claim-daily-reward.yml) file directly.

## 📝References

- [anime_game_daily_login_autocheck](https://github.com/Baiker000/anime_game_daily_login_autocheck)
- [genshin-auto-daily-check-in-docker](https://github.com/Bing-su/genshin-auto-daily-check-in-docker)

## License

All the content in this repository is licensed under the [MIT License](LICENSE.txt).

Copyright (c) 2024 pulnip