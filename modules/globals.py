# -*- coding: utf_8 -*-
from modules.character import CharactersList
from modules.aicontroller import AIController
import direct.directbase.DirectStart
from pandac.PandaModules import CollisionTraverser
from modules.interface import ingameInterface
from modules.sounds import *

base.cTrav = CollisionTraverser()
clist = CharactersList()
intfc = ingameInterface(clist)
aictrl = AIController(clist)
sounds = Sounds()
player = clist.newCharacter('res/actors/gnum',
							{
								'stand': 'res/actors/gnum-stand',
								'walk': 'res/actors/gnum-walk'}
							,
							base.cTrav,
							1, clist, intfc)
player.model.setScale(0.3)

player1 = clist.newCharacter('res/actors/gnum',
							{
								'stand': 'res/actors/gnum-stand',
								'walk': 'res/actors/gnum-walk'}
							,
							base.cTrav,
							1, clist, intfc)
player1.model.setScale(0.3)

player2 = clist.newCharacter('res/actors/gnum',
							{
								'stand': 'res/actors/gnum-stand',
								'walk': 'res/actors/gnum-walk'}
							,
							base.cTrav,
							1, clist, intfc)
player2.model.setScale(0.3)

clist.switchCharacter(2)

taskMgr.add(clist.update,'characters update')
taskMgr.doMethodLater(0.5, aictrl.update, 'AI update')
#taskMgr.doMethodLater(1, clist.randomChangeCurrentCharacterHP,'current character.s HP update')

#sounds.attack1()
