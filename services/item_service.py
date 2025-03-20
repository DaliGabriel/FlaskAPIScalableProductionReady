from repositories.item_repository import ItemRepository

class ItemService:
    @staticmethod
    def get_all_items():
        return ItemRepository.get_all()

    @staticmethod
    def get_item_by_id(item_id):
        return ItemRepository.get_by_id(item_id)

    @staticmethod
    def create_item(item_data):
        return ItemRepository.create(item_data)

    @staticmethod
    def update_item(item_id, item_data):
        return ItemRepository.update(item_id, item_data)

    @staticmethod
    def delete_item(item_id):
        return ItemRepository.delete(item_id)
