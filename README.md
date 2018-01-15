#### discord-bots-and-hooks
Bots and hooks for managing our Discord server


#### Installation and Running (Bot)

Bot currently polls messages on #i-am-on-it channel. If the related
contribution is approved or rejected, it removes it.

It also removes all messages not starting with https://utopian.io.

```
$ git clone https://github.com/utopian-io/discord-bots-and-hooks
$ cd discord-bots-and-hooks
$ pip install -r requirements.txt
$ export BOT_TOKEN=[BOT_TOKEN]
$ python3 utopian_bot/main.py
```


#### Installation (Hooks)

Posts to related discord channel once the contributions are approved or
rejected.


```
$ git clone https://github.com/utopian-io/discord-bots-and-hooks
$ pip install -r requirements.txt
$ cd discord-bots-and-hooks/hooks/
$ export DISCORD_HOOK_URL=[DISCORD_HOOK_URL]
$ export MYSQL_CONNECTION_STRING=[mysql+pymysql://user:pass@localhost/dbname]
$ python3 accepted_hook.py
$ python3 hidden_hook.py
```

All set.
