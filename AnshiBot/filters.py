# AnshiBot/filters.py

abusive_words = [
    "badword1", "badword2", "mc", "bc", "madarchod", "bhosdike", "chutiya"
    # Add more words you want to block
]

banned_sticker_ids = [
    "CAACAgUAAxkBAAEGZg5lGv",  # Sample sticker file_id start
    # Add sticker file_ids you want to block
]

def check_abuse(text):
    return any(word.lower() in text.lower() for word in abusive_words)

def check_sticker(message):
    return message.sticker and message.sticker.file_id.startswith(tuple(banned_sticker_ids))
