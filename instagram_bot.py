from instapy import InstaPy

session = InstaPy(username = "tony_banks_g", password = "kaj501btoyota")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["love", "instagood", "photooftheday", "fashion", "like4like"], amount =3)

session.end()
