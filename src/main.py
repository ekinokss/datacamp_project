from src.db import init_db
from src.cli import main_menu

#entry point
if __name__ == "__main__":
    init_db()
    main_menu()