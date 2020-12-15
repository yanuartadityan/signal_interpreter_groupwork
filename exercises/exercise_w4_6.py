""" exercise_w4_6.py """
import logging.config
import yaml

with open("log_settings.yaml", "r") as yfile:
    config = yaml.safe_load(yfile.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


def bus_validator():
    """ bus_validator """
    try:
        user_age = int(input("Enter your age: "))
        logger.info("User entered age: %d", user_age)
    except ValueError as err:
        print("You have entered an invalid input")
        logger.error("Error occurred %s", err)
    else:
        if user_age >= 24:
            print("Congratulations, you are old enough to drive a bus")
            logger.info("User is old enough to drive")
        else:
            print(f"Sorry, you have to wait {24-user_age} more years to drive a bus")
            logger.info("User is not old enough to drive")
    finally:
        print("Good bye!")
        logger.info("Bus validator is finished")


if __name__ == "__main__":
    bus_validator()
