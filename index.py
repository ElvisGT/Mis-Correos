
import ezgmail

ezgmail.init()

all_mails = ezgmail.unread(maxResults='500')
mails_list = list()
accounts_arr = list()

#Almacenar todos los mails
for mail in all_mails:
    for message in mail.messages:
        msg_data = {
            'sender':message.sender,
            'body':message.body,
            'subject':message.subject,
            'timestamp':message.timestamp
        }
        mails_list.append(msg_data)

#Almacenar solamente el correo
for mail in mails_list:
    sender_arr = mail['sender'].split()
    account_sender = sender_arr[len(sender_arr) - 1]
    accounts_arr.append(account_sender)


#Contar correos
acc_count = dict()


for account in accounts_arr:
    #Eliminar simbolos de mayor-menor
    if account.startswith("<") and account.endswith(">"):
        new_acc = account[1:-1]
        #Contando correos
        acc_count[new_acc] = acc_count.get(new_acc,0) + 1


#Ordenando informacion por cantidad de correos
temp_tuple = tuple()
sorted_list_acc = list()
for k,v in acc_count.items():
    temp_tuple = (v,k)
    sorted_list_acc.append(temp_tuple)
    sorted_list_acc = sorted(sorted_list_acc,reverse=True)

#Mostrando informacion
for v,k in sorted_list_acc:
    print(f"{k} - {v}")
    