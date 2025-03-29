from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    #print(group_info)
                    groups_info.append(group_info)
        return groups_info
    except Exception as e:
        print(e)
        return []

async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []

async def logUserBot():
    load_dotenv()
    api_id = int(29917243)
    api_hash = "79f2c6c5756f3622339e1bcbc895b5a4"
    phone_number = "51916017269"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)

    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmstreamly", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4772417777")

    # @client.on(events.NewMessage)
    # async def my_event_handler(event):
    #     # Verificar si el mensaje proviene de un chat privado
    #     if event.is_private:
    #         sender = await event.get_sender()
    #         sender_id = sender.id
    #         message = event.message.message
    #         # Responder solo en chats privados
    #         await client.send_message(sender_id, "Esta es una cuenta solo de Spam. Si estas interesado en algun servicio, escríbeme en @ indicando el servicio.")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@spmstreamly", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>", parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam"] and i['group_id'] not in[-1001697833157,-1001766344706,-1001188565789,-1001466371297,-1001417452208,-1001538693959,-1001833726352,-1001245528374,-1001860642360,-1001407944624,-1001797335984,-1001334983901,-1001878771766,-1001496268564,-1001297580019,-1001344804867,-1001874564897,-1001468410810,-1001400929051,-1002013714959,-1001767286812,-1001350471615,-1001974938642,-1001250029579,-1001141226142,-1001882740795,-1001678259754,-1001781855275,-1001089223194,-1001486248056,-1001154432305,-1001223907779,-1001955809129,-1001508095827,-1001225510423,-1001252405524,-1001658442088,-1001690153909,-1002129491365,-1001477403365,-1001451159315,-1001925756345,-1001845385041,-1001940782387,-1001925378942,-1001955958482,-1001412789657,-1001514551287,-1001464703314,-1001468854109,-1001911929545,-1001376670660,-1001152963122,-1001826153639,-1001983920380,-1002096926310]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.forward_messages(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spmstreamly", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spmstreamly", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        else: break
                        await asyncio.sleep(10)
                        if j==2: break
            await client.send_message("@spmstreamly", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(300) 
        except:
            pass

if __name__ == "__main__":
    asyncio.run(logUserBot())
