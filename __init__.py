from mycroft import MycroftSkill, intent_file_handler


class SkillRadio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.skill.intent')
    def handle_radio_skill(self, message):
        self.speak_dialog('radio.skill')


def create_skill():
    return SkillRadio()

