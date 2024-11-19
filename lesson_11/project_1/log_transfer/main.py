import logging

from log_config import configure_logging
from mongo import get_last_doc, put_docs
from elastic import get_new_docs

logger = logging.getLogger(__name__)


def main() -> None:
    configure_logging(level=logging.INFO)
    logger.info("Starting Logs transfer script")
    last_doc = get_last_doc()
    new_docs = get_new_docs(last_doc["@timestamp"])
    if len(new_docs) > 0:
        put_docs(new_docs)


if __name__ == "__main__":
    main()
