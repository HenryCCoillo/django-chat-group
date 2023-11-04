
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
import json

from .models import Message, Room

# quiero implementar una autenticacion en django channels
class DashboardConsumerView(AsyncJsonWebsocketConsumer):
    async def connect(self):        

        self.user = self.scope['user']

        if self.user.is_authenticated:
            self.dashboard_slug = self.scope['url_route']['kwargs']['dashboard_slug']
            self.room_group_name = f'chat-{self.dashboard_slug}'

            await self.channel_layer.group_add(self.room_group_name,self.channel_name)        
            
            await self.accept()

            # Usamos sync_to_async para obtener la sala
            await self.get_room(self.dashboard_slug, True)
        
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "user_join","user":self.list_user}
            )
        
        else:
            await self.close()
        

    async def disconnect(self, close_code):
        print(f'Conncection close with code:{close_code}')
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        await self.get_room(self.dashboard_slug, False)
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "user_leave","user":self.user.username}
        )
        
        # self.room.remove_user_from_online(self.user)

    async def receive(self,text_data):
        if self.user.is_authenticated:
            text_data_json  = json.loads(text_data)
            message = text_data_json["message"]

            # Guardar los datos en la base de datos
            await self.save_data_item(self.user,message,self.dashboard_slug)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message,"user":self.user.username}
            )

        else:
            await self.close()

    # Receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def user_join(self, event):
        await self.send(text_data=json.dumps(event))

    async def user_leave(self, event):
        await self.send(text_data=json.dumps(event))


    @database_sync_to_async
    def create_data_item(self,user,message,slug):
        room = Room.objects.get(slug=slug)
        return Message.objects.create(user=user,room=room,content=message)

    async def save_data_item(self,user,message,slug):
        await self.create_data_item(user,message,slug)

    @database_sync_to_async
    def get_room_item(self, dashboard_slug,online):
        self.rooms = Room.objects.get(slug=dashboard_slug)
        if online:  
            self.rooms.online.add(self.user)
            self.list_user = [user.username for user in self.rooms.online.all()]
        else:
            self.rooms.online.remove(self.user)

        return Room.objects.get(slug=dashboard_slug)

    
    async def get_room(self,dashboard_slug,online):        
        self.room = await self.get_room_item(dashboard_slug,online)
