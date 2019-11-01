import os

from config import Config


def _updateUserPic(user,pic):
    if user.pic != pic:
        if user.pic != Config.DEFAULT_USER_PIC_LOCATIONS:
            os.remove(os.path.join("static",user.pic))
        user.pic = pic
        return True
    return False



def updateUser(user,*,username,email,password,pic):
    change = False

    if user.username != username:
        change = True
        user.username = username

    if user.email != email:
        change = True
        user.email = email

    if password and user.password != password:
        change = True
        user.password = password

    change = _updateUserPic(user,pic)

    if change:
        user.insert()
