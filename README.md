# MembershipBot
Telegram bot to create membership and license system in your group. User is banned/kicked after their subscription expires.

License redeem system.
Can handle multiple redeems to single user (adds more time in case membership already exists).

# How to setup

- Remove all the text from codes.txt and add your codes. Check codes_examples.txt for examples
- Modify bot.py and add your data (TOKEN, group_ip, OWNER_ID) and change reply messages to your needs
- Modify main.py and change the amount of seconds for each bot restart. (Less time = More restarts = More often checking if memberships expired or not)
- Leave it running 24/7

# How the bot works

- /start = Welcome message
- /help = Same as /start
- /redeem (code) - (E.g /redeem 09534295) Verifies if code exists in codes.txt, if valid, grabs user_id and adds membership
NOTE: You need to provide the group invite link on success redeem message. I highly recommend to enable manually approval on group configs.
