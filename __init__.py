from mycroft import MycroftSkill, intent_handler


class RememberStuff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('stuff.remember.intent')
    def handle_stuff_remember(self, message):
        self.speak_dialog('stuff.remember')


def create_skill():
    return RememberStuff()

