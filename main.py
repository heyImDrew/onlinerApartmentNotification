import time
from src.updater import Updater


if __name__ == '__main__':

    # Getting the Updater object to perform loop apartment updating
    updater = Updater()

    # Getting user preferences
    updater.load_settings()

    # Running the updater once in given time
    updater.run()
    while True:
        updater.update()
        time.sleep(updater.delay)
