class person:
    def __init__(self, name_param):
        self.name = name_param
        print("hihi i'm", name_param, self)

    def talk(self):
        print("안녕하세요 저는 ",self.name, "입니다.")

person_1 = person("유재석")
person_1.talk()
person_2 = person("박명수")
person_2.talk()

