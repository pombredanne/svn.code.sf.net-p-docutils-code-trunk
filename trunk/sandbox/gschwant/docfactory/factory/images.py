"""
:author:  Dr. Gunnar Schwant
:contact: g.schwant@gmx.de
:version: 0.2.5
"""

#----------------------------------------------------------------------
# This file was generated by img2py.py
#
from wxPython.wx import wxBitmapFromXPMData, wxImageFromBitmap
import cPickle, zlib
from wxPython.wx import wxImageFromStream, wxBitmapFromImage
import cStringIO


def getLogoSmallData():
    return cPickle.loads(zlib.decompress(
'x\xda\x8d\x90=\x0b\x830\x10\x86w\x7f\xc5\x81_%\x81#\x96"\x8eZ\xc1\xd5\xc1\
\xc5U\x1c+\xd8\xff?\xf5\xde\x8b\x89\xba\xf5U\x02\xcfs\x17/\xf1\xb1}\xabd*\
\xab\x9a\xf0>\xa9*\x93e*\x99Vzo\xcb\xfaQ\xca\x84\xd2A\xa3<\x83\x9d\xe4\xe0\
\xd1\xf308\xa7\xdc\x82kW\x87\xba\x01\xf7\xae\x0f\x9c\x82\x9b\xb3\x9e{n\x02\
\x93\x9f\x87\t\xca\x16\xfcr\xafP\xdf\xc3y\x8ez\x01\xee\\\x17\xf7\xf3-\xe4\
\xaf4kv\x84\xc7\x91\x83\x94\x06,j/r\x97u\x14+\xe5\x8b\xdcgVI\xf4\xaf\xbco\
\xc7\x0c\xc99H\xb46Y\x0e\x9d\xf1\xf0\xd6\xda6=\x0eO\x19\x9e\x0c\x92\xd3<tB\
\x12\xc1\x11\x17\xe6\x94\x19:e\xaf\xb8(5\xb2\xb70&~\xd3GF\x99\xf8\x97(\x06Jo\
\xc4?\x8a\x04u\xfa' ))

def getLogoSmallBitmap():
    return wxBitmapFromXPMData(getLogoSmallData())

def getLogoSmallImage():
    return wxImageFromBitmap(getLogoSmallBitmap())

#----------------------------------------------------------------------
def getLogoBigData():
    return cPickle.loads(zlib.decompress(
'x\xda\x8d\x94Ko\xc20\x10\x84\xef\xfc\nKyPa\xb12m\x84\xb8D\nE\xca\x95\x03\
\x17_\x11\xc7"\xa5\xff\xff\xd4\x9d];qL(\x8c\x90\xea\xe9~\x9d]?\xe8\xc7\xfdw\
\xb7\xba\xac\xbf>\r\x7fv\x8d\xd9\xadW\xd7\xcb\x9a\xcc\xcd|\xdf\xaf\xb7\x1fq[\
v\x85s\x07\xd7\xf7\xe2\x0b\xf8^$\xdek\xdd\xc5\xfaY}\xdf;\'\xbe\x84\xdf\xbb}\
\xac\xb7\xf0\'w\x8a\xbe\x82?Lu\xa3\xf9\x07\xd7\xe8\xdf\xd7Z\x1f\xfb[\xad\xa3\
\xa3\xf8\x0e\xbea:\xd4\x878_\xa8o\xe0\x8f\xee8\xe6S\x94\xaeL\xf8\x85\t\xd2#\
\xf0Q4@Dg\x11YQ\x0e\x05j\x88\x14r\x12H\xf2\xf1\xd3Z\x920\xc4!j\x06\xf1 \x83\
\xd2g\xa6\x90AH\x9aC\x1a\xc0\x0b\xb4\xe1\x15\x87\x10\xd9\x17\x90\xd1y^&Y\xf3\
F\x92}#\xe9\r\x88\x8b\x0b\x83\x83\xe2\x95\x15\ne>\x82\x1cb\x8d\x87\x08J\x0fs\
\x0e\xcd\xef\x84\x9eC\x9e\xe2\x05\x93\xbatp;>\x95\xb8\xf2\xbe\xebt\x84\x1126\
U\xf2&\xb0\x9f\t*\xe2\x07\x1b\xf7\xc8\xe9\xba\xb2\xac\xea\xfa\x1f\xa8\x0bP\
\xf5\x04\xa2\xc0\x101R\xd7\x1eS=B\xda\x0c3\x03\xaa\xfd\x02\xc4ck\x0e27\x9b\
\xb6]\x80\xf89F\xc8\n\xb4\x90\xc4B\xbbmY\xa1\x1d\xe7,\xb4\x93Sb\n\xfb\xd2f\
\x8f\x83\x07\x91\xc7\xbe\x800\x94\x1fAT\n\xe5\'\x9e]\x8b\xcc\x93_\xcb$\xbd`\
\x9dgv\xc1E&}*\xc6$_\xf3\xf9+\xd0=JJ\xfa\x0f\xc3\xbc\x10C\xf4\x07\xe7\xd5-h'\
 ))

def getLogoBigBitmap():
    return wxBitmapFromXPMData(getLogoBigData())

def getLogoBigImage():
    return wxImageFromBitmap(getLogoBigBitmap())

#----------------------------------------------------------------------
def getProjectData():
    return cPickle.loads(zlib.decompress(
'x\xda]\x90\xb1\n\x840\x0c\x86\xf7{\x8a@\xb5\x1e\x14B\x0b"\x8ez\x82k\x07\x17\
Wq<\xa1\xf7\xfe\xd3\xa5\x899\xeb\xfdt\xf9\xbe\xfe\t\xb4\xcf\xe3\x13\x1eK\x13\
:\xc8\'@h\x1e\xdb\xd2 \xec\xf0:\xb6\xfd\xcd\xb4\x12\x99\x99\xd2zfP\x9eg\xe6!\
s\xe7;\x7f\xb2\xcd<\xf9I\xd9d\xee\xaf\xfbJ\xb8W\x8e\xb2o\xf4^\xf6\'\xe1I\xd9\
en}\xab\xfd:\xf3\xe8Ge\x00\xa4\xc0/"Y\xe0]"\xac\x14\xae\xf3\x80\xc8\x95\x03\
\xda\x17\x99\x12\x16Qy\xedK\xa02\x9e\x0b\xa8\x16\xd7\xbb$\xe5\x8aq\x92\x89\
\xf6:\xe7\x06s\x97\xd4sh\xaaR\xc6\x98]\xc4\xda\xa2\xbeHB\xb3\xe4TJh\xb6\xb6T\
\xbcKD\xcb\xef,%\xeb\xeb\x97\xfeB\x12\xbf\x98zjg' ))

def getProjectBitmap():
    return wxBitmapFromXPMData(getProjectData())

def getProjectImage():
    return wxImageFromBitmap(getProjectBitmap())

#----------------------------------------------------------------------
def getFile1Data():
    return cPickle.loads(zlib.decompress(
'x\xda\xd3\xc8)0\xe4\nV74S\x00"\x13\x05Cu\xae\xc4`\xf5|\x85d\x05\xa7\x9c\xc4\
\xe4l0O\x01\xc8Sv\x03\x030?\x02\xc4w6p6\x80\xf2\xf5@|\x0b\x03\x10\x84\xa8\
\xd7\x83\x03\x05\x10\x80\n*@A\x84\x1e6A0\x13.\x98\x0f\x02`\x12C%Pm>\xbaJ\xa0\
\xb2\x88A\xad2\x02\x01\xe0\x82\xf9\xc8\x00&\x88\x06\x80\x82z\x00lj[\xe4' ))

def getFile1Bitmap():
    return wxBitmapFromXPMData(getFile1Data())

def getFile1Image():
    return wxImageFromBitmap(getFile1Bitmap())

#----------------------------------------------------------------------
def getLinkData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4gz\xba8\x86T\xcc\
\xb9:\xd1\x91\xaf\xc1\x80\x83\xe5\xe0\x8f\xff\xfa\xfd\xe2\x01J\t+\xe6\xdd\
\xf1\x9e=\xcd\xaf\xdc\xd1\xd5\xc1k\xe5\xda\xb3[3_\xcb13\xb1\\\x10JXw\x9f!dW\
\xdc\x9b\xc9\xcfo,\x08Qn\xb1|\xc0\xf9m%{\x83\xf5\x89k\xcb\xac\x94\xafX\xae\
\xff\xfc\xfb\xdeT\xa5\x10\xd7\xa9{\xce1,\x99\xbf\x9c\x8b\xef\x9e\xe3)M\x9fd\
\x91\x86Rq\xf6S\xef4\xc5]Z\xc3N\x01-e\xf0t\xf5sY\xe7\x94\xd0\x04\x00\t\x8e?\
\x85' )

def getLinkBitmap():
    return wxBitmapFromImage(getLinkImage())

def getLinkImage():
    stream = cStringIO.StringIO(getLinkData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getImageData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\xf7z\xba8\x86T\xcc\
9\x1a\xec\xc8\xd5`\xc0\xe3}\xb4\xfd%{\xcd\xe5_\xaa\x07w\xdf\xfb\x1bl\xe3\xb3\
tv\xe8\x1c.\xb1S7<6M\xc8c\x9aP\x11xU\xfa\x93:Si\xcc\x13\xc6\xa93\x99?\xd51;,\
\xbev\xf0\xee\xef\xbe\xba\xd7\xc6\x13X\xe3z5\x05-\xbc\x0fqu.\xd3\xa8\xe7z\
\xe5\xfd4%>\x819r\xc3\xaa\x9b\xec\xf1\x0b\xe4\x8f){\xa8\xce{\xbfd\n\xcf\x0c\
\x9e];\xcf20:8\x98\xfb\xeb]\x14\xe9\x9c\xe1\x1fi\xde\xc8\xb0\xd3\xea\xc1?\
\x03/\xef\xba\xff\xbd\xdc\xcf/\xb9\\\xfb\xb4`}3\xd0a\x0c\x9e\xae~.\xeb\x9c\
\x12\x9a\x00\x90]PH' )

def getImageBitmap():
    return wxBitmapFromImage(getImageImage())

def getImageImage():
    stream = cStringIO.StringIO(getImageData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getOpenData():
    return zlib.decompress(
"x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4W{\xba8\x86T\xccY\
\x1a\xec\xc9w@\x81\xa3e\x19\xff\xf3\xe7\x97\xbb\x05\\X\xa5<{\xa47;Lal\xd0{\
\xf4V\xc5p\xf3\xda\xc5\xf7.32oX\x98b5\x9d%\xf0\xe2d\x81^!\xa3nk\xf7\xcbvI\
\x87j_\x1d\x939\xe3\xa9\xfe\xf4o\xe5\xcdf\xadiBF[%\x18\xae\t\xcd\xe8t\xc9\
\xda\xf0\xccG\xf5\x0f\xe3\xea\\\xe5\x0f\t\x13\x8d'\xb2\x0b\xf7\xcaUx\xc7>m] \
|\xbb\xbc\xe0\xa7\xe4\xfb\xfb\x07\xd9\xd9\xa5\x9c\xf8\x1f\xecJ\xf2\x05:\x83\
\xc1\xd3\xd5\xcfe\x9dSB\x13\x00\x15\x16EI" )

def getOpenBitmap():
    return wxBitmapFromImage(getOpenImage())

def getOpenImage():
    stream = cStringIO.StringIO(getOpenData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getNewData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\x07{\xba8\x86T\xcc\
INI\xf8\xf1\x7f~#\xd3\x81\xa6\x04#\xa1\x80\xae\xbbrb"\xaa\x162\x87O\x9c\xe0\
\xd8\xca\x10<\xaf\xb3akF[\xf2\xaeI\x19\xcc\n\xeb\x12\x0e\x18\xb4\xb0\x06k\
\xea\xdd\xbe\xc8\xabt\x91u\xc7\x81\x15\x8c\xcd\x07\x19\xa6\x944\xc8\x1dW\x91\
r\x88[\xb6\xe4\x067\xc3\xf1W|:\xa9.g\xc4\x80\xc63x\xba\xfa\xb9\xacsJh\x02\
\x00\x18\x0c1\x97' )

def getNewBitmap():
    return wxBitmapFromImage(getNewImage())

def getNewImage():
    stream = cStringIO.StringIO(getNewData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getPasteData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4/\xf4tq\x0c\xa9\x98\
\xb3tr\xa0P\x93\x01\x8f\x8b9\xcf\xf5\x027\xff,\x1b\xcd\xd2\x0fr\x1f\x95\xd3&\
]\x9a\x12vw=\xd3\xcd\xed\xd1\x0bX:\x1e\xf0\xaf\xfd\x99k\x15\xf3\xdd\xf8\xda\
\x1d\x86\x13\xcb%\x04\xe72q6\x18\xfcVN3]}\xf1\xfaq\xc9f\x9d\x89\xa7y\xa6\xe4\
\x1e\xdf\xbc\'`\xdb\xde(w\x87M\xac\xd7\xbf\x96\x9dT\xb7^\xc5\xb0wJ\xe6\x01\
\xfd\rz\x0c\x1f\xf4\x05S\xf5\xafo1\x11\x16\x0e2\xe8\x95\xcex\xa4,\xf1\xde\
\xb7[\xf1\x80O\xe9.\xe7}Y\x13\x1c=\xf9\x83\x7fk\x1f\xdf"\xe3\xc3p\x84\xe1\
\xe5\x89\x152\x0c\x96\xb7\x0f\xdd\xd1\xacg\xae`r\xba\xee;u\xc9r\xa0c\x19<]\
\xfd\\\xd69%4\x01\x00\xaaxW\x00' )

def getPasteBitmap():
    return wxBitmapFromImage(getPasteImage())

def getPasteImage():
    stream = cStringIO.StringIO(getPasteData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getCopyData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe47y\xba8\x86T\xccY:9\
\x90\xaf\xc1\x80\xc3\xb9\xfb\xe3\xbdc\x93\xaf\xf3\x1f\x94\xdc \xdd\xf97U{}\
\x8e\x84\xc3\xa3v\x9e\x06\x83\x17?\xa5\x18\x8c\x1cgD\xdeN\tn\xbd}%\xe4\xe7E\
\xbb]\xf3\xea>z\x88\xdcT\xb9\xf8H\xd9I\xa2d\x91h\xd3T\x8f]\x82\xd5,\xef3\x9a\
\x13\x8eD\n\x1d\xf1YT\xddwY\xed\xc42\xc1\xe4O\x13\x03\xdafHW\xb0\x94\x9e\x10\
d=\xf8zJV\xf0\xfc@\x81\x8c\xab+\xc3}y\xaaN\xab\x94/\\\xcd\xfd\xea\xa0\xc7\
\xac\xb8\x1bb \xa72x\xba\xfa\xb9\xacsJh\x02\x00\x80\xa5K\xbe' )

def getCopyBitmap():
    return wxBitmapFromImage(getCopyImage())

def getCopyImage():
    stream = cStringIO.StringIO(getCopyData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getCutData():
    return zlib.decompress(
"x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\xe7{\xba8\x86T\xcc\
Y;\xc9\x9b\xaf\xc1\x80\xc3E\xf6\xf1\xde\xd9\xf3d\xc2%\xbc\x12/<xs\xeb\xc0\
\x87\x1f\x0e.O2^\xf4\xd81^(\xcf\xbc\xa0\xf6\xe3\xa8\xc3F\xc9\xba\xac\x07\xcf\
O=\xf3\x89^\xb1*\x98ymT\xae\xe4MY\x86\xcb3z\xdf\xb3\x98\t\xce\xe8^x\xf5\xa8\
\x96\xbb\xdb\xbc4\xc5\x0b\x0cmo\xae\xda-Y\xcb\xaa?\xf1\xe3\x16\xd1\x89\xb9\
\xd1\t\x07'^2\xddw\x957h\xa2\xd9D\x1b\x9b\x8e\x87@\xab\x19<]\xfd\\\xd69%4\
\x01\x00\xb0TE\xc8" )

def getCutBitmap():
    return wxBitmapFromImage(getCutImage())

def getCutImage():
    stream = cStringIO.StringIO(getCutData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getRedoData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\x17{\xba8\x86T\xcc\
9;\xe94o\x83\x82\x80\x0b{\xb2\xf257\xc5\x04E\xef\xa6\xde\xc8S\x15\x02\xc2\
\xfb\xdaN0\xde\xcfm\xbf+~c\x81\x87\x10\xb3\x8e\xf2\xe1\xff\x02k\n\x1f\xdea\\\
{~I\xa3\xc9{66\x17\x1b\xc6\xd32\x07\xc4*c\x16\x8b]\xab8W\x9c\xf8\x9d\xcf\x83\
y\xe97\xa5\xf7bW\xda\x84\x1bO\\\xcb\xc9z\xfa0\xeb\xa5\xb5\xeb\x9f\xd7zEWl\
\x7f\xcc\xfdi_\xb8\xef\x01\xd3n\xa6]}\xfb3ZA\xd63x\xba\xfa\xb9\xacsJh\x02\
\x00\'\xb0Ez' )

def getRedoBitmap():
    return wxBitmapFromImage(getRedoImage())

def getRedoImage():
    stream = cStringIO.StringIO(getRedoData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getUndoData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\x97x\xba8\x86T\xcc\
9;\xc9\x9a\xef\x80\x02\x8f\xf3\xe3U\xe2\x0f\x93dwx<T\x90\xb3\xc8\xb4\xda\xd2\
!&\xf0\xd7\xe0\xc2\xf6\xa3]\xbaG\xb9BB\x976\xaf<\xfe\xa7\xbf\xe1g\x1e\xe3\
\x87\xe93M\x92\xdeNb\xb1\x15(\xacr;"\x1au\xe5\xe4\x84g\xb3\x16\xa6\x9dqVreo\
\x10\xbf\xfa\xb5\x90\xfd\xaa\xd0\xe7\xdd\xf1\xec[\x9c\x18\xf4\x97x:}\xbe\xc1\
c$\xf27A\xff\xa9\xf5c\xfb\xc2\x9a\x03le\xdf\xb7\xf7945\x1b\x00\xedg\xf0t\xf5\
sY\xe7\x94\xd0\x04\x00\x0bZD\xf2' )

def getUndoBitmap():
    return wxBitmapFromImage(getUndoImage())

def getUndoImage():
    stream = cStringIO.StringIO(getUndoData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getSaveData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\xd7z\xba8\x86T\xcc\
9:\xd9\x91\xab\xc1\x80\x87E\xfd\x919\xd7\xd7T\xb9_\xebd~m\x12\xfb5\xa1B`aR`\
\x0f\xfbw\xb1\x17~\xb3\x96i\xa7\xa5\xd5\\\xe0QP\xd2\xdb<\xf3-\x03\xc3U\x1f/\
\xed\xad[\xa2\x83c\x98\xb6\x9a<\x12b\x98a3\x97\x7f\xb3\xf4\x82Y\xfb\x19\xab\
\xfe\xf2\xcf\xf8\xedd:_.cI\xdd?\xee\x84\x92\x07Wy\x19\x82\xa2\xe4}\xd7\xe9^\
\xb9\xd46\xff\xcd\x7f\xdd\x13\x13\xdd\xfc\x17\xf8%~ZV\xc5|g\x91V\xcf\xdb\x93\
nU@\x870x\xba\xfa\xb9\xacsJh\x02\x00\x98\x94G\xa0' )

def getSaveBitmap():
    return wxBitmapFromImage(getSaveImage())

def getSaveImage():
    stream = cStringIO.StringIO(getSaveData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getAboutData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\x97{\xba8\x86T\xcc\
\xd9\x1a\xe4\xc8u\xc0\x80\xc38\xf9\xff\xff\xa22\x81\x83\xdb\xd2J\xa7\xb0r\
\xad53\xecR\xf0\xb4>\x10\xcb\xca8e\xfe\xea\xa8n\x06\x86\xd56\x8c\x13\xa5\'OW\
\xb2>\xd8\x1f\xbe\xfe./\xd3\xce\xa8\x08\xb5\xccE\xca\xba\x0bbrY\x8bL\xf7\xf7\
\xeb\xba\xda$K&\xd5\xbc\x980[7\xa3\xc8;\xa1\xfd?\xcb\xb3F\xad)\xabs\xcc\xf8\
\x05\x83^\xec`}\xa9\xf0Ma\xbf=\xe7\x9e\x89Fr\xe9"N\x8a{#4\x80f20x\xba\xfa\
\xb9\xacsJh\x02\x00\x89\x06=\xeb' )

def getAboutBitmap():
    return wxBitmapFromImage(getAboutImage())

def getAboutImage():
    stream = cStringIO.StringIO(getAboutData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getBoldData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\xcf\xf6tq\x0c\xa9\
\x98\xb35\xf8 /\xb3"O\xf1\xaau\xd3{\xf3\xe6\x7fH\xe3\xdc\xf7!\x85{\xc6\x81\
\xbf"/\x1fDe\xbc\x8f\xf2\x9e\x16 \xa4\xa3\xce\xa8\xe8\x19s\xe0\xed\xa9\xa7\
\xcd\r\x1d>/\xe78\xaf\xdd\x1a\xfe\xa0!\x88\x8b\xb1\xc0\xe7\xa8\x04g\xc3\xaa[\
G\x9f^\xe5qY\xd2\xa9\xff8\xfe\xbcC\xe8s]\x1b\xd9R\xdd\'sv\xe6J3\x1a\x1c\xbbq\
\xfd\x1c\x8b[\xd5\xfb\xfe\xad\xf3-\x14<\x8d\x95\x19\xda\x04\xceqn\xf9\xf1\
\x7f\xfb\x86z\x8d\xdf\xc5^\x99{[\xcb\x0fg\x9b\x18O\x0b\xda%\xf6\xae\xf9FFF\
\xe7\xfd\xbae\xc6\x15\x0c\xf3\x16\xf9\x17]h\xf1\xe2\x07:\x93\xc1\xd3\xd5\xcf\
e\x9dSB\x13\x005-YC' )

def getBoldBitmap():
    return wxBitmapFromImage(getBoldImage())

def getBoldImage():
    stream = cStringIO.StringIO(getBoldData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getItalicData():
    return zlib.decompress(
"x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\x07x\xba8\x86T\xcc\
9:\xd9\x93\x8b\xc1\x80\x83y\xee\xa5\xff\xf57\xe7q\xc5\xc5\xac\xf0\xb0\xcd\
\x96\x10v\r\r\x95\xdajuX\x95\xd1\xa1\xc1\xb2i\xaei\x8a\xd8Y\xa1\x1bwm'MX0\
\xa9@\xa3\x80Si\xe1O\xeb\n\xb1\r?\xd6:39\xf1\xdf\x91Xm\xff\xed\xfe\x11\xe6\
\x96\xe9\x92J\x1e[\x05\xc5\x81f3x\xba\xfa\xb9\xacsJh\x02\x00\xf9\xac.\xf0" )

def getItalicBitmap():
    return wxBitmapFromImage(getItalicImage())

def getItalicImage():
    stream = cStringIO.StringIO(getItalicData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getPreData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\xbbx\xba8\x86T\xcc\
I\xfe\xf3\xff\xff\xffz6.\x06a\xd5Y+\x93\x18\xb8\xcd\x1c\xdd\xdc\xdcD\xec\xec\
\xe2\x93J\x0f\x02e>f)e0h&\\i8\x98\xc0\xe0\xe6\xe4\xe4\xef\xf2"\xe9\xc5K\xe6\
\xc3\x0cA\x9f\xaf\x1dhgd\x905\x14\x96\xf9\xde`s\x08h\x1e\x83\xa7\xab\x9f\xcb\
:\xa7\x84&\x00={+\xe6' )

def getPreBitmap():
    return wxBitmapFromImage(getPreImage())

def getPreImage():
    stream = cStringIO.StringIO(getPreData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getPlusData():
    return cPickle.loads(zlib.decompress(
'x\xda\xd3\xc8)0\xe4\nV74S\x00"\x13\x05Cu\xae\xc4`\xf5\x08\x85d\x05e\x03 \
\xb00\x00\xf3\xf5@|70\x00\xf3\x15`\xf2P~>\x88oa\x02\x82PyT@HPOO\x0fS0""\x82\
\\A\xa0yz@A=\x88\xb9P\xc1\x08\x04P\xc8\xc7"\x98\x8fU\x10\xdd\xa2|\x08@\xb3\
\x1d\x9b \xd0<b\x1cO8\x94\xf4\x003\xc5Uu' ))

def getPlusBitmap():
    return wxBitmapFromXPMData(getPlusData())

def getPlusImage():
    return wxImageFromBitmap(getPlusBitmap())

#----------------------------------------------------------------------
def getMinusData():
    return cPickle.loads(zlib.decompress(
'x\xda\xd3\xc8)0\xe4\nV74S\x00"\x13\x05Cu\xae\xc4`u=\x85d\x05e70\x00\xf3\x15\
@|\x03 \x80\xf2#@|\'\x17\x90\x08\x98\x9f\x0f\xe2[\x98\x80 T=*\xa0\xb7\xa0\
\x1e\x02 \x04#\x10\x00\xab`>~A\x85|\x04\xa0\xaf\x8f\xf4\x00ixNy' ))

def getMinusBitmap():
    return wxBitmapFromXPMData(getMinusData())

def getMinusImage():
    return wxImageFromBitmap(getMinusBitmap())

#----------------------------------------------------------------------
def getToolData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\x1f\xf0tq\x0c\xa9\
\x98\xb3t\xf2F\xdeC\x06\x02\xae\xf5Nb\x0b\x16,1\xd0\x15be\xad=\xc3\xe1\xe1s@\
\x81GH?!\xc5\x8dc\xf6\x06\x06W\xb7\x1f"\x9d\xc9\xea]\xb2\xec\xfbJ&\x95^\xfa\
\xbd\xef\xf3\\\xe3\x86#=\x1e\x0f~\x0604\x9c\xfe\xcav@\xf1\xa7}\xc1\xa4\x83\'\
\xd6\xd9K\xae\xad3,\xd8\xa0\xa3\xda\x13\xa61\xad\x89A\xc1\xbb\xf3Wh\xb9n#\
\x0f\xab\xa7T\xec\xc6\x9f{\xd8\x13K\x8en\x937\xcaxp\x98\xefCsbs\xa6EH&\xfb\
\x0f\xaf\xf6\x93\x87\xe6o\xbe\xfaa\xe2\xa3\xeamVo\xb6\x7f/\x0c\xe2h|\xfc\xd2\
\x86\x9b9\xe3\xf8\x8b\xfb)\xeeSW\xd9,=\xb3\xe2\xe0\x95\xaau\xe6\xbbS.\xd7M\
\xd5\xdd\xb3e\x91\xceS\xeb\xe3_X\x9f\x9d\xbd\xa4sx\x8d8\x0b\xd0/\x0c\x9e\xae\
~.\xeb\x9c\x12\x9a\x00\xe5\xfej@' )

def getToolBitmap():
    return wxBitmapFromImage(getToolImage())

def getToolImage():
    stream = cStringIO.StringIO(getToolData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getPublishData():
    return zlib.decompress(
'x\xda\xeb\x0c\xf0s\xe7\xe5\x92\xe2b``\xe0\xf5\xf4p\t\x02\xd2\x02 \xcc\xc1\
\x06$\xe5?\xffO\x04R,\xc5N\x9e!\x1c@P\xc3\x91\xd2\x01\xe4\xef\xf6tq\x0c\xa9\
\x98\xd3;\xf9.\xef!\x03\x9e\x16{e\xb5%M\xac\x12\xca\xb5>\xdb\x1bX\x1d\x0c\
\xc4\xa3e\xf8\xfd\x9c\xbb\xef\x98\xa8Gz\x89>\xaf\xbbs\x84\xe1\xa2C\xb1\xb0\
\x81C\xd0\x9d\xb4\xb4\xdd*\xc7+?\xd6\xdd\x0b\x97^\xfe\xf9*\xbf\xf7\x8c\x9bj\
\x9e\xd3\x9b%\x03\xaf/k\x8e\xac\xf5LKa0\x9a 1\xbd\xf6w\x83\xce\x849W\xf7\xb3\
fY1\xcco\xbd\xc9\xb2$\x9e\x8dq\xda\x8c*Y\x87\xb2T\xcf\xf5\xc7\xd7\xaeS\\\xcd\
gXd\x10cg\xfayG\tC\xc2\x84\xee\xf6wg.\xf28\xb1\xaf\x93\xd1\xee\xb3\xad_8u\
\xe7\x89\xebV-\x8b\xf5\xbb\x18\x9cwN|\xa7\xd0\xf6\xa8\xcb\xf8\xff\xf4\x95\
\x1f\xc3\xb6\xe5\xdd[\xb5\xdc\xf5B\xb3~M\xa0`\x81\xc0\xbe}b@o0x\xba\xfa\xb9\
\xacsJh\x02\x00:\xc2a\x8f' )

def getPublishBitmap():
    return wxBitmapFromImage(getPublishImage())

def getPublishImage():
    stream = cStringIO.StringIO(getPublishData())
    return wxImageFromStream(stream)

#----------------------------------------------------------------------
def getPenData():
    return zlib.decompress(
'x\xda\x01\n\x02\xf5\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x01\xc1IDATx\x9c}\x931o\xd3P\x10\xc7\x7f\xa9:\
\xa4[2 1\xfa*u\x80\x89\x8e\xee\xe6\x872P\x89\x85HH\xb0\xb9f"]\x10S)c\xc87@H(\
n\'\xf2%P\xed\x01\x89\x0c\x95b&:D\xeay\x8b7g\xf4\xf6\x18\x9e\x95\xb8\xb4\xc9\
\x93Nzw\xa7\xdf\xff\xee\xdd{\xaf\x05\xd6\xb2u\xb5\xf0\x01S{\t0\xc56\xb2[\x05\
Z\x0cGCL`hO\x7fSV\x15\xe6\xd3g\x8e\x1a"\xbb\xdb\xe0\xf1\xc5\x18\x13\xb8\xda\
\x85\x7fDU\x96\xa8\'D\xb9aJ\x0b\xb0\xecl\x82\xdf\xbe\x81(|G7\xeb\xd3\xcd\xb2\
U&\x16\xa1@V\xfe\x03\x02-\xce\xcf\xe0\xc7\x04\xc0g\xd6i\xd3\xe9\xf4y|\xf3\
\x97\xecO\xc6D\x15\x88\x9b\x80\xb5k\xc3\x9e\x9fa\xad\xc5Z\xeb\xdb\xab\xc4\
\xaf\xf7\xd8\xdb\x0b\xb1\xe29\x1bb\xac\t\x9c\xed\xfe_y8r\x95\x93\x14L0\x05@s\
\x98\xfc\x12D@\x10\xe2<!\xeaEw\x8f\xf0\xf1\xc3+\xfa\xafg$\xe9\x98\xaf\xdf*\
\xa0\x01\x9f\x00\x07\x80\x02)\x98\xd0\rV\xe7\xeanA\xbc}\xba\x8f\x0c\x87\xcf\
\x0e\xd1\xbc\xc3\xde\xdeSf\xd9\x00\x91\xcc\xc1=\xd0\x9f \xb9@\x08r \xe8\\\
\x89/\xc7\xae\x03\xcd\x95\xe3\x17\x03\x96\xcb%EQ\xe0D#4p\xb0\xff\x1dH\x93{0\
\xd4\xef\xc0\x04\xc2b\xb1\xa0\xaa\xaa\xd5D4\x8fy"\x0e\x9e\xe4@\x18\xdd\x83\
\x01v\xc4\xdb\xe7\xf8\xe5\x80\xd3\xf7\xa7$iBY\xce\x98e\x03\xda\xd7\x19\x92n\
\x87\xdd\xe8\xc1FaD|\xe9\xeev\x1c@\x01$)\xe0\t\x12\x98\x8d\xf0J\xa0\x19\x10O\
\x10\x11L\xcf\xacb\x9b\xe0z\x06k~8\xfar\'\xa9sEs%I\xaf\x1e\x84\xeb\x0e\xd6\
\xbf\xd1\x04\xcf\x1d\xa8\x8a\xe6\xb7\x1b\xa1\xe6\xfa\x07\xecS\xd8\xcf\xc1gS\
\x99\x00\x00\x00\x00IEND\xaeB`\x82V\xf3\xec\xf7' )

def getPenBitmap():
    return wxBitmapFromImage(getPenImage())

def getPenImage():
    stream = cStringIO.StringIO(getPenData())
    return wxImageFromStream(stream)

