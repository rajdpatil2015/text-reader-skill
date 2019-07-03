from mycroft import MycroftSkill, intent_file_handler


class TextReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.text.intent')
    def handle_reader_text(self, message):
        self.speak_dialog('reader.text')


def create_skill():
    return TextReader()

