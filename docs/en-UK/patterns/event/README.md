# Event

A module that contains two functions. One to subscribe to a specific event, and the other to post an event when it occures. Each event is stored in a dictionary. This utility ONLY DEALS WITH THE CREATING, AND POSTING THE EVENTS; this module does not include a way to implement or activate the controlling mechanism in the design pattern. A simple way to implement the design pattern involves functions that setup handlers to each event. The example I will use in this instance is a logging handler from my unreleased Login software using the [Logger](#) defined in this code base.

Example:

```python
"""
When two things are happening at once in a function, it is an indicator of low cohesion; high coupling; overall bad design; and an indicator that the event pattern should be used.
"""
import utils
import system # system found in the example code base
import i18n # internationalization library

# individual functions to handle what happens during each event
def handle_application_start(ui: str, logger: utils.Logger) -> None:
    logger.log(i18n.t("general.logs.application_start", ui_name=ui.upper()))

def handle_user_registered_event(user: system.User, logger: utils.Logger) -> None:
    logger.log(i18n.t("general.logs.user_registered", name=user.name), utils.LoggingLevel.INFO)

def handle_user_logged_in_event(user: system.User, logger: utils.Logger) -> None:
    logger.log(i18n.t("general.logs.user_login", name=user.name), utils.LoggingLevel.INFO)

def handle_user_password_forgotten_event(user: system.User, logger: utils.Logger) -> None:
    logger.log(i18n.t("general.logs.reset_password", name=user.name), utils.LoggingLevel.INFO)

def handle_user_upgrade_plan_event(name: str, plan: str, logger: utils.Logger) -> None:
    logger.log(i18n.t("general.logs.upgrade_plan", name=name, plan=plan), utils.LoggingLevel.INFO)

def handle_application_end(logger: utils.Logger) -> None:
    logger.log(i18n.t("general.logs.application_end"))

# one function to run each of the individual function
def setup_log_event_handlers(logger: utils.Logger):
    utils.subscribe("application_start", lambda ui: handle_application_start(ui, logger))
    utils.subscribe("user_registered", lambda user: handle_user_registered_event(user, logger))
    utils.subscribe("user_logged_in", lambda user: handle_user_logged_in_event(user, logger))
    utils.subscribe("user_password_forgotten", lambda user: handle_user_password_forgotten_event(user, logger))
    utils.subscribe("user_upgrade_plan", lambda args: handle_user_upgrade_plan_event(*args, logger=logger))
    utils.subscribe("application_end", lambda _: handle_application_end(logger))
```