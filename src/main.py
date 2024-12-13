import logging
import platform

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:  # noqa: D103
    logger.info(platform.python_version())


if __name__ == "__main__":
    main()
