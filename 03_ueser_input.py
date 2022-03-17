from __future__ import division
from tokenize import Double

from pkg_resources import load_entry_point


Ueser_name = input("what's your name? :)")
print()
fav_num = int (input("what's your favourit number?"))
if fav_num == 6:
    print("oh that's my favourit number too")
print()
Double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num
print("hi {}, your favourite number is {}".format(Ueser_name, fav_num))
print()
print("but your favourit number Doubled is {} did you know that?".format(Double))
print()
print("and your favourit number halfed  is {}".format (half))
print()
print("your favourit number squared  is {}".format (squared))
print()
print("bye and thank you for doing this with me :)")