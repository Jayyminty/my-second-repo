from character import Character

def main():
    hero = Character("Knight", 60, 5)
    enemy1 = Character("Goblin 1", 20, 3)
    enemy2 = Character("Goblin 2", 20, 3)
    enemies = [enemy1, enemy2]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(e.is_alive() for e in enemies):
        target = enemy1 if enemy1.is_alive() else enemy2
        hero.attack(target)

        for enemy in enemies:
            if enemy.is_alive() and hero.is_alive():
                enemy.attack(hero)

        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")


if __name__ == "__main__":
    main()