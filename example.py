class SomeExampleClass:
  def __init__(self):
    self.some_value = "A string of text"

  def an_instance_method(self):
    return self.some_value

  def an_instance_method_with_prefix(self):
    return "A prefix: " + self.some_value

  def do_addition(self):
    return 7 + 13
