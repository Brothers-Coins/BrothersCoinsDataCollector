from src.controller.app_manager import Manager

if __name__ == '__main__':
    manager = Manager()
    data = manager.get_transactions()
