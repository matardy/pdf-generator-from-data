from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove,Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import os
import pandas as pd
from data_preprocessing import ExcelReader
from PDFGenerator import PDFGenerator
import os 


updater = Updater('5263400184:AAHhLANzxoE7thVGtMWOe9ufW6hruGsQnmU', use_context=True)
dispatcher = updater.dispatcher
# Global variables
CITY , EMB, MTR , DATE, ANALISIS, MATRIX = range(6)

city = '' 




def start(update: Update, context: CallbackContext):
    
    update.message.reply_text(
        'Bienvenido, este bot generará certificados en PDF una vez reciba:\n'
        '- Matriz en Excel con las Columnas: Nombre, Apellido, Cedula, Nacimiento, Estado. \n'
        '- Ciudad donde se realiza. \n'
        '- Embarcación.\n'
        '- Matricula de la embaración.\n'
        '- Fecha en la que se realiza.\n'
        '- Análisis que se realiza.\n'
        ''
        'Ingrese la ciudad donde se realiza: \n'

    )

    return CITY
    

def ciudad(update: Update, context:CallbackContext):
    context.user_data['city'] = update.message.text
   
    update.message.reply_text(
        'Ingrese el nombre de la Embaración: '

    )
    return EMB

    

def embarcacion(update: Update, context:CallbackContext):
    context.user_data['emb'] = update.message.text

    
    update.message.reply_text(
        'Ingrese la matricula: \n'
        'Pista: La matricula de sofia R es: P-04-00616 '
    )

    return MTR

    

def matricula(update: Update, context:CallbackContext):
    context.user_data['mtr'] = update.message.text

    update.message.reply_text(
        'Ingrese la fecha en la que se realiza la muestra: \n'
    )
    return DATE 

def fecha(update: Update, context: CallbackContext):
    context.user_data['date'] = update.message.text
    
    update.message.reply_text(
        'Ingrese el tipo de analisis: '
        'Ejm: Covid-19 Prueba rapida.'
    )
    return ANALISIS

def analisis(update: Update, context: CallbackContext):
    context.user_data['analisis'] = update.message.text
    update.message.reply_text(
        'Gracias, ahora porfavor envia la matrix con los datos en Excel. \n'
        'Recuerde que solo puede contener las columnas: Nombre, Apellido, Cedula, Nacimiento, Estado.'

    )
    
    return MATRIX

def matriz(update:Update, context: CallbackContext):
    update.message.reply_text('Generando certificados..')
    context.bot.get_file(update.message.document).download()

    file_name = str(os.popen('ls | grep .xlsx').read())
    file_name = file_name.rstrip('\n')
    df = ExcelReader(str(file_name))
    pdf = PDFGenerator()
    pdf.populate_pdf(df,context.user_data.get('city'), 'info@biselmed.com', '0958925173',context.user_data.get('emb'), context.user_data.get('date'), context.user_data.get('analisis'))
    
    pdf.output('/Users/gutembergmendoza/Stev/Python/PDF_generator/telegramBot/Certificates.pdf', 'F')
    update.message.reply_text('Certificados generados con exito! \n'
    'Para descargarlos presiona aqui: \n'
    '/descargar')
    #os.system("python3 main.py")
    return ConversationHandler.END


def descargar(update: Update, context):
    filename = 'Certificates.pdf'
    context.bot.send_document(chat_id = update.message.chat_id, document = open('/Users/gutembergmendoza/Stev/Python/PDF_generator/telegramBot/Certificates.pdf', 'rb'), filename = 'Certificates.pdf')
    os.system('rm /Users/gutembergmendoza/Stev/Python/PDF_generator/*.xlsx*')


def get_input(update:Update, context: CallbackContext):
    CITY = update.message.text
    update.message.reply_text("Ingrese la ciudad: ")
    user = update.message.from_user
    print(CITY)




    
     # writing to a custom file
def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )
    print(CITY)

    return ConversationHandler.END

def help(update: Update, context: CallbackContext):
    #reply_keyboard = [['Prueba', 'Girl', 'Other']]
    query = update.callback_query 
    querydata = query.data 
    context.user_data['key'] = querydata
    print(context.user_data['key'])
   



conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states = {
        CITY: [MessageHandler(Filters.text,ciudad)],
        EMB: [MessageHandler(Filters.text, embarcacion)], 
        MTR: [MessageHandler(Filters.text, matricula)], 
        DATE:[MessageHandler(Filters.text, fecha)], 
        ANALISIS: [MessageHandler(Filters.text, analisis)],
        MATRIX: [MessageHandler(Filters.document,matriz)], 
    }, 
    fallbacks = [CommandHandler('cancel', cancel)],
)

def main(): 
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(CommandHandler('descargar', descargar))
    # dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(MessageHandler(Filters.text, ciudad))
    # dispatcher.add_handler(MessageHandler(Filters.text, embarcacion))
    # dispatcher.add_handler(MessageHandler(Filters.text, matricula))
    # dispatcher.add_handler(MessageHandler(Filters.text, fecha))
    # dispatcher.add_handler(MessageHandler(Filters.text, analisis))




    #updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))
    #updater.dispatcher.add_handler(CommandHandler('certificates', certificates))
    print(city)
    updater.start_polling()
    updater.idle()
    print(city)
def trying(): 
    print(city)

if __name__ == '__main__':
    main() 
    trying()