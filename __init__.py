from mycroft import MycroftSkill, intent_file_handler


class Answer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('answer.intent')
    def handle_answer(self, message):
        self.speak_dialog('answer')


def create_skill():
    return Answer()

