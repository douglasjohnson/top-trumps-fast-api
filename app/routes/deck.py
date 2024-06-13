from fastapi import APIRouter, Path, Response, status

from app.database import (
    find_decks,
    find_deck,
    create_deck as repo_create_deck,
    update_deck as repo_update_deck,
    delete_deck as repo_delete_deck,
)
from app.models.deck import (
    Deck,
)


router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
async def get_decks():
    decks = await find_decks()
    if decks:
        return decks
    return []


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_deck(response: Response, id_: str = Path(..., alias="id")):
    deck = await find_deck(id_)
    if deck:
        return deck
    response.status_code = status.HTTP_404_NOT_FOUND


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_deck(deck: Deck, response: Response):
    saved_deck = await repo_create_deck(deck)
    if saved_deck:
        return saved_deck
    response.status_code = status.HTTP_400_BAD_REQUEST


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_deck(deck: Deck, response: Response, id_: str = Path(..., alias="id")):
    updated_deck = await repo_update_deck(id_, deck)
    if updated_deck:
        return updated_deck
    response.status_code = status.HTTP_404_NOT_FOUND


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_deck(response: Response, id_: str = Path(..., alias="id")):
    deleted = await repo_delete_deck(id_)
    if deleted:
        return
    response.status_code = status.HTTP_404_NOT_FOUND
