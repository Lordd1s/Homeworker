import pickle


class Airplane:
    def charactery(self):
        print("Speed: ~700km/h")
        print("Color: White")
        print("Company name: Fly Arystan")


fly_arystan = Airplane()
fly_arystan.charactery()

with open('fly_arystan.pickle', 'wb') as by:
    pickle.dump(fly_arystan, by)

with open('fly_arystan.pickle', 'rb') as byby:
    new = pickle.load(by)

print(new)
