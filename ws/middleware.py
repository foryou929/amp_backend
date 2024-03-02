from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken
from user.models import List as User


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        # Access the access token from the query string parameters
        access_token = scope["query_string"].decode().split("token=")[1]
        # JWTAuthentication().get_user(access_token)
        try:
            decoded_token = AccessToken(access_token)
            user_id = decoded_token.payload["user_id"]
            user = await self.get_user(user_id)
            scope["user"] = user
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return None
        return await self.inner(scope, receive, send)

    @database_sync_to_async
    def get_user(self, user_id):
        return User.objects.get(id=user_id)
