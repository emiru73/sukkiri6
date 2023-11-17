class Hero:
    # name = '松田'
    # hp = 100

# コンストラクタの書き方、初期化
# self.nameとageを宣言しているためHeroクラスに入っていることになるよって、上のフィールド宣言はいらない
    def __init__(self,name='松田',hp=32):
        self.name = name
        self.hp = hp

    def sleep(self, hours):
        print('{}は{}時間寝た！'.format(self.name, hours))
        self.hp += hours


print('スッキリファンタジーXII ～金色の理想郷～')
h = Hero()
# h.sleep(3)
# print('{}のHPは現在{}です'.format(h.name,h.hp))
# h = Hero('松田',3)
print('{}のHPは現在{}です'.format(h.name,h.hp))

# sum = (a,b)⇒ a+ b
# sum(5,10)