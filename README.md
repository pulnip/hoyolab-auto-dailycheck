# hoyolab-auto-dailycheck

## Usage

### Prerequisite

1. Go to [HoYoLab](https://www.hoyolab.com/) and sign-in your account
2. Find `ltuid_v2`, `ltoken_v2` and `ltuid_v2` in Cookies and Copy somewhere
    - You can find it from **developer tools > Storage > Cookie > `https://www.hoyolab.com`**

### Project Setup

3. Fork this repository
4. Go to **Settings > Secrets and variables > Actions**
5. Add the following environment variables to **Repository secrets**
- **HOYO_LTUID** : `ltuid_v2`, Your HoYoverse/HoYoLab UID
- **HOYO_LTOKEN** : `ltoken_v2`, Your personal HoYoLab API access token
- **HOYO_LTMID** : `ltmid_v2` Another key value to access API

## References

- [anime_game_daily_login_autocheck](https://github.com/Baiker000/anime_game_daily_login_autocheck)
- [genshin-auto-daily-check-in-docker](https://github.com/Bing-su/genshin-auto-daily-check-in-docker)

## License

All the content in this repository is licensed under the [MIT License](LICENSE.txt).

Copyright (c) 2024 pulnip
