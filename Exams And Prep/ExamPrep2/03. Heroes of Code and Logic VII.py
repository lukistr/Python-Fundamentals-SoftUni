num_heroes = int(input())

heroes = {}

for _ in range(num_heroes):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {'HP': int(hp), 'MP': int(mp)}

while True:
    command = input()
    if command == "End":
        break

    action, *args = command.split(" - ")

    if action == "CastSpell":
        hero_name, mp_needed, spell_name = args
        mp_needed = int(mp_needed)
        if heroes[hero_name]['MP'] >= mp_needed:
            heroes[hero_name]['MP'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        hero_name, damage, attacker = args
        damage = int(damage)
        heroes[hero_name]['HP'] -= damage
        if heroes[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif action == "Recharge":
        hero_name, amount = args
        amount = int(amount)
        recovered = min(200 - heroes[hero_name]['MP'], amount)
        heroes[hero_name]['MP'] += recovered
        print(f"{hero_name} recharged for {recovered} MP!")

    elif action == "Heal":
        hero_name, amount = args
        amount = int(amount)
        recovered = min(100 - heroes[hero_name]['HP'], amount)
        heroes[hero_name]['HP'] += recovered
        print(f"{hero_name} healed for {recovered} HP!")

for hero_name, stats in heroes.items():
    print(f"{hero_name}\n  HP: {stats['HP']}\n  MP: {stats['MP']}")
