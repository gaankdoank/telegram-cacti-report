import telebot
import mysql.connector
import json
import datetime
from datetime import datetime
from mysql.connector import Error

bot = telebot.TeleBot("753045927:AAEOjo9tmoDBj0dUip9-qGg2jdGc2k5boWw")

try:
 	connection = mysql.connector.connect(host='localhost',
                             database='cacti',
                             user='root',
                             password='ibs123')
 	if connection.is_connected():
       		db_Info = connection.get_server_info()
       		print("Connected to MySQL database... MySQL Server version on ",db_Info)
       		cursor = connection.cursor()
       		cursor.execute("SELECT description,hostname FROM host WHERE status='1'")
       		record = cursor.fetchall()
       		print ("Total Row(s)", cursor.rowcount)
		#bot.reply_to(287076189,record)
		#while record is not None:
		#for row in record:
		#	print(row)
		data = []
		#for row in record:
	#		datetime = datetime.datetime(row[2])
	#		print(datetime)
		print json.dumps(record, sort_keys=True, indent=4, separators=(',',':'))
		#bot.send_message(287076189,"Automatic hosts Checked, the following offline devices : \n ============================= \n \n"+json.dumps(record,sort_keys=True, indent=4, separators=(',',':')))
		bot.send_message(-367111902,"Automatic hosts Checked, the following offline devices : \n ============================= \n \n"+json.dumps(record,sort_keys=True, indent=4, separators=(',',':')))
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

