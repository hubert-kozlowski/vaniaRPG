import argparse
import logging
import random
import sys

from functions.LeaveGame import leaveGame
from functions.screens import (Fight, Inventory, Shop, Stats, menuScreen,
                               startScreen)
from functions.screens.startScreen import startScreen

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    parser = argparse.ArgumentParser(description='Your Game Description')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Debug mode enabled")

    try:
        logging.info("Game started")
        startScreen()
    except Exception as e:
        logging.exception("An unexpected error occurred:")
        # Optionally, handle the error gracefully or exit the game

if __name__ == "__main__": # If the script is being executed directly
    main() # Run the game
