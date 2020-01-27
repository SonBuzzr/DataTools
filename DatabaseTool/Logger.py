import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format="%(asctime)s: %(levelname)s: \n%(message)s",
)

logging.warning('This will get logged to a file')