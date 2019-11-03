import os

from config import Config

def _saveUserPic(user,pic):
    '''
    returns path of the saved pic
    '''
    profilePicPath = os.path.join(Config.UPLOAD_FOLDER,user.email + pic.filename)
    pic.save(os.path.join("static",profilePicPath))
    return profilePicPath


def _updateUserPic(user,pic):
    '''
    returns true if pic has been updated otherwise false
    '''
    if pic and user.pic != pic:
        if user.pic != Config.DEFAULT_USER_PIC_LOCATIONS:
            os.remove(os.path.join("static",user.pic))
        user.pic = _saveUserPic(user,pic)
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


def extensionIsAllowed(pic):
    ext = pic.filename[pic.filename.rfind(".") + 1:]
    return ext in Config.ALLOWED_EXTENSIONS
