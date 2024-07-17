from rubpy import Client
from rubpy.types import Updates
import time
import numexpr as ne
import threading 

MAX_LEN = 50
COOLDWON_DURATION = 5
HELP_TEXT = open('help.txt', encoding="UTF-8").read()

variables = {
    "pi": 3.141592653589793,
    "e": 2.718281828459045,
    "k": 1000
}

cooldowns = {}

def main():
    bot=Client(name="MathBot")

    @bot.on_message_updates()
    async def hello(message: Updates):
        if(message.is_me):
            return
        
        if(not message.is_private):
            await message.reply("ربات فقط در پیوی کار می کند 📗")
            return

        if(not message.is_text): return
    
        if(len(message.text) > MAX_LEN):
            await message.reply("متن زیادی بزرگ است 🔴")
            return

        if(message.text == "?" or message.text == "؟"):
            await message.reply(HELP_TEXT)
            return
        
        if(message.author_guid in cooldowns):
            if(cooldowns[message.author_guid]):
                await message.reply("لطفا قبل از ارسال هر درخواست چند ثانیه صبر کنید 🕗")
                return

        is_valid = ne.validate(message.text.lower(), global_dict=variables) != None
        if(is_valid): return

        result = str(ne.evaluate(message.text.lower(), global_dict=variables))
        await message.reply("🌍 ننتیجه محاسبه: " + result)

        # cooldown_thread = threading.Thread(target= lambda: cooldown_handler(message.author_guid))
        # cooldown_thread.start()
    
    bot.run()

def cooldown_handler(guid):
    cooldowns[guid] = True
    time.sleep(COOLDWON_DURATION)
    print("COOLDOWN_RESET_DONE")
    cooldowns[guid] = False

if(__name__ == "__main__"):
    main()