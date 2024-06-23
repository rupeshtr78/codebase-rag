import logging

logger = logging.getLogger(__name__)
# set up the logger
logger.setLevel("INFO")

console_handler = logging.StreamHandler()
console_handler.setLevel("INFO")

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
