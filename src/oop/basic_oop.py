class User:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def introduce(self):
        print(f"I'm {self.__name} and i'm {self.__age} year's old")


class UserController:
    users_inst = []

    def add_user(self):
        users_dict = [{"name": "이승훈", "age": 26}, {"name": "김승훈", "age": 27}, {"name": "박승훈", "age": 28}]
        for i in users_dict:
            self.users_inst.append(User(i["name"], i["age"]))

    def intro_user(self):
        for i in self.users_inst:
            i.introduce()


controller = UserController()
controller.add_user()
controller.intro_user()