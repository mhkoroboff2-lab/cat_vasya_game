from character import Character
from spells import Fireball, IceLance

warrior = Character(10, 8, 12, 5, 6, 10, 'warrior')
mage = Character(5, 7, 8, 10, 15, 9, 'mage')

print(f"Воин: HP={warrior.max_health}, DMG={warrior.damage}, DEF={warrior.defense}, Mana={warrior.mana}")
print(f"Маг:  HP={mage.max_health}, DMG={mage.damage}, DEF={mage.defense}, Mana={mage.mana}")

mage.add_spell(Fireball())
mage.add_spell(IceLance())

print(f"\nМаг кастует Fireball: урон {mage.cast_spell(0)}, осталось маны {mage.mana}")
print(f"\nМаг кастует IceLance: урон {mage.cast_spell(1)}, осталось маны {mage.mana}")

try:
    mage.cast_spell(1)
except ValueError as e:
    print(f"Ожидаемая ошибка: {e}")
