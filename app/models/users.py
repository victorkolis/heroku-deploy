from pydantic import BaseModel, Field, validator


class User(BaseModel):
    # "COMPOSITION", Data Modeling
    id: str = Field(None, description='Id do usuário')
    name: str = Field(None, description='Nome do usuário')

    @validator('name')
    def must_have_name(cls, name):
        if not name:
            raise Exception('Usuário sem nome')
        return name.title()
