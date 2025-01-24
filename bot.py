import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace 'YOUR_TOKEN' with your bot's API token
TOKEN = '7572493486:AAGmdrhwlgoZ9T_CCHPPxslPQgokggwTFRo'
OWNER_CHAT_ID = '6258915779'  # Owner's chat ID to receive messages

# List of images
IMAGES = [
    'https://envs.sh/9xo.jpg',
    'https://envs.sh/9-x.jpg',  # Replace with your actual image URLs
    'https://envs.sh/r7R.jpg',
    'https://envs.sh/r7C.jpg',
    'https://envs.sh/r7Y.jpg',
    'https://envs.sh/rEL.jpg',
    'https://envs.sh/o-9.jpg',
]

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Select a random image from the list
    random_image = random.choice(IMAGES)
    
    # Send a photo with inline buttons and a custom caption
    caption = (
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿\n"
        " ᴛʜɪs ɪs ᴄʜᴧᴛ ᴡєʙ ʙσᴛ ʙʏ @cyber_ansh\n"
        " ᴛʜɪs ɪs σηʟʏ ᴛєsᴛɪηɢ ʙσᴛ\n"
        " ᴄʟɪᴄᴋ ʟɪᴠє ᴄʜᴧᴛ ʙυᴛᴛση ᴄʜᴧᴛ ʟɪᴠє\n"
        " ʏσυ ᴄᴧη ʙυʏ ᴘꝛєϻɪυϻ ᴘσꝛᴛғσʟɪσ ᴡєʙsɪᴛє  ᴛєϻᴘʟᴧᴛєs\n"
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿"
    )
    await update.message.reply_photo(
        photo=random_image, 
        caption=caption,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("sυᴘᴘσꝛᴛ", url='http://t.me/ans_X_bot'),  # Direct link to the channel
                InlineKeyboardButton("σᴡηєꝛ", url='http://t.me/cyber_ansh')  # Direct link to the owner's channel
            ],
            [
                InlineKeyboardButton("ᴡєʙ ᴛєϻᴘʟᴧᴛєs", url='https://lighthearted-frangipane-95d886.netlify.app/'),  # Direct link to the website
                InlineKeyboardButton("ʟɪᴠє ᴄʜᴧᴛ", url='https://anshu908.github.io/chat_gpt_web/')  # Add your web chat URL here
            ]
        ])
    )

# Message handler to forward messages to the owner
async def forward_to_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.send_message(chat_id=OWNER_CHAT_ID, text=update.message.text)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_owner))

    application.run_polling()

if __name__ == '__main__':
    main()
