import os

from bson import ObjectId
from pydantic_mongo import AbstractRepository
from pymongo import MongoClient
from app.models.deck import Deck

MONGO_DETAILS = os.environ.get('MONGODB_URI')

client = MongoClient(MONGO_DETAILS)

database = client['top-trumps-fast-api']

deck_collection = database.get_collection("decks")


class DeckRepository(AbstractRepository[Deck]):
    class Meta:
        collection_name = 'decks'


deck_repository = DeckRepository(database=database)


async def find_decks():
    decks = []
    for deck in deck_repository.find_by({}):
        decks.append(deck)
    return decks


async def find_deck(id_: str):
    deck = deck_repository.find_one_by_id(ObjectId(id_))
    if deck:
        return deck


async def create_deck(deck: Deck):
    result = deck_repository.save(deck)
    if result.inserted_id:
        return deck


async def update_deck(id_: str, deck: Deck):
    existing_deck = deck_repository.find_one_by_id(ObjectId(id_))
    if existing_deck:
        deck.id = ObjectId(id_)
        result = deck_repository.save(deck)
        if result.modified_count:
            return deck


async def delete_deck(id_: str):
    result = deck_repository.delete_by_id(ObjectId(id_))
    return result.deleted_count > 0
