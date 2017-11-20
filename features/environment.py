
from fixture.application import Application


def before_scenario(context,scenario):
    context.app = Application()


def after_scenario(context,scenario):
    context.app.driver.quit()
    # pass

