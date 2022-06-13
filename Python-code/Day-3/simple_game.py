print('''

                          .,..
                        .,;;,   .nmMMMMMMMMMMMMMmn,.
                   .   ,MMMMMMMMMMM'd",dMMMMMMMMMMMM"4MMMMMMMMMM"4P4MMMMMMx `
        uMM" x uMP uMMMMMMMM"4MM f,MMMMMMMMMMMMMML`MMMMMMMMMMb h.`MMMMMMMx
       dMP uM uMP uMMMMMMMMMx`4M, dMMMMMMMMMMMMMMP MMMMMMMMMMM,)M MMMMMMMM
      dMP xP uMP ,MMMMMMMMMMPb;"4.`MMPPPPP"MP4MMM dMMMMMMMMMMM dP MMMMMMMM
     dMM xP dMM  MMMMMMC"MMMn;"h.' "Tnmn,.,,nMMM",MMMP""MP"MP xP uMMMMMMM"
    dMM uM dMMP  MMMMMMM;"M,"Mx  ,dc,.  `"""""; -4MmnnxC,uML.= ,dMP"MMMP
   dMM',MP MMM> 4MMMMMMMM;`Mb`"P $$P"   ..     `hc,""???"""". =" .ndP"
  uMMM MM 4MMM  4MMMMMMMMMx`4Mn d$" ,cc$????c,.,$$$$$$$$$$c      --
 ,MMMP,MM MMMM   MMMM"MMM"Tb;"T $$$""" _,c, `$$$$$$$$$$$$$$$====c,
 MMMM dM>,MMMM   MMMM;"M"b,"Tb jP""   c$$$$h ?$$$$$$$$?$P""       ,
;MMMM MM>4MMMM.  4MMMM;"b;"bx.,?F   ,$$$$$$$,`$$$$$$P"zP _,c$$$c   ,
4MMMM MM>4MMMMb  `4MMMMn;"b;T d.   ,$"  `$$$h $$$$$" d$ c$$$$$$$  '
4MMMM MM>4MMMMM   b"4M,"4n."P $L.  d$    $$$F $$$$F $$$ "  `$$$P
dMMMM MMb MMMMML  `b`4Mn`"Mbr<$$$h."P   -??".z$$$$F`$$$     $$P
MMMMM,4MM,"MMMMMb. `?-"4M;"T'<$$$$$hcccccc$$$$$$$$$ ?$$c   -""
MMMMMb MMb MMMMMMMx  '$c ?$$$$$$$$   `?$$$$$$P"  ,c$$$$'
     "MMMMM "MMMM dMMMMMM> ?$c ?$$$$$$$r  :.  """ .  z$$$$$',d
      "MMMMb MMMM MMMMMMMb <$$c ?$$$$$$$. `''''''' ,d$$$$P' <$.
       `MMMMx`MMM MMMMMMM" $$$$h "$$$$$$$c,.  .,,,c$$$$P"   $$h
        `MMMM MM';MMMMMM"  $$$$$$.`?$$$$$$$$$$$$$$$$$$"     <$$.
         4MMP,MM dMMMMM"   $$$$$$$$c,""$$$$$$$$$$$$P"        $$h
         4MM dM",MMMMM"    ??????$$$$$c ""??????""           ?$$.
 4       dMP M",MMMMP  ,;;;;;;;;;;,.""?$$cccccr               $$$
; b.    uMM d uMMMP" ;!!!!!!!!!!!!!!!!;,`"?$$$         $L     ?$$L
'x`4nnmMMP uMMMP"   !!!!!!!!!!!!!!!!!!!!!!;,""        -$$.    `$$$
 "4n,,dM>-dMM"     !!!!!!!!!!!!!!!!!!!!!!!!!!;,        ???     $$$L
   `"`_,pdP"      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!;      $cccc,.  ??$$.
     ""          ;!!!!!'''``'''   ``_,_``""???$$$.
                  dMMMMMMMMMMMMMMMMMx.``!!!!!!!!!!!!  $$$$$$$$$$$$$$$h
  __________________________________________________________________________
Miss Grundy
  __________________________________________________________________________
''')
print("Welcome to Jumanji..!\nSir we need your help to save our Queen named Miss Grundy")
print("Your mission is to find kidnapped queen\n")
choice1 = input('You/\' at crossroad ,where do you want to go? Type"left"or "right.').lower()

if choice1 =="left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. type "wait" to wait for boat or type "swim" to swim across.').lower()
  if choice2 == "wait":
    choice3 = input('You arrive at the island unharmed. There is house with three dorrs red,yellow and black which color do you choose?\n').lower()
    if choice3 == "red":
      print("You selected wrong door, game over..!\n")
    elif choice3 == "yellow":
      print("You found queen..You successfully completed the Mission.\n")
    elif choice3 == "black":
      print("You selected wrong door\n")  
    else:
      print("Please select correct door\n")

  else:
    print("You got attacked by Aligator. Game Over..!\n")

else:
  print("You fell into hole,Game Over..!\n")