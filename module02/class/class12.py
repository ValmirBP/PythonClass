from nntplib import NNTPTemporaryError
from emoji import emojize
import emoji


color = {
    'bold'          : '\033[1m'
    ,'red'          : '\033[31m'
    ,'green'        : '\033[32m'
    ,'yellow'       : '\033[33m'
    ,'blue'         : '\033[34m'
    ,'redBold'      : '\033[1;31m'
    ,'greenBold'    : '\033[1;32m'
    ,'yellowBold'   : '\033[1;33m'
    ,'blueBold'     : '\033[1;34m'
    ,'end'          : '\033[m'

}

presentation = {
   'classStart' : ' CLASS 12 :snake: '
   ,'classEnd'  : ' CLASS 12 END :snake: '
}

emojiLst = {
    'cool'           : ':smiling_face_with_sunglasses:'
    ,'medalGold'     : ':1st_place_medal:'
    ,'medalSilver '  : '2nd_place_medal'
    ,'medal3rd'      : '3th_place_medal'
    ,'challenge'      : 'crossed_swords'
    ,'notSoSincere'  : ':grinning_face_with_sweat:'
}



print (" {} {:=^50} {}".format(color['greenBold'], emojize(presentation['classStart']), color['end']))

name = str(input("Type your name: ")).strip().capitalize()
if name == "Valmir":
    print("{} That is a  good name Mr {} {} {}".format(color['green'], name, color['end'], emojize(emojiLst['cool'])))
else:
    print("{} WoW!! Your name is good Mr {} {} {}".format(color['blue'], name, emojize(emojiLst['notSoSincere']),color['end']))


print (" {} {:=^50} {}".format(color['greenBold'], emojize(presentation['classEnd']), color['end']))