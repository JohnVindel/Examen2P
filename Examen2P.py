#*****Examen Segundo Parcial*****#
import telebot

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['tabla-unidades'])
def foto(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('/Users/John Vindel/Downloads/Tabla de Convercion.png', 'rb')
    bot.send_photo(id, photo)
#    print("Archivo Imagen")

@bot.message_handler(commands=['formula-cuadratica'])
def foto(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('/Users/John Vindel/Downloads/Formula Cuadratica.png', 'rb')
    bot.send_photo(id, photo)
#    print("Archivo Imagen")

@bot.message_handler(commands=['documento', 'pdf'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    document = open('/Users/John Vindel/Downloads/Codex Examen.pdf', 'rb')
    bot.send_document(id, document)
    print("Documento PDF")

@bot.message_handler(commands=['ubicacion', 'ubicación', 'gps'])
def documento(mensaje):
    bot.send_chat_action(id, 'find_location')
    bot.send_location(id, 15.49564557067027, -87.99124599749254)
    bot.reply_to(mensaje, "Universidad UCRISH, San Pedro Sula, Cortes, Honduras")
    print("Ubicacion")



bot.polling()
