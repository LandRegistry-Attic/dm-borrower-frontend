class DeedApiInterface(object):
    def __init__(self, implementation):
        self.implementation = implementation

    def get_deed(self, deed_reference):
        return self.implementation.get_deed(deed_reference)
