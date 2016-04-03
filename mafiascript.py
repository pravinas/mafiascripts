import random

itemlist = {"Ammo " : 6,
"Antidote " : 5,
"Apple " : 3,
"BEES" : 5,
"Bloodthirsty Gun" : 0,
"Bullet removal kit" : 3,
"Combinator" : 9,
"Cookie " : 4,
"Election monitor" : 3,
"Enchanted <Heal>" : 0,
"Enchanted <Investigation>" : 0,
"Enchanted <Kill Utility>" : 0,
"Enchanted <Kill>" : 0,
"Enchanted <Useless>" : 0,
"Fire" : 0,
"Fire extinguisher" : 3,
"Flat Blade" : 3,
"Gasoline" : 0,
"Ghostly Essence" : 0,
"Glass Shards" : 3,
"Glass Shield" : 3,
"Gross <Food>" : 0,
"Gun" : 5,
"Gunpowder" : 3,
"Honey" : 2,
"Hunch" : 3,
"I'm Duckman!" : 4,
"Knife" : 5,
"Liquid Nitrogen" : 5,
"Magnetic field warper" : 1,
"Magnifying Glass" : 2,
"Missile defense system" : 1,
"Orange" : 3,
"Perfume" : 5,
"Poison " : 0,
"Poisoned Bullets" : 2,
"Prayer book" : 3,
"Present" : 5,
"Recipe Book " : 5,
"Roasted <Food>" : 0,
"Rocket <Item>" : 0,
"Rocketpack" : 0,
"Scope" : 5,
"Sharp Blade" : 2,
"Shovel" : 0,
"Sniper Rifle" : 0,
"Soap" : 3,
"Soda Bottle" : 3,
"Spring " : 5,
"Spring Cannon" : 4,
"Stick" : 6,
"Suicide Bomb" : 0,
"Taser" : 4,
"Tinfoil" : 3,
"Toilet Paper Tube " : 3,
"Turkish Delight" : 0,
"Twilight ritual" : 3
}

def weighted_choice():
   total = sum(itemlist.itervalues())
   r = random.uniform(0, total)
   upto = 0
   for choice in itemlist:
      if upto + itemlist[choice] > r:
         return choice
      upto += itemlist[choice]
   assert False, "Shouldn't get here"

print weighted_choice()
