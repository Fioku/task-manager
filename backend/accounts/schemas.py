from datetime import datetime
from django.contrib.auth.models import User
from ninja import Schema
from ninja.orm import create_schema

UserSchema = create_schema(User)

class UserSchema(Schema):
    id: int
    username: str
    first_name: str
    last_name: str
    password: str
    last_login: datetime
    is_superuser: bool
    email: str