import os
import requests
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from pymongo import MongoClient

# Set up logging
# credit by @cyber_ansh 
# api used by anshapi 
#
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Apna bot token daalo na meri jaan 
TELEGRAM_BOT_TOKEN = "8077840807:AAEjwYQJ3N3vzLnYfaaxJty9yOternFcvXM"
IMGBB_API_KEY = "d6cb513ea3d93fa748b4c0d3965df795"
IMGBB_UPLOAD_URL = "https://api.imgbb.com/1/upload"

# Apna mongo db daalo 
MONGO_URI = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['telegram_bot']
users_collection = db['users']

# imgbb image upload karne ka function 
async def upload_to_imgbb(image_path):
    with open(image_path, "rb") as file:
        response = requests.post(IMGBB_UPLOAD_URL, data={"key": IMGBB_API_KEY}, files={"image": file})
    if response.status_code == 200:
        return response.json().get("data", {}).get("url")
    return None

# Function to handle image messages
async def handle_image(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_path = f"temp_{photo.file_id}.jpg"
    
    processing_msg = await update.message.reply_text("Processing your image... ⏳")
    
    await file.download_to_drive(file_path)
    image_url = await upload_to_imgbb(file_path)
    os.remove(file_path)
    
    await context.bot.delete_message(chat_id=update.message.chat_id, message_id=processing_msg.message_id)
    
    if image_url:
        await update.message.reply_text(f"Here is your image URL: {image_url}")
    else:
        await update.message.reply_text("Failed to upload image. Please try again later.")

# Function to handle new users
async def new_user(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_id = user.id
    username = user.username or "No Username"
    
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id, "username": username})
        logging.info(f"New user added: {username} ({user_id})")
        await update.message.reply_text("Welcome to the bot! 🎉")


# Broadcast message to all users
async def broadcast(update: Update, context: CallbackContext):
    if update.message.from_user.id == 6258915779:  # Replace with your Telegram ID
        message = update.message.text.replace("/broadcast", "").strip()
        users = users_collection.find()

        for user in users:
            user_id = user.get("user_id")  # Use `.get()` to avoid KeyError
            if user_id:
                try:
                    await context.bot.send_message(chat_id=user_id, text=message)
                except Exception as e:
                    logging.warning(f"Failed to send message to {user_id}: {e}")
            else:
                logging.warning(f"User entry missing 'user_id': {user}")

        await update.message.reply_text("Broadcast sent successfully!")
    else:
        await update.message.reply_text("You are not authorized to use this command.")

# Start command
async def start(update: Update, context: CallbackContext):
    await new_user(update, context)
    keyboard = [
        [InlineKeyboardButton("Aᴘɪ", url="https://t.me/+7AUuVrP8F69kYWY1"), InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Ur_support07")],
        [InlineKeyboardButton("ᴏᴡɴᴇʀ", url="t.me/cyber_ansh"), InlineKeyboardButton("ᴀᴅᴍɪɴ", url="t.me/Rishu1286")],
        [InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="t.me/UR_RISHU_143")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_photo("https://i.ibb.co/BH7zhrSq/temp-Ag-ACAg-UAAxk-BAAIBRmf-Wqp1e-T6-Bt-GSf0yy-M5c-EPxw0-X5-AAJbwz-Ebw-QTJVXY2-Do-Hd250-YAQADAg-ADe.jpg", caption= f"ᴛʜɪs ʙᴏᴛ ɢɪᴠᴇ ʏᴏᴜ ᴘᴜʙʟɪᴄ ʟɪɴᴋ ᴏғ ᴀ ɪᴍᴀɢᴇ.\nʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴍᴇ ᴀɴʏ ɪᴍᴀɢᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴘᴜʙʟɪᴄ ʟɪɴᴋ ᴏғ ɪᴍᴀɢᴇ.", reply_markup=reply_markup)

# Main function
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    
    app.run_polling()

if __name__ == "__main__":
    main()
