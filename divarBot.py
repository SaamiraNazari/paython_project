from telebot.types import Update
from  telegram import Update
from telegram.ext import    ApplicationBuilder,ContextTypes,MessageHandler,filters,CommandHandler
from caper import get_avg_price_from_divar


token='8184048243:AAFiyURmBfVBA7HVh-mFLj5TZ-hz9PmOJ1o'

async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query=update.message.text.strip()
    await update.message.reply_text(f'در حال جستجو برای {query}')

    avg=get_avg_price_from_divar(query)
    if avg:
        await update.message.reply_text(f'میانگین قیمت {avg} تومان')
    else:
        await update.message.reply_text('نتیجه ای یافت نشد')
app=ApplicationBuilder().token(token).build()
app.add_handler(MessageHandler(filters.TEXT, handle_query))
app.run_polling()