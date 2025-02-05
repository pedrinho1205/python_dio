from typing import Annotated

from pydantic import Field
from desafio_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(
        description="nome da categoria", examples="Scale", max_length=10)]
