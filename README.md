#### discord-bots-and-hooks
Bots and hooks for managing our Discord server


#### Installation and Running (Moderation Bot)

Bot currently polls messages on #i-am-on-it channel. If the related
contribution is approved or rejected, it removes it.

It also removes all messages not starting with https://utopian.io.

```
$ git clone https://github.com/utopian-io/discord-automation
$ cd discord-automation
$ pip install -r requirements.txt
$ export =[BOT_TOKEN]
$ python3 utopian_bot/main.py
```

#### Installation and Running (Main Bot)

Bot currently sends a message to a specified channel every hour, unless the last message in the channel belongs to it. It also sends the same message if !help is used.

```
$ git clone https://github.com/utopian-io/discord-automation
$ cd discord-automation
$ pip install -r h_requirements.txt
$ export UB_TOKEN=[BOT_TOKEN]
$ python3 main_bot/app.py
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
