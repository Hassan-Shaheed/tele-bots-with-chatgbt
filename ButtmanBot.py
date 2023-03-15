import telegram
import random
import time


# replace the bot token with your own bot token
bot = telegram.Bot(token=6133567465:AAF28PLM9A1PjeAudsrpo9BLROAGhSXkSMw)


# list of motivational messages in Arabic from Batman
messages = ["لدي سلاح واحد. لا أستسلم أبداً.",
            "لا يهم من أكون تحت السطح، بل ماذا أفعل.",
            "أنا الانتقام، أنا الليل، أنا باتمان.",
            "أنا باتمان.",
            "يمكن لأي شخص أن يصبح بطلاً. حتى رجل يفعل شيئًا بسيطًا ومطمئنًا مثل وضع معطف حول كتف الصبي الصغير ليخبره بأن العالم لم ينتهِ.",
            "الليل يكون أظلم قبل الفجر. وأعدك، الفجر قادم.",
            "أنا السبب في أن المجرمين يتنفسون بسهولة عندما يشرق الشمس.",
            "الأمر لا يتعلق بما أريد، بل بما هو عادل!",
            "الخفافيش ترعبني. حان الوقت لمشاركة أعدائي هذا الخوف.",
            "لست خائفاً من أن أكون صادقاً بعد الآن. لست خائفاً أيضاً من أن ينظروا إليّ كشخص شرير.",
            "أنا أرتدي قناعًا. وهذا القناع، ليس لإخفاء من أنا، ولكن لإنشاء من أنا.",
            "أسعى إلى وسيلة لمحاربة الظلم. لتحويل الخوف ضد أولئك الذين يفترسون الخائفين.",
            "لن أقتلك. لكنني لست مضطر

# function to send a random motivational message to the group
def send_motivational_message():
    message = "Motivation from Batman: " + random.choice(messages)
    bot.send_message(chat_id='@your_group_name_here', text=message)

# main function to run the bot and send messages every 2 hours
def main():
    while True:
        send_motivational_message()
        time.sleep(10)

if __name__ == '__main__':
    main()
