from rubpy import Client
from rubpy.types import Updates
import time
import numexpr as ne

MAX_LEN = 50
HELP_TEXT = open('help.txt', encoding="UTF-8").read()

VARIABLES = {
    "pi": 3.141592653589793,
    "e": 2.718281828459045,
    "k": 1000
}

async def validation_middleware(message: Updates):
    if(message.is_me): return False
    
    if(not message.is_text): return False
    
    if(not message.is_private):
        await message.reply("ربات فقط در پیوی کار می کند 📗")
        return False

    if(len(message.text) > MAX_LEN):
        await message.reply("متن زیادی بزرگ است 🔴")
        return False
    
    return True

def main():
    bot=Client(name="MathBot")

    @bot.on_message_updates()
    async def help(message: Updates):
        validation_result = await validation_middleware(message)
        if not validation_result: return

        if(message.text == "?" or message.text == "؟"):
            await message.reply(HELP_TEXT)
            return

    @bot.on_message_updates()
    async def math(message: Updates):
        validation_result = await validation_middleware(message)
        if not validation_result: return

        is_valid = ne.validate(message.text.lower(), global_dict=VARIABLES) != None
        if(is_valid): return

        result = str(ne.evaluate(message.text.lower(), global_dict=VARIABLES))
        await message.reply("🌍 ننتیجه محاسبه: " + result)
    

    bot.run()

if __name__ == "__main__":
    main()