from Chef import Chef
class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")
    # Overwrite
    def make_special_dish(self):
        print("The chef makes orange bbq ribs.")