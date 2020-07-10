class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class NullHandler(object):
    def __init__(self, handler):
        self.handler = handler

    def handle(self, obj, event=None):
        if self.handler:
            return self.handler.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event=None):
        if event.field_type == int:
            if event.field_value:
                obj.integer_field = event.field_value
            elif event.field_value == 0:
                obj.integer_field = event.field_value
            else:
                return obj.integer_field
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event=None):
        if event.field_type == float:
            if event.field_value:
                obj.float_field = event.field_value
            elif event.field_value == 0.0:
                obj.float_field = 0.0
            else:
                return obj.float_field
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event=None):
        if event.field_type == str:
            if event.field_value:
                obj.string_field = event.field_value
            elif event.field_value == '':
                obj.string_field = event.field_value
            else:
                return obj.string_field
        else:
            return super().handle(obj, event)


class EventGet(object):
    def __init__(self, field_type):
        self.field_type = field_type
        self.field_value = None


class EventSet(object):
    def __init__(self, field_value):
        self.field_value = field_value
        self.field_type = type(field_value)


# if __name__ == '__main__':
#     obj = SomeObject()
#     obj.integer_field = 42
#     obj.float_field = 3.14
#     obj.string_field = "some text"
#     chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
#     print(chain.handle(obj, EventGet(int)))
#     print(chain.handle(obj, EventGet(float)))
#     print(chain.handle(obj, EventGet(str)))
#     chain.handle(obj, EventSet(0))
#     print(chain.handle(obj, EventGet(int)))
#     chain.handle(obj, EventSet(0.0))
#     print(chain.handle(obj, EventGet(float)))
#     chain.handle(obj, EventSet(''))
#     print(chain.handle(obj, EventGet(str)))
