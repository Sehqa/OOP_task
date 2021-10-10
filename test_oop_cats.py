from fast_cat import FastCat
from slow_cat import SlowCat

fast_cats = FastCat([123312])
print(fast_cats._color)
slow_cats = SlowCat('white')
fast_cats.meow()
fast_cats.run()
fast_cats.jump()
slow_cats.meow()
fast_cats.hearVacuumCleaner()
slow_cats.hearVacuumCleaner()
slow_cats.jump()

