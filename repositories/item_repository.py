from models.item import Item
from extensions import db

class ItemRepository:
    @staticmethod
    def get_all():
        return Item.query.all()

    @staticmethod
    def get_by_id(item_id):
        return Item.query.get(item_id)

    @staticmethod
    def create(item_data):
        new_item = Item(**item_data)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def update(item_id, item_data):
        item = ItemRepository.get_by_id(item_id)
        if not item:
            return None
        for key, value in item_data.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    @staticmethod
    def delete(item_id):
        item = ItemRepository.get_by_id(item_id)
        if not item:
            return None
        db.session.delete(item)
        db.session.commit()
        return item
