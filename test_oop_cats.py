from fast_cat import FastCat
from slow_cat import SlowCat
from time import sleep

fast_cats = FastCat('black')
slow_cats = SlowCat('white')
fast_cats.meow()
fast_cats.jump()
slow_cats.meow()
fast_cats.hearVacuumCleaner()
slow_cats.hearVacuumCleaner()
slow_cats.jump()

