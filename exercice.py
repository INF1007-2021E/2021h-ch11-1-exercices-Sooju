from game import *

class Weapon:
	def __init__(self, name, attack_dmg, level):
		self.__name = name
		self.attack_dmg = attack_dmg
		self.level = level

	def make_unarmed(self):
		self.__name = "Unarmed"
		self.attack_dmg = 20

	def show(self):
		print(self.__name)
		print(self.attack_dmg)
		print(self.level)

class Character:
	def __init__(self, name, max_hp, attack, defense, level, weapon, hp):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp = hp

	def compute_damage(self, a, d):
		crit = 1
		if random.random() < 1/16:
			crit = 2

		randomize = random.uniform(0.85, 1)
		dmg = (((((2 * a.level/5) + 2) ** a.attack * a.attack/d.defense)/50 + 2) * (crit * randomize))

		return dmg


	def show(self):
		print(self.__name)
		print(self.max_hp)
		print(self.attack)
		print(self.defense)
		print(self.level)
		print(self.weapon)
		print(self.hp)


def main():
	weapon1 = Weapon("Broken Blade", 15, 1)
	weapon1.make_unarmed()
	weapon1.show()

	character_a = Character("Riven", 100, 5, 15, 1, "Broken Blade", 100)
	character_b = Character("Pikachu", 75, 10, 20, 1, "Thunder Bolt", 75)
	print(character_a.compute_damage(character_a, character_b))


if __name__ == "__main__":
	main()

