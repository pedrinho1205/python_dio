from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

from desafio_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(
        description="Nome do Atleta", examples="Joao", max_length=50)]
    cpf: Annotated[str, Field(
        description="Cpf do Atleta", examples="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", examples=25)]
    peso: Annotated[PositiveFloat, Field(
        description="Peso do Atleta", examples=75.5)]
    altura: Annotated[PositiveFloat, Field(
        description="Altura do Atleta", examples=1.7)]
    sexo: Annotated[str, Field(
        description="Sexo do Atleta", examples="M", max_length=1)]
