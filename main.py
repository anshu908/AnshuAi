import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace 'YOUR_TOKEN' with your bot's API token
#created by @cyber_ansh
TOKEN = '7572493486:AAGmdrhwlgoZ9T_CCHPPxslPQgokggwTFRo'
OWNER_CHAT_ID = '6258915779'  # Replace with the owner's chat ID

# List of images
IMAGES = [
    'https://envs.sh/9xo.jpg',
    'https://envs.sh/9-x.jpg',
    'https://envs.sh/r7R.jpg',
    'https://envs.sh/r7C.jpg',
    'https://envs.sh/r7Y.jpg',
    'https://envs.sh/rEL.jpg',
    'https://envs.sh/o-9.jpg',
]

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_image = random.choice(IMAGES)
    caption = (
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿\n"
        " ᴛʜɪs ɪs ᴄʜᴧᴛ ᴡєʙ ʙσᴛ ʙʏ @cyber_ansh\n"
        " ᴛʜɪs ɪs σηʟʏ ᴛєsᴛɪηɢ ʙσᴛ\n"
        " ᴄʟɪᴄᴋ ʟɪᴠє ᴄʜᴧᴛ ʙυᴛᴛση ᴄʜᴧᴛ ʟɪᴠє\n"
        " ʏσυ ᴄʟɪᴄᴋ ʟɪɴᴋ ғσʀ ᴘꝛєϻɪυϻ ᴡєʙ ᴛєϻᴘʟᴧᴛєs\n"
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿"
    )
    await update.message.reply_photo(
        photo=random_image,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("sυᴘᴘσꝛᴛ", url='http://t.me/ans_X_bot'),
                InlineKeyboardButton("σᴡηєꝛ", url='http://t.me/cyber_ansh')
            ],
            [
                InlineKeyboardButton(
                    "ᴡєʙ ᴛєϻᴘʟᴧᴛєs", 
                    web_app=WebAppInfo(url="https://lighthearted-frangipane-95d886.netlify.app/")
                ),
            ]
        ])
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_image = random.choice(IMAGES)
    caption = (
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿\n"
        "ʜᴏᴡ ᴄᴀɴ ɪ ʜᴇʟᴘ ʏᴏᴜ?\n"
         "@cyber_ansh\n"
        "ᴘʟᴇᴀsᴇ sᴇʟᴇᴄᴛ ғʀᴏᴍ ᴛʜᴇ ᴏᴘᴛɪᴏɴs ʙᴇʟᴏᴡ:\n"
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿"
    )
    await update.message.reply_photo(
        photo=random_image,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ᴄσηᴛᴧᴄᴛ", url="http://t.me/cyber_ansh"),
            ],
            [
                InlineKeyboardButton("ʟᴇᴀʀɴ ᴍᴏʀᴇ", url="https://proansh.vercel.app/"),
            ],
            [
                InlineKeyboardButton(
                    "ᴄʜᴀᴛʙᴏᴛ",
                    web_app=WebAppInfo(url="https://matrixgpt.vercel.app/")
                )
            ]
        ])
    )

# Message handler to forward messages to the owner
async def forward_to_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.send_message(chat_id=OWNER_CHAT_ID, text=update.message.text)

# Main function to set up the bot
def main():
    # Initialize the application with the bot token
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))
    
    # Add command handler for /help
    application.add_handler(CommandHandler("help", help_command))
    
    # Add message handler to forward messages to the owner
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_owner))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
