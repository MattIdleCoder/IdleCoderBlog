FasdUAS 1.101.10   ��   ��    k             l      ��  ��   �� 	This AppleScript utility creates a user interface with optional voice directions for any 
	command line-launchable program or script. This demonstration has been written to 
	launch a Python program that uses Unix-type command line flags/switches, but it
	can be adapted to launch any program in the same directory, or any command 
	recognisable by the operating system. It will guide your user through setting 
	the options for your chosen program, options which would normally be set at the 
	command line.
 
	All the lines you need to edit have been marked with '-- XX' for fast GUI development.
 
	Author: matta_idlecoder@protonmail.com 
     � 	 	   	 T h i s   A p p l e S c r i p t   u t i l i t y   c r e a t e s   a   u s e r   i n t e r f a c e   w i t h   o p t i o n a l   v o i c e   d i r e c t i o n s   f o r   a n y   
 	 c o m m a n d   l i n e - l a u n c h a b l e   p r o g r a m   o r   s c r i p t .   T h i s   d e m o n s t r a t i o n   h a s   b e e n   w r i t t e n   t o   
 	 l a u n c h   a   P y t h o n   p r o g r a m   t h a t   u s e s   U n i x - t y p e   c o m m a n d   l i n e   f l a g s / s w i t c h e s ,   b u t   i t 
 	 c a n   b e   a d a p t e d   t o   l a u n c h   a n y   p r o g r a m   i n   t h e   s a m e   d i r e c t o r y ,   o r   a n y   c o m m a n d   
 	 r e c o g n i s a b l e   b y   t h e   o p e r a t i n g   s y s t e m .   I t   w i l l   g u i d e   y o u r   u s e r   t h r o u g h   s e t t i n g   
 	 t h e   o p t i o n s   f o r   y o u r   c h o s e n   p r o g r a m ,   o p t i o n s   w h i c h   w o u l d   n o r m a l l y   b e   s e t   a t   t h e   
 	 c o m m a n d   l i n e . 
   
 	 A l l   t h e   l i n e s   y o u   n e e d   t o   e d i t   h a v e   b e e n   m a r k e d   w i t h   ' - -   X X '   f o r   f a s t   G U I   d e v e l o p m e n t . 
   
 	 A u t h o r :   m a t t a _ i d l e c o d e r @ p r o t o n m a i l . c o m   
   
  
 l     ��������  ��  ��        l     ��������  ��  ��        p         �� �� 0 debuggingit DebuggingIt  �� �� 0 sayingit SayingIt  ������ 0 usercanceled userCanceled��        l     ����  r         m     ��
�� boovfals  o      ���� 0 sayingit SayingIt��  ��        l    ����  r        m    ��
�� boovfals  o      ���� 0 debuggingit DebuggingIt��  ��        l    ����  r       !   m    	��
�� boovfals ! o      ���� 0 usercanceled userCanceled��  ��     " # " l     ��������  ��  ��   #  $ % $ l     ��������  ��  ��   %  & ' & l     �� ( )��   ( C ==============CHOOSE THE COMPILER AND PROGRAM YOU'RE RUNNING:     ) � * * z = = = = = = = = = = = = = C H O O S E   T H E   C O M P I L E R   A N D   P R O G R A M   Y O U ' R E   R U N N I N G :   '  + , + l     �� - .��   - [ U change to your scripting language of choice, or leave blank for a shell script-- XX:    . � / / �   c h a n g e   t o   y o u r   s c r i p t i n g   l a n g u a g e   o f   c h o i c e ,   o r   l e a v e   b l a n k   f o r   a   s h e l l   s c r i p t - -   X X : ,  0 1 0 l    2 3 4 2 r     5 6 5 m     7 7 � 8 8  p y t h o n   6 o      ���� 0 compiler Compiler 3 	  XX    4 � 9 9    X X 1  : ; : l    < = > < r     ? @ ? m     A A � B B  M a r k o v . p y @ o      ���� 0 yourprogname YourProgName = > 8 Change to the filename of your code or script. -- XX       > � C C p   C h a n g e   t o   t h e   f i l e n a m e   o f   y o u r   c o d e   o r   s c r i p t .   - -   X X       ;  D E D l     ��������  ��  ��   E  F G F l   ! H���� H r    ! I J I l    K���� K n     L M L 1    ��
�� 
psxp M l    N���� N b     O P O l    Q���� Q I   �� R S
�� .earsffdralis        afdr R  f     S �� T��
�� 
rtyp T m    ��
�� 
ctxt��  ��  ��   P m     U U � V V  : :��  ��  ��  ��   J o      ���� 0 
homefolder 
homeFolder��  ��   G  W X W l  " ' Y���� Y r   " ' Z [ Z b   " % \ ] \ o   " #���� 0 
homefolder 
homeFolder ] o   # $���� 0 yourprogname YourProgName [ o      ���� *0 yourprognameasposix YourProgNameAsPOSIX��  ��   X  ^ _ ^ l  ( 3 `���� ` r   ( 3 a b a b   ( / c d c b   ( - e f e b   ( + g h g o   ( )���� 0 compiler Compiler h m   ) * i i � j j  " f o   + ,���� *0 yourprognameasposix YourProgNameAsPOSIX d m   - . k k � l l  " b o      ���� "0 commandlinetext CommandLineText��  ��   _  m n m l  4 ; o p q o r   4 ; r s r m   4 7 t t � u u   s o      ���� 0 audiophrase AudioPhrase p    Std string initialisation    q � v v 4   S t d   s t r i n g   i n i t i a l i s a t i o n n  w x w l     ��������  ��  ��   x  y z y l     ��������  ��  ��   z  { | { l     �� } ~��   } F @=============HANDLERS/FUNCTIONS:================================    ~ �   � = = = = = = = = = = = = = H A N D L E R S / F U N C T I O N S : = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = |  � � � l     �� � ���   � j d===== General purpose GUI functions I've written to tailor AppleScript widgets for most situations.     � � � � � = = = = =   G e n e r a l   p u r p o s e   G U I   f u n c t i o n s   I ' v e   w r i t t e n   t o   t a i l o r   A p p l e S c r i p t   w i d g e t s   f o r   m o s t   s i t u a t i o n s .   �  � � � l     �� � ���   � > 8===== PickAFile is the only one that might need changed:    � � � � p = = = = =   P i c k A F i l e   i s   t h e   o n l y   o n e   t h a t   m i g h t   n e e d   c h a n g e d : �  � � � l     ��������  ��  ��   �  � � � i     � � � I      �� ����� $0 interactwithuser InteractWithUser �  � � � o      ���� 0 comment Comment �  ��� � o      ���� 0 choice Choice��  ��   � k      � �  � � � Z     � ����� � o     ���� 0 debuggingit DebuggingIt � I   �� ���
�� .sysodlogaskr        TEXT � b     � � � o    ���� 0 comment Comment � o    ���� 0 choice Choice��  ��  ��   �  ��� � Z    � ����� � o    ���� 0 sayingit SayingIt � I   �� ���
�� .sysottosnull���     TEXT � b     � � � o    ���� 0 comment Comment � o    ���� 0 choice Choice��  ��  ��  ��   �  � � � l     ��������  ��  ��   �  � � � l     �� � ���   � W Q Widget offering mandatory choice between two, 1st is default, no cancel offered:    � � � � �   W i d g e t   o f f e r i n g   m a n d a t o r y   c h o i c e   b e t w e e n   t w o ,   1 s t   i s   d e f a u l t ,   n o   c a n c e l   o f f e r e d : �  � � � i    � � � I      �� ����� 0 pickabutton PickAButton �  � � � o      ���� 0 question Question �  � � � o      ���� 0 firstchoice FirstChoice �  ��� � o      ���� 0 defaultchoice DefaultChoice��  ��   � k     1 � �  � � � r      � � � m      � � � � �  N o n e � o      ���� 0 
answertext 
AnswerText �  � � � Z    � ����� � o    ���� 0 sayingit SayingIt � I   �� ���
�� .sysottosnull���     TEXT � o    	���� 0 question Question��  ��  ��   �  � � � r      � � � I   �� � �
�� .sysodlogaskr        TEXT � o    ���� 0 question Question � �� � �
�� 
btns � J     � �  � � � o    ���� 0 firstchoice FirstChoice �  ��� � o    ���� 0 defaultchoice DefaultChoice��   � �� ���
�� 
dflt � m    ���� ��   � o      ���� 0 dialoganswer DialogAnswer �  � � � r   ! & � � � n   ! $ � � � 1   " $��
�� 
bhit � o   ! "���� 0 dialoganswer DialogAnswer � o      ���� 0 
answertext 
AnswerText �  � � � I   ' .�� ����� $0 interactwithuser InteractWithUser �  � � � m   ( ) � � � � �   �  ��� � o   ) *���� 0 
answertext 
AnswerText��  ��   �  �� � L   / 1 � � o   / 0�~�~ 0 
answertext 
AnswerText�   �  � � � l     �}�|�{�}  �|  �{   �  � � � l     �z�y�x�z  �y  �x   �  � � � i    � � � I      �w ��v�w 0 pickfromlist PickFromList �  � � � o      �u�u "0 listinstruction ListInstruction �  � � � o      �t�t 0 listofitems ListOfItems �  ��s � o      �r�r 0 defaultitem DefaultItem�s  �v   � l    = � � � � k     = � �  � � � r      � � � m      � � � � �  N o n e � o      �q�q 0 listpick ListPick �  � � � Z    � ��p�o � o    �n�n 0 sayingit SayingIt � I   �m ��l
�m .sysottosnull���     TEXT � o    	�k�k "0 listinstruction ListInstruction�l  �p  �o   �  � � � r     � � � I   �j � �
�j .gtqpchltns    @   @ ns   � o    �i�i 0 listofitems ListOfItems � �h � 
�h 
okbt � m     �  C h o o s e  �g
�g 
prmp o    �f�f "0 listinstruction ListInstruction �e�d
�e 
inSL o    �c�c 0 defaultitem DefaultItem�d   � o      �b�b 0 
listresult 
ListResult �  Z     2	�a
 =    # o     !�`�` 0 
listresult 
ListResult m   ! "�_
�_ boovfals	 l  & ) r   & ) m   & '�^
�^ boovtrue o      �]�] 0 usercanceled userCanceled g a user hit cancel. Historical quirk of 'choose from list'. See AppleScript LanguageGuide 2013 p148    � �   u s e r   h i t   c a n c e l .   H i s t o r i c a l   q u i r k   o f   ' c h o o s e   f r o m   l i s t ' .   S e e   A p p l e S c r i p t   L a n g u a g e G u i d e   2 0 1 3   p 1 4 8�a  
 l  , 2 l  , 2 r   , 2 n   , 0 4   - 0�\
�\ 
cobj m   . /�[�[  o   , -�Z�Z 0 
listresult 
ListResult o      �Y�Y 0 listpick ListPick X R 'choose from list' always returns a list, even of one item, if Cancel is not hit.    � �   ' c h o o s e   f r o m   l i s t '   a l w a y s   r e t u r n s   a   l i s t ,   e v e n   o f   o n e   i t e m ,   i f   C a n c e l   i s   n o t   h i t . g a ListResult is not false. Note that there's a result, not that it's true. See LanguageGuide p148     � �   L i s t R e s u l t   i s   n o t   f a l s e .   N o t e   t h a t   t h e r e ' s   a   r e s u l t ,   n o t   t h a t   i t ' s   t r u e .   S e e   L a n g u a g e G u i d e   p 1 4 8    !  I   3 :�X"�W�X $0 interactwithuser InteractWithUser" #$# m   4 5%% �&&  $ '�V' o   5 6�U�U 0 listpick ListPick�V  �W  ! (�T( L   ; =)) o   ; <�S�S 0 listpick ListPick�T   � ; 5 Widget offering list of choices, with cancel offered    � �** j   W i d g e t   o f f e r i n g   l i s t   o f   c h o i c e s ,   w i t h   c a n c e l   o f f e r e d � +,+ l     �R�Q�P�R  �Q  �P  , -.- l     �O�N�M�O  �N  �M  . /0/ i   121 I      �L3�K�L 0 getusertext GetUserText3 454 o      �J�J 0 userquestion UserQuestion5 6�I6 o      �H�H 0 defaulttext defaultText�I  �K  2 l    M7897 k     M:: ;<; r     =>= m     ?? �@@  > o      �G�G 0 
useranswer 
UserAnswer< ABA W    JCDC Q    EEFGE k    :HH IJI Z   "KL�F�EK o    �D�D 0 sayingit SayingItL I   �CM�B
�C .sysottosnull���     TEXTM o    �A�A 0 userquestion UserQuestion�B  �F  �E  J NON r   # ,PQP I  # *�@RS
�@ .sysodlogaskr        TEXTR o   # $�?�? 0 userquestion UserQuestionS �>T�=
�> 
dtxtT o   % &�<�< 0 defaulttext defaultText�=  Q o      �;�; 0 	boxanswer 	BoxAnswerO UVU r   - 2WXW l  - 0Y�:�9Y n   - 0Z[Z 1   . 0�8
�8 
ttxt[ o   - .�7�7 0 	boxanswer 	BoxAnswer�:  �9  X o      �6�6 0 
useranswer 
UserAnswerV \�5\ I   3 :�4]�3�4 $0 interactwithuser InteractWithUser] ^_^ m   4 5`` �aa  _ b�2b o   5 6�1�1 0 
useranswer 
UserAnswer�2  �3  �5  F R      �0�/c
�0 .ascrerr ****      � ****�/  c �.d�-
�. 
errnd d      ee m      �,�, ��-  G l  B Efghf r   B Eiji m   B C�+
�+ boovtruej o      �*�* 0 usercanceled userCanceledg   user hit cancel   h �kk     u s e r   h i t   c a n c e lD G    lml o    	�)�) 0 usercanceled userCanceledm l   n�(�'n >   opo o    �&�& 0 
useranswer 
UserAnswerp m    qq �rr  �(  �'  B s�%s L   K Mtt o   K L�$�$ 0 
useranswer 
UserAnswer�%  8 * $ Widget that asks the user for input   9 �uu H   W i d g e t   t h a t   a s k s   t h e   u s e r   f o r   i n p u t0 vwv l     �#�"�!�#  �"  �!  w xyx l     � ���   �  �  y z{z i   |}| I      �~�� 0 pickafolder PickAFolder~ � o      �� 0 instruction Instruction� ��� o      �� 0 defaultpath DefaultPath�  �  } l    g���� k     g�� ��� r     ��� m     �� ���  � o      �� $0 folderpathstring FolderPathString� ��� Q    +���� k     �� ��� Z   ����� o    �� 0 sayingit SayingIt� I   ���
� .sysottosnull���     TEXT� o    �� 0 instruction Instruction�  �  �  � ��� r     ��� I   ���
� .sysostflalis    ��� null�  � ���
� 
prmp� o    �� 0 instruction Instruction� ���
� 
dflc� o    �
�
 0 defaultpath DefaultPath�  � o      �	�	 0 chosenfolder ChosenFolder�  � R      ���
� .ascrerr ****      � ****�  � ���
� 
errn� d      �� m      �� ��  � l  ( +���� r   ( +��� m   ( )�
� boovtrue� o      �� 0 usercanceled userCanceled�   user hit cancel   � ���     u s e r   h i t   c a n c e l� ��� Z   , d���� � H   , .�� o   , -���� 0 usercanceled userCanceled� k   1 `�� ��� Z  1 @������� o   1 2���� 0 debuggingit DebuggingIt� I  5 <�����
�� .sysodlogaskr        TEXT� b   5 8��� m   5 6�� ��� L T h e   H F S   p a t h   o f   t h e   c h o s e n   f o l d e r   i s :  � o   6 7���� 0 chosenfolder ChosenFolder��  ��  ��  � ��� r   A F��� n   A D��� 1   B D��
�� 
psxp� o   A B���� 0 chosenfolder ChosenFolder� o      ���� 0 posixfolder PosixFolder� ��� r   G N��� b   G L��� b   G J��� m   G H�� ���  "� o   H I���� 0 posixfolder PosixFolder� m   J K�� ���  "� o      ���� $0 folderpathstring FolderPathString� ���� Z  O `������� o   O P���� 0 debuggingit DebuggingIt� I  S \�����
�� .sysodlogaskr        TEXT� b   S X��� m   S V�� ��� P T h e   P O S I X   p a t h   o f   t h e   c h o s e n   f o l d e r   i s :  � o   V W���� $0 folderpathstring FolderPathString��  ��  ��  ��  �  �   � ���� L   e g�� o   e f���� $0 folderpathstring FolderPathString��  � R L Widget that asks the user to choose a folder, offering a default and Cancel   � ��� �   W i d g e t   t h a t   a s k s   t h e   u s e r   t o   c h o o s e   a   f o l d e r ,   o f f e r i n g   a   d e f a u l t   a n d   C a n c e l{ ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� i   ��� I      ������� 0 	pickafile 	PickAFile� ��� o      ���� 0 instruction Instruction� ���� o      ���� 00 defaultfolderpathalias DefaultFolderPathAlias��  ��  � l    o���� k     o�� ��� r     ��� m     �� ���  � o      ����  0 filepathstring FilePathString� ��� Q    /���� k    $�� ��� Z   ������� o    ���� 0 sayingit SayingIt� I   �����
�� .sysottosnull���     TEXT� o    ���� 0 instruction Instruction��  ��  ��  � ��� l   ������  � � } In the next line, you need to insert the correct UTI type for the files you want to open. This can be a list of file types.    � ��� �   I n   t h e   n e x t   l i n e ,   y o u   n e e d   t o   i n s e r t   t h e   c o r r e c t   U T I   t y p e   f o r   t h e   f i l e s   y o u   w a n t   t o   o p e n .   T h i s   c a n   b e   a   l i s t   o f   f i l e   t y p e s .  � ��� l   ������  � P J To open everything in the chosen folder, omit the <of type {""}> command:   � ��� �   T o   o p e n   e v e r y t h i n g   i n   t h e   c h o s e n   f o l d e r ,   o m i t   t h e   < o f   t y p e   { " " } >   c o m m a n d :� ���� l   $� � r    $ I   "����
�� .sysostdfalis    ��� null��   ��
�� 
prmp o    ���� 0 instruction Instruction ��
�� 
ftyp J    		 
��
 m     � " p u b l i c . p l a i n - t e x t��   ����
�� 
dflc o    ���� 00 defaultfolderpathalias DefaultFolderPathAlias��   o      ���� 0 
chosenfile 
ChosenFile   XX    �  X X��  � R      ����
�� .ascrerr ****      � ****��   ����
�� 
errn d       m      ���� ���  � l  , / r   , / m   , -��
�� boovtrue o      ���� 0 usercanceled userCanceled   user hit cancel    �     u s e r   h i t   c a n c e l�  Z   0 l���� H   0 2 o   0 1���� 0 usercanceled userCanceled k   5 h  Z  5 D !����  o   5 6���� 0 debuggingit DebuggingIt! I  9 @��"��
�� .sysodlogaskr        TEXT" b   9 <#$# m   9 :%% �&& H T h e   H F S   p a t h   o f   t h e   c h o s e n   f i l e   i s :  $ o   : ;���� 0 
chosenfile 
ChosenFile��  ��  ��   '(' r   E J)*) n   E H+,+ 1   F H��
�� 
psxp, o   E F���� 0 
chosenfile 
ChosenFile* o      ���� 0 	posixfile 	PosixFile( -.- r   K V/0/ b   K T121 b   K P343 m   K N55 �66  "4 o   N O���� 0 	posixfile 	PosixFile2 m   P S77 �88  "0 o      ����  0 filepathstring FilePathString. 9��9 Z  W h:;����: o   W X���� 0 debuggingit DebuggingIt; I  [ d��<��
�� .sysodlogaskr        TEXT< b   [ `=>= m   [ ^?? �@@ L T h e   P O S I X   p a t h   o f   t h e   c h o s e n   f i l e   i s :  > o   ^ _����  0 filepathstring FilePathString��  ��  ��  ��  ��  ��   A��A L   m oBB o   m n����  0 filepathstring FilePathString��  � D > Widget that asks the user to choose a file, offering a Cancel   � �CC |   W i d g e t   t h a t   a s k s   t h e   u s e r   t o   c h o o s e   a   f i l e ,   o f f e r i n g   a   C a n c e l� DED l     ��������  ��  ��  E FGF l     ��������  ��  ��  G HIH i   JKJ I      ��L���� 0 	pickfiles 	PickFilesL MNM o      ���� 0 instruction InstructionN O��O o      ���� 00 defaultfolderpathalias DefaultFolderPathAlias��  ��  K l    �PQRP k     �SS TUT r     VWV m     XX �YY  W o      ����  0 filepathstring FilePathStringU Z[Z Q    1\]^\ k    &__ `a` Z   bc����b o    ���� 0 sayingit SayingItc I   ��d��
�� .sysottosnull���     TEXTd o    ���� 0 instruction Instruction��  ��  ��  a efe l   ��gh��  g �  In the next line, you need to insert the correct UTI type for the files you want to open. This should be a list of file types,   h �ii �   I n   t h e   n e x t   l i n e ,   y o u   n e e d   t o   i n s e r t   t h e   c o r r e c t   U T I   t y p e   f o r   t h e   f i l e s   y o u   w a n t   t o   o p e n .   T h i s   s h o u l d   b e   a   l i s t   o f   f i l e   t y p e s ,f jkj l   ��lm��  l t n using the Apple definition of UTIs. To open everything in the chosen folder, omit the <of type {""}> command:   m �nn �   u s i n g   t h e   A p p l e   d e f i n i t i o n   o f   U T I s .   T o   o p e n   e v e r y t h i n g   i n   t h e   c h o s e n   f o l d e r ,   o m i t   t h e   < o f   t y p e   { " " } >   c o m m a n d :k o��o r    &pqp I   $����r
�� .sysostdfalis    ��� null��  r ��st
�� 
prmps o    ���� 0 instruction Instructiont ��uv
�� 
ftypu J    ww x��x m    yy �zz " p u b l i c . p l a i n - t e x t��  v ��{|
�� 
dflc{ o    ���� 00 defaultfolderpathalias DefaultFolderPathAlias| ��}��
�� 
mlsl} m     ��
�� boovtrue��  q o      ���� 0 chosenfiles ChosenFiles��  ] R      ����~
�� .ascrerr ****      � ****��  ~ ����
�� 
errn d      �� m      ���� ���  ^ l  . 1���� r   . 1��� m   . /��
�� boovtrue� o      ���� 0 usercanceled userCanceled�   user hit cancel   � ���     u s e r   h i t   c a n c e l[ ��� Z   2 �������� H   2 4�� o   2 3���� 0 usercanceled userCanceled� k   7 ��� ��� X   7 u����� l  G p���� k   G p�� ��� Z  G Z������� o   G J�� 0 debuggingit DebuggingIt� I  M V�~��}
�~ .sysodlogaskr        TEXT� b   M R��� m   M P�� ��� L T h e   H F S   p a t h   o f   t h e   c h o s e n   f i l e s   a r e :  � o   P Q�|�| 0 	filealias 	FileAlias�}  ��  ��  � ��� r   [ b��� n   [ `��� 1   \ `�{
�{ 
psxp� o   [ \�z�z 0 	filealias 	FileAlias� o      �y�y 0 	posixfile 	PosixFile� ��x� l  c p���� r   c p��� b   c n��� b   c j��� b   c h��� o   c d�w�w  0 filepathstring FilePathString� m   d g�� ���  "� o   h i�v�v 0 	posixfile 	PosixFile� m   j m�� ���  "  � o      �u�u  0 filepathstring FilePathString� 1 +<==== note the space after the second quote   � ��� V < = = = =   n o t e   t h e   s p a c e   a f t e r   t h e   s e c o n d   q u o t e�x  � = 7<====== how you iteratate through a list in AppleScript   � ��� n < = = = = = =   h o w   y o u   i t e r a t a t e   t h r o u g h   a   l i s t   i n   A p p l e S c r i p t�� 0 	filealias 	FileAlias� o   : ;�t�t 0 chosenfiles ChosenFiles� ��s� Z  v ����r�q� o   v y�p�p 0 debuggingit DebuggingIt� I  | ��o��n
�o .sysodlogaskr        TEXT� b   | ���� m   | �� ��� ` T h e   l i s t   o f   P O S I X   p a t h s   o f   t h e   c h o s e n   f i l e s   i s :  � o    ��m�m  0 filepathstring FilePathString�n  �r  �q  �s  ��  ��  � ��l� L   � ��� o   � ��k�k  0 filepathstring FilePathString�l  Q L F Widget that asks the user to choose multiple files, offering a Cancel   R ��� �   W i d g e t   t h a t   a s k s   t h e   u s e r   t o   c h o o s e   m u l t i p l e   f i l e s ,   o f f e r i n g   a   C a n c e lI ��� l     �j�i�h�j  �i  �h  � ��� l     �g�f�e�g  �f  �e  � ��� i   ��� I      �d��c�d 0 sendoutputto SendOutputTo� ��� o      �b�b 0 	chosenapp 	ChosenApp� ��� o      �a�a 0 docbody DocBody� ��`� o      �_�_ 0 docname DocName�`  �c  � l    ����� k     ��� ��� I    �^��]
�^ .JonspClpnull���     ****� l    ��\�[� o     �Z�Z 0 docbody DocBody�\  �[  �]  � ��Y� O    ���� k    ��� ��� Z    '���X�W� F    ��� o    �V�V 0 sayingit SayingIt� H    �� o    �U�U 0 debuggingit DebuggingIt� l   #���� k    #�� ��� I   �T��S
�T .sysodelanull��� ��� nmbr� m    �� ?�      �S  � ��R� I   #�Q��P
�Q .sysottosnull���     TEXT� m    �� ��� L H e r e   a r e   t h e   r e s u l t s   o f   y o u r   a n a l y s i s .�P  �R  �   for a faster debug   � ��� &   f o r   a   f a s t e r   d e b u g�X  �W  � ��� I  ( -�O�N�M
�O .aevtoappnull  �   � ****�N  �M  � ��� I  . 3�L�K�J
�L .miscactvnull��� ��� null�K  �J  � ��� I  4 9�I��H
�I .sysodelanull��� ��� nmbr� m   4 5�G�G �H  � ��� Z  : I���F�E� l  : =��D�C� =  : =��� o   : ;�B�B 0 	chosenapp 	ChosenApp� m   ; <�� ���  M i c r o s o f t   W o r d�D  �C  � I  @ E�A��@
�A .sysodelanull��� ��� nmbr� m   @ A�?�? �@  �F  �E  �    Z   J ��> =  J M o   J K�=�= 0 	chosenapp 	ChosenApp m   K L �  M a i l O   P �	
	 k   T �  r   T r I  T p�<�;
�< .corecrel****      � null�;   �:
�: 
kocl m   V W�9
�9 
bcke �8�7
�8 
prdt K   Z j �6
�6 
pvis m   ] ^�5
�5 boovtrue �4
�4 
subj o   a b�3�3 0 docname DocName �2�1
�2 
ctnt o   e f�0�0 0 docbody DocBody�1  �7   o      �/�/ 0 
themessage 
theMessage �. O   s � k   w �  I  w ��-�, 
�- .corecrel****      � null�,    �+!"
�+ 
kocl! m   y |�*
�* 
trcp" �)#�(
�) 
prdt# K    �$$ �'%&
�' 
pnam% m   � �'' �((  M a t t& �&)�%
�& 
radd) m   � �** �++ ( a i n s y @ p r o t o n m a i l . c o m�%  �(   ,�$, l  � ��#-.�#  - A ;send  --<===== this line will send the email automatically.   . �// v s e n d     - - < = = = = =   t h i s   l i n e   w i l l   s e n d   t h e   e m a i l   a u t o m a t i c a l l y .�$   o   s t�"�" 0 
themessage 
theMessage�.  
 m   P Q00x                                                                                  emal  alis      Macintosh HD                   BD ����Mail.app                                                       ����            ����  
 cu             Applications  /:Applications:Mail.app/    M a i l . a p p    M a c i n t o s h   H D  Applications/Mail.app   / ��  �>   k   � �11 232 l  � �4564 O  � �787 I  � ��!9:
�! .prcskprsnull���     ctxt9 m   � �;; �<<  n: � =�
�  
faal= m   � ��
� eMdsKcmd�  8 m   � �>>�                                                                                  sevs  alis    \  Macintosh HD                   BD ����System Events.app                                              ����            ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��  5    cmd-n = open new document   6 �?? 4   c m d - n   =   o p e n   n e w   d o c u m e n t3 @�@ l  � �ABCA O  � �DED I  � ��FG
� .prcskprsnull���     ctxtF m   � �HH �II  vG �J�
� 
faalJ m   � ��
� eMdsKcmd�  E m   � �KK�                                                                                  sevs  alis    \  Macintosh HD                   BD ����System Events.app                                              ����            ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��  B + % cmd-v = paste the clipboard contents   C �LL J   c m d - v   =   p a s t e   t h e   c l i p b o a r d   c o n t e n t s�   M�M l  � �����  �  �  �  � 4    
�N
� 
cappN o    	�� 0 	chosenapp 	ChosenApp�Y  � 1 + Sends the results to the user's chosen app   � �OO V   S e n d s   t h e   r e s u l t s   t o   t h e   u s e r ' s   c h o s e n   a p p� PQP l     ����  �  �  Q RSR l     ����  �  �  S TUT i    #VWV I      �X�� (0 chooseoutputappfor ChooseOutputAppForX YZY o      �
�
 0 results ResultsZ [�	[ o      �� 0 title Title�	  �  W l    d\]^\ k     d__ `a` r     bcb m     dd �ee  c o      �� 0 	outputapp 	OutputAppa f�f Q    dghig k    Wjj klk r    
mnm m    oo �pp j W h i c h   a p p l i c a t i o n   d o   y o u   w a n t   t o   s e n d   t h e   r e s u l t s   t o ?n o      ��  0 outputquestion OutputQuestionl qrq Z   st��s o    �� 0 sayingit SayingItt I   �u� 
� .sysottosnull���     TEXTu o    ����  0 outputquestion OutputQuestion�   �  �  r vwv r    1xyx I   /��z{
�� .gtqpchltns    @   @ ns  z J    || }~} m     ���  T e x t E d i t~ ��� m    �� ���  M i c r o s o f t   W o r d� ��� m    �� ��� 
 N o t e s� ���� m    �� ���  M a i l��  { ����
�� 
okbt� l 	   !������ m     !�� ���  S e l e c t��  ��  � ����
�� 
appr� m   " #�� ���   O u t p u t   f i l e   t y p e� ����
�� 
inSL� J   $ '�� ���� m   $ %�� ���  T e x t E d i t��  � �����
�� 
prmp� o   ( )����  0 outputquestion OutputQuestion��  y o      ���� "0 outputappanswer OutputAppAnswerw ���� Z   2 W������� >  2 5��� o   2 3���� "0 outputappanswer OutputAppAnswer� m   3 4��
�� boovfals� l  8 S���� k   8 S�� ��� l  8 8������  � Z T  Note that this means there's a result, not that it's true. See LanguageGuide p148    � ��� �     N o t e   t h a t   t h i s   m e a n s   t h e r e ' s   a   r e s u l t ,   n o t   t h a t   i t ' s   t r u e .   S e e   L a n g u a g e G u i d e   p 1 4 8  � ��� r   8 @��� n   8 >��� 4   9 >���
�� 
cobj� m   < =���� � o   8 9���� "0 outputappanswer OutputAppAnswer� o      ���� 0 	outputapp 	OutputApp� ��� I   A J������� $0 interactwithuser InteractWithUser� ��� m   B E�� ��� R O K .   I ' m   n o w   s a v i n g   t o   a   n e w   f i l e   o f   t y p e  � ���� o   E F���� 0 	outputapp 	OutputApp��  ��  � ���� I   K S������� 0 sendoutputto SendOutputTo� ��� o   L M���� 0 	outputapp 	OutputApp� ��� o   M N���� 0 results Results� ���� o   N O���� 0 title Title��  ��  ��  � ? 9 user didn't hit cancel, so extensionResult is not false.   � ��� r   u s e r   d i d n ' t   h i t   c a n c e l ,   s o   e x t e n s i o n R e s u l t   i s   n o t   f a l s e .��  ��  ��  h R      �����
�� .ascrerr ****      � ****��  � �����
�� 
errn� d      �� m      ���� ���  i l  _ d���� r   _ d��� m   _ `��
�� boovtrue� o      ���� 0 usercanceled userCanceled�   user hit cancel   � ���     u s e r   h i t   c a n c e l�  ] 8 2 Widget that asks the user to choose an output app   ^ ��� d   W i d g e t   t h a t   a s k s   t h e   u s e r   t o   c h o o s e   a n   o u t p u t   a p pU ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ������  � [ U==================================MAIN=========================================  --XX   � ��� � = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = M A I N = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =     - - X X� ��� l     ��������  ��  ��  � ��� l      ������  ��� 
NOTE 1: The code blocks below are used to create sequential, simple GUI input boxes to set most command line variables 
your program might need. For each block you decide to use, you only need to modify the lines marked '-- XX'.

NOTE 2: The user interface that you write here for your program needs to take into account all the mandatory command line 
flags/switches your program has, plus any optional flags/switches you want to set.  

NOTE 3. As the user answers the questions, a valid command line for your program is assembled. 

NOTE 4. Finally, before your program is run, the user is asked which application they want to send the output of your program to.
   � ���8   
 N O T E   1 :   T h e   c o d e   b l o c k s   b e l o w   a r e   u s e d   t o   c r e a t e   s e q u e n t i a l ,   s i m p l e   G U I   i n p u t   b o x e s   t o   s e t   m o s t   c o m m a n d   l i n e   v a r i a b l e s   
 y o u r   p r o g r a m   m i g h t   n e e d .   F o r   e a c h   b l o c k   y o u   d e c i d e   t o   u s e ,   y o u   o n l y   n e e d   t o   m o d i f y   t h e   l i n e s   m a r k e d   ' - -   X X ' . 
 
 N O T E   2 :   T h e   u s e r   i n t e r f a c e   t h a t   y o u   w r i t e   h e r e   f o r   y o u r   p r o g r a m   n e e d s   t o   t a k e   i n t o   a c c o u n t   a l l   t h e   m a n d a t o r y   c o m m a n d   l i n e   
 f l a g s / s w i t c h e s   y o u r   p r o g r a m   h a s ,   p l u s   a n y   o p t i o n a l   f l a g s / s w i t c h e s   y o u   w a n t   t o   s e t .     
 
 N O T E   3 .   A s   t h e   u s e r   a n s w e r s   t h e   q u e s t i o n s ,   a   v a l i d   c o m m a n d   l i n e   f o r   y o u r   p r o g r a m   i s   a s s e m b l e d .   
 
 N O T E   4 .   F i n a l l y ,   b e f o r e   y o u r   p r o g r a m   i s   r u n ,   t h e   u s e r   i s   a s k e d   w h i c h   a p p l i c a t i o n   t h e y   w a n t   t o   s e n d   t h e   o u t p u t   o f   y o u r   p r o g r a m   t o . 
� ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ������  � _ Y=========PICK AND MODIFY THE QUESTIONS BELOW TO CREATE THE COMMAND LINE FOR YOUR PROGRAM:   � ��� � = = = = = = = = = P I C K   A N D   M O D I F Y   T H E   Q U E S T I O N S   B E L O W   T O   C R E A T E   T H E   C O M M A N D   L I N E   F O R   Y O U R   P R O G R A M :� ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ������  � n h Ask if the user wants audio instructions for your program and, if so, play an audio intro for the user:   � ��� �   A s k   i f   t h e   u s e r   w a n t s   a u d i o   i n s t r u c t i o n s   f o r   y o u r   p r o g r a m   a n d ,   i f   s o ,   p l a y   a n   a u d i o   i n t r o   f o r   t h e   u s e r :� ��� l  < N������ r   < N��� I   < J������� 0 pickabutton PickAButton� ��� m   = @�� ��� R D o   y o u   w a n t   F i o n a   t o   t a l k   y o u   t h r o u g h   i t ?� ��� m   @ C�� �    N o ,   t h a n k s .� �� m   C F �  Y e s ,   p l e a s e .��  ��  � o      ���� 0 fionaanswer FionaAnswer��  ��  �  l  O p���� Z   O p���� =  O V	
	 o   O R���� 0 fionaanswer FionaAnswer
 m   R U �  Y e s ,   p l e a s e . k   Y l  r   Y \ m   Y Z��
�� boovtrue o      ���� 0 sayingit SayingIt  I  ] d����
�� .sysottosnull���     TEXT m   ] ` �� H i ,   I ' m   F i o n a .   I ' m   g o i n g   t o   w a l k   y o u   t h r o u g h   a   M a r k o v i a n   r a n d o m   t e x t   g e n e r a t i o n   e x e r c i s e ,   u s i n g   t h e   w o r d   c h a i n s   f r o m   m u l t i p l e   i n p u t   t e x t   f i l e s   t o   c r e a t e   r a n d o m ,   g r a m m a t i c a l l y   c o r r e c t   b u t   m e a n i n g l e s s   E n g l i s h .��   �� r   e l m   e h � $ I ' m   n o w   r u n n i n g   a   o      ���� 0 audiophrase AudioPhrase��  ��  ��  ��  ��    l     ��������  ��  ��    l     ��������  ��  ��    !  l     ��������  ��  ��  ! "#" l     ��$%��  $ L F== Ask the user to pick a text option from a list, offering a default:   % �&& � = =   A s k   t h e   u s e r   t o   p i c k   a   t e x t   o p t i o n   f r o m   a   l i s t ,   o f f e r i n g   a   d e f a u l t :# '(' l  q)����) Z   q*+����* =  q t,-, o   q r���� 0 usercanceled userCanceled- m   r s��
�� boovfals+ k   w.. /0/ l  w �1231 r   w �454 I   w ���6���� 0 pickfromlist PickFromList6 787 m   x {99 �:: P W h a t   O r d e r   o f   M a r k o v   d o   y o u   w a n t   t o   r u n ?8 ;<; J   { �== >?> m   { ~@@ �AA 
 F i r s t? BCB m   ~ �DD �EE  S e c o n dC FGF m   � �HH �II 
 T h i r dG J��J m   � �KK �LL  F o u r t h��  < M��M m   � �NN �OO  S e c o n d��  ��  5 o      ���� 0 	userstext 	UsersText2 	  XX   3 �PP    X X0 QRQ Z   � �STU��S l  � �V����V =  � �WXW o   � ����� 0 	userstext 	UsersTextX m   � �YY �ZZ 
 F i r s t��  ��  T l  � �[\][ r   � �^_^ m   � ����� _ o      ���� 0 order Order\ 	  XX   ] �``    X XU aba l  � �c����c =  � �ded o   � ����� 0 	userstext 	UsersTexte m   � �ff �gg  S e c o n d��  ��  b hih r   � �jkj m   � ����� k o      ���� 0 order Orderi lml l  � �n����n =  � �opo o   � ����� 0 	userstext 	UsersTextp m   � �qq �rr 
 T h i r d��  ��  m sts r   � �uvu m   � ����� v o      �� 0 order Ordert wxw l  � �y�~�}y =  � �z{z o   � ��|�| 0 	userstext 	UsersText{ m   � �|| �}}  F o u r t h�~  �}  x ~�{~ r   � �� m   � ��z�z � o      �y�y 0 order Order�{  ��  R ��� l  � ����� r   � ���� b   � ���� b   � ���� o   � ��x�x 0 audiophrase AudioPhrase� o   � ��w�w 0 	userstext 	UsersText� m   � ��� ���    o r d e r   M a r k o v ,  � o      �v�v 0 audiophrase AudioPhrase� 	  XX   � ���    X X� ��u� l  ����� r   ���� b   � ���� b   � ���� o   � ��t�t "0 commandlinetext CommandLineText� m   � ��� ���    - o  � o   � ��s�s 0 order Order� o      �r�r "0 commandlinetext CommandLineText� 	  XX   � ���    X X�u  ��  ��  ��  ��  ( ��� l     �q�p�o�q  �p  �o  � ��� l     �n�m�l�n  �m  �l  � ��� l     �k�j�i�k  �j  �i  � ��� l ���h�g� Z  ����f�e� l 
��d�c� = 
��� o  �b�b 0 usercanceled userCanceled� m  	�a
�a boovfals�d  �c  � k  ��� ��� l ���� r  ��� I  �`��_�` 0 pickabutton PickAButton� ��� m  �� ��� � W h a t   a b o u t   a   s t a r t i n g   p h r a s e ?   D o   y o u   w a n t   t o   p i c k   o n e   f r o m   o n e   o f   t h e   i n p u t   f i l e s   y o u   p l a n   t o   u s e ?� ��� m  �� ���  N o� ��^� m  �� ���  Y e s�^  �_  � o      �]�] 0 usestartseq UseStartSeq� 	  XX   � ���    X X� ��� l   �\�[�Z�\  �[  �Z  � ��Y� Z   ����X�W� =  '��� o   #�V�V 0 usestartseq UseStartSeq� m  #&�� ���  Y e s� k  *��� ��� l *A���� r  *A��� I  *=�U��T�U 0 getusertext GetUserText� ��� b  +6��� b  +2��� m  +.�� ��� > O K ,   n o w   p l e a s e   c u t   a n d   p a s t e   a  � o  .1�S�S 0 order Order� m  25�� ��� �   w o r d   p h r a s e   f r o m   o n e   o f   y o u r   i n p u t   f i l e s .   T h i s   w i l l   b e   t h e   s t a r t   o f   t h e   M a r k o v i a n   p a r a g r a p h .� ��R� m  69�� ��� . C h o o s e   a   r a n d o m   p h r a s e .�R  �T  � o      �Q�Q 0 
start_text  � 	  XX   � ���    X X� ��� r  BQ��� I BM�P��O
�P .corecnte****       ****� n  BI��� 2 EI�N
�N 
cwor� o  BE�M�M 0 
start_text  �O  � o      �L�L "0 numwordsentered NumWordsEntered� ��� l RR�K���K  � � display dialog "The starting phrase you have entered is " & "'" & start_text & "'" & " of length " & NumWordsEntered & " words"   � ��� � d i s p l a y   d i a l o g   " T h e   s t a r t i n g   p h r a s e   y o u   h a v e   e n t e r e d   i s   "   &   " ' "   &   s t a r t _ t e x t   &   " ' "   &   "   o f   l e n g t h   "   &   N u m W o r d s E n t e r e d   &   "   w o r d s "� ��� I RW�J��I
�J .sysodelanull��� ��� nmbr� m  RS�H�H �I  � ��� l XX�G�F�E�G  �F  �E  � ��D� Z  X����C�� > X_��� o  X[�B�B 0 
start_text  � m  [^�� ��� t C o p y   a n d   p a s t e   y o u r   s t a r t i n g   p h r a s e   f r o m   o n e   o f   t h e   t e x t s .� l b����� Z  b����A�� = bi��� o  be�@�@ "0 numwordsentered NumWordsEntered� o  eh�?�? 0 order Order� k  l�    l lw r  lw b  ls	 o  lo�>�> 0 audiophrase AudioPhrase	 m  or

 � R   s t a r t i n g   w i t h   t h e   w o r d s   y o u   h a v e   c h o s e n , o      �=�= 0 audiophrase AudioPhrase 	  XX    �    X X �< l x� r  x� b  x� b  x� b  x� b  x o  x{�;�; "0 commandlinetext CommandLineText m  {~ �    - s   m  � �  " o  ���:�: 0 
start_text   m  �� �    "   o      �9�9 "0 commandlinetext CommandLineText 	  XX    �!!    X X�<  �A  � k  ��"" #$# I ���8%�7
�8 .sysodlogaskr        TEXT% m  ��&& �'' � Y o u r   M a r k o v   O r d e r   d o e s   n o t   m a t c h   t h e   l e n g t h   o f   t h e   s t a r t i n g   p h r a s e .�7  $ ()( I ���6*�5
�6 .sysodelanull��� ��� nmbr* m  ���4�4 �5  ) +�3+ L  ��,, m  ���2
�2 boovfals�3  � 	  XX   � �--    X X�C  � l ��./0. r  ��121 b  ��343 o  ���1�1 0 audiophrase AudioPhrase4 m  ��55 �66 @   f r o m   a   r a n d o m   s t a r t i n g   p h r a s e ,  2 o      �0�0 0 audiophrase AudioPhrase/ 	  XX   0 �77    X X�D  �X  �W  �Y  �f  �e  �h  �g  � 898 l     �/�.�-�/  �.  �-  9 :;: l     �,�+�*�,  �+  �*  ; <=< l     �)�(�'�)  �(  �'  = >?> l     �&@A�&  @ b \==  For completeness, you should check your user input has the correct type and value range:   A �BB � = =     F o r   c o m p l e t e n e s s ,   y o u   s h o u l d   c h e c k   y o u r   u s e r   i n p u t   h a s   t h e   c o r r e c t   t y p e   a n d   v a l u e   r a n g e :? CDC l �E�%�$E Z  �FG�#�"F = ��HIH o  ���!�! 0 usercanceled userCanceledI m  ��� 
�  boovfalsG k  � JJ KLK r  ��MNM m  ��OO �PP  N o      �� 0 	userstext 	UsersTextL QRQ r  ��STS c  ��UVU I  ���W�� 0 getusertext GetUserTextW XYX m  ��ZZ �[[ \ H o w   m a n y   w o r d s   l o n g   s h o u l d   t h e   o u t p u t   t e x t   b e ?Y \�\ m  ��]] �^^  3 0 0�  �  V m  ���
� 
ctxtT o      �� 0 	userstext 	UsersTextR _`_ l ��abca r  ��ded b  ��fgf b  ��hih b  ��jkj o  ���� 0 audiophrase AudioPhrasek m  ��ll �mm    c r e a t i n g   a  i o  ���� 0 	userstext 	UsersTextg m  ��nn �oo "   w o r d   p a r a g r a p h ,  e o      �� 0 audiophrase AudioPhraseb 	  XX   c �pp    X X` q�q l � rstr r  � uvu b  ��wxw b  ��yzy b  ��{|{ o  ���� "0 commandlinetext CommandLineText| m  ��}} �~~    - w  z o  ���� 0 	userstext 	UsersTextx m  �� ���   v o      �� "0 commandlinetext CommandLineTexts 9 3 Needs an extra space if this is the last arg -- XX   t ��� f   N e e d s   a n   e x t r a   s p a c e   i f   t h i s   i s   t h e   l a s t   a r g   - -   X X�  �#  �"  �%  �$  D ��� l     ����  �  �  � ��� l     ����  �  �  � ��� l     ���
�  �  �
  � ��� l     �	���	  � F @===========SET COMMAND LINE TO TIME HOW LONG THE PROGRAM TAKES:    � ��� � = = = = = = = = = = = S E T   C O M M A N D   L I N E   T O   T I M E   H O W   L O N G   T H E   P R O G R A M   T A K E S :  � ��� l ;���� Z  ;����� = ��� o  �� 0 usercanceled userCanceled� m  �
� boovfals� k  7�� ��� l ���� r  ��� I  ���� 0 pickabutton PickAButton� ��� m  �� ��� � D o   y o u   w a n t   t o   t i m e   y o u r   p r o g r a m ,   t o   s e e   h o w   l o n g   e a c h   s t a g e   o f   t h e   a n a l y s i s   t a k e s ?� ��� m  �� ���  N o� �� � m  �� ���  Y e s�   �  � o      ���� 0 
timingthis 
TimingThis� 	  XX   � ���    X X� ���� Z  7������� = %��� o  !���� 0 
timingthis 
TimingThis� m  !$�� ���  Y e s� l (3���� r  (3��� b  (/��� o  (+���� "0 commandlinetext CommandLineText� m  +.�� ���    - t  � o      ���� "0 commandlinetext CommandLineText� ) # XX - if your program has a -t flag   � ��� F   X X   -   i f   y o u r   p r o g r a m   h a s   a   - t   f l a g��  ��  ��  �  �  �  �  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ��������  ��  ��  � ��� l     ������  � " ===  SELECT MULTIPLE FILES:    � ��� 8 = = =     S E L E C T   M U L T I P L E   F I L E S :  � ��� l <������� Z  <�������� = <?��� o  <=���� 0 usercanceled userCanceled� m  =>��
�� boovfals� k  B��� ��� l BO���� r  BO��� I  BK������� 0 	pickfiles 	PickFiles� ��� m  CF�� ��� � O k ,   p l e a s e   s e l e c t   o n e   o r   m o r e   t e x t   f i l e s   t o   c o m b i n e   w o r d   s e q u e n c e s .� ���� o  FG���� 0 
homefolder 
homeFolder��  ��  � o      ���� &0 filepathsasstring FilePathsAsString� 	  XX   � ���    X X� ��� Z  Py������ ? PU��� o  PS���� 0 order Order� m  ST���� � l Xk���� r  Xk��� b  Xg��� b  Xc��� b  X_��� o  X[���� 0 audiophrase AudioPhrase� m  [^�� ��� B   b y   f i n d i n g   i d e n t i c a l   p h r a s e s   o f  � l _b������ o  _b���� 0 order Order��  ��  � m  cf�� ��� �   w o r d s   i n   t h e   i n p u t   f i l e s ,   a n d   r e p e a t e d l y   c h o o s i n g   t h e   n e x t   w o r d   r a n d o m l y   f r o m   a l l   t h e   p o s s i b i l i t i e s   f o u n d .  � o      ���� 0 audiophrase AudioPhrase� 	  XX   � ���    X X��  � l ny���� r  ny��� b  nu��� o  nq���� 0 audiophrase AudioPhrase� m  qt�� ��� �   b y   f i n d i n g   i d e n t i c a l   w o r d s   i n   t h e   i n p u t   f i l e s ,   a n d   r a n d o m l y   c h o o s i n g   t h e   n e x t   w o r d   f r o m   a l l   t h e   p o s s i b i l i t i e s   f o u n d .  � o      ���� 0 audiophrase AudioPhrase� 
  XX	   � ���    X X 	� ���� l z��� � r  z� b  z� o  z}���� "0 commandlinetext CommandLineText o  }����� &0 filepathsasstring FilePathsAsString o      ���� "0 commandlinetext CommandLineText� 	  XX     �    X X��  ��  ��  ��  ��  �  l     ��������  ��  ��   	 l     ��������  ��  ��  	 

 l     ��������  ��  ��    l     ����   - '===========SET AUDIO TO MENTION TIMER:     � N = = = = = = = = = = = S E T   A U D I O   T O   M E N T I O N   T I M E R :    l ������ Z  ������ = �� o  ������ 0 usercanceled userCanceled m  ����
�� boovfals Z  ������ = �� o  ������ 0 
timingthis 
TimingThis m  �� �  Y e s l ��  r  ��!"! b  ��#$# o  ������ 0 audiophrase AudioPhrase$ m  ��%% �&& 4   A n d   I ' m   g o i n g   t o   t i m e   i t ." o      ���� 0 audiophrase AudioPhrase 	  XX     �''    X X��  ��  ��  ��  ��  ��   ()( l     ��������  ��  ��  ) *+* l     ��������  ��  ��  + ,-, l     ��./��  . 3 -===========RUN YOUR PROGRAM OR SHELL SCRIPT:    / �00 Z = = = = = = = = = = = R U N   Y O U R   P R O G R A M   O R   S H E L L   S C R I P T :  - 121 l     ��������  ��  ��  2 343 l ��5����5 Z  ��67����6 = ��898 o  ������ 0 usercanceled userCanceled9 m  ����
�� boovfals7 k  ��:: ;<; Z ��=>����= o  ������ 0 sayingit SayingIt> I ����?��
�� .sysottosnull���     TEXT? o  ������ 0 audiophrase AudioPhrase��  ��  ��  < @A@ Z ��BC����B o  ������ 0 debuggingit DebuggingItC I ����D��
�� .sysodlogaskr        TEXTD b  ��EFE m  ��GG �HH J S e n d i n g   t h i s   c o m m a n d   t o   t h e   c m d   l i n e :F o  ������ "0 commandlinetext CommandLineText��  ��  ��  A I��I r  ��JKJ I ����L��
�� .sysoexecTEXT���     TEXTL o  ������ "0 commandlinetext CommandLineText��  K o      ���� 0 programresult ProgramResult��  ��  ��  ��  ��  4 MNM l     ��������  ��  ��  N OPO l ��Q����Q Z  ��RS����R = ��TUT o  ������ 0 usercanceled userCanceledU m  ����
�� boovfalsS I  ����V���� (0 chooseoutputappfor ChooseOutputAppForV WXW o  ������ 0 programresult ProgramResultX Y��Y m  ��ZZ �[[ 8 T h e   r e s u l t s   a r e   a s   f o l l o w s :  ��  ��  ��  ��  ��  ��  P \]\ l     ��������  ��  ��  ] ^_^ l     ��`a��  ` > 8=====================END OF MAIN========================   a �bb p = = = = = = = = = = = = = = = = = = = = = E N D   O F   M A I N = = = = = = = = = = = = = = = = = = = = = = = =_ cdc l     ��������  ��  ��  d e��e l     ��������  ��  ��  ��       ��fghijklmnop��  f 
����������������~�}�� $0 interactwithuser InteractWithUser�� 0 pickabutton PickAButton�� 0 pickfromlist PickFromList�� 0 getusertext GetUserText�� 0 pickafolder PickAFolder�� 0 	pickafile 	PickAFile�� 0 	pickfiles 	PickFiles� 0 sendoutputto SendOutputTo�~ (0 chooseoutputappfor ChooseOutputAppFor
�} .aevtoappnull  �   � ****g �| ��{�zqr�y�| $0 interactwithuser InteractWithUser�{ �xs�x s  �w�v�w 0 comment Comment�v 0 choice Choice�z  q �u�t�u 0 comment Comment�t 0 choice Choicer �s�r�q�p�s 0 debuggingit DebuggingIt
�r .sysodlogaskr        TEXT�q 0 sayingit SayingIt
�p .sysottosnull���     TEXT�y  � ��%j Y hO� ��%j Y hh �o ��n�mtu�l�o 0 pickabutton PickAButton�n �kv�k v  �j�i�h�j 0 question Question�i 0 firstchoice FirstChoice�h 0 defaultchoice DefaultChoice�m  t �g�f�e�d�c�g 0 question Question�f 0 firstchoice FirstChoice�e 0 defaultchoice DefaultChoice�d 0 
answertext 
AnswerText�c 0 dialoganswer DialogAnsweru 
 ��b�a�`�_�^�]�\ ��[�b 0 sayingit SayingIt
�a .sysottosnull���     TEXT
�` 
btns
�_ 
dflt�^ 
�] .sysodlogaskr        TEXT
�\ 
bhit�[ $0 interactwithuser InteractWithUser�l 2�E�O� 
�j Y hO�㡢lv�k� E�O��,E�O*�l+ 	O�i �Z ��Y�Xwx�W�Z 0 pickfromlist PickFromList�Y �Vy�V y  �U�T�S�U "0 listinstruction ListInstruction�T 0 listofitems ListOfItems�S 0 defaultitem DefaultItem�X  w �R�Q�P�O�N�R "0 listinstruction ListInstruction�Q 0 listofitems ListOfItems�P 0 defaultitem DefaultItem�O 0 listpick ListPick�N 0 
listresult 
ListResultx  ��M�L�K�J�I�H�G�F�E%�D�M 0 sayingit SayingIt
�L .sysottosnull���     TEXT
�K 
okbt
�J 
prmp
�I 
inSL�H 
�G .gtqpchltns    @   @ ns  �F 0 usercanceled userCanceled
�E 
cobj�D $0 interactwithuser InteractWithUser�W >�E�O� 
�j Y hO������ E�O�f  eE�Y ��k/E�O*�l+ O�j �C2�B�Az{�@�C 0 getusertext GetUserText�B �?|�? |  �>�=�> 0 userquestion UserQuestion�= 0 defaulttext defaultText�A  z �<�;�:�9�< 0 userquestion UserQuestion�; 0 defaulttext defaultText�: 0 
useranswer 
UserAnswer�9 0 	boxanswer 	BoxAnswer{ ?�8q�7�6�5�4�3�2`�1�0}�8 0 usercanceled userCanceled
�7 
bool�6 0 sayingit SayingIt
�5 .sysottosnull���     TEXT
�4 
dtxt
�3 .sysodlogaskr        TEXT
�2 
ttxt�1 $0 interactwithuser InteractWithUser�0  } �/�.�-
�/ 
errn�.���-  �@ N�E�O Eh�
 ���& *� 
�j Y hO��l E�O��,E�O*�l+ 
W 
X  eE�[OY��O�k �,}�+�*~�)�, 0 pickafolder PickAFolder�+ �(��( �  �'�&�' 0 instruction Instruction�& 0 defaultpath DefaultPath�*  ~ �%�$�#�"�!�% 0 instruction Instruction�$ 0 defaultpath DefaultPath�# $0 folderpathstring FolderPathString�" 0 chosenfolder ChosenFolder�! 0 posixfolder PosixFolder �� ����������������  0 sayingit SayingIt
� .sysottosnull���     TEXT
� 
prmp
� 
dflc� 
� .sysostflalis    ��� null�  � ���
� 
errn����  � 0 usercanceled userCanceled� 0 debuggingit DebuggingIt
� .sysodlogaskr        TEXT
� 
psxp�) h�E�O � 
�j Y hO*��� E�W 
X  eE�O� 4� �%j Y hO��,E�O�%�%E�O� a �%j Y hY hO�l �������� 0 	pickafile 	PickAFile� ��� �  ��� 0 instruction Instruction� 00 defaultfolderpathalias DefaultFolderPathAlias�  � ��
�	��� 0 instruction Instruction�
 00 defaultfolderpathalias DefaultFolderPathAlias�	  0 filepathstring FilePathString� 0 
chosenfile 
ChosenFile� 0 	posixfile 	PosixFile� �������� �������%����57?� 0 sayingit SayingIt
� .sysottosnull���     TEXT
� 
prmp
� 
ftyp
� 
dflc� 
�  .sysostdfalis    ��� null��  � ������
�� 
errn������  �� 0 usercanceled userCanceled�� 0 debuggingit DebuggingIt
�� .sysodlogaskr        TEXT
�� 
psxp� p�E�O "� 
�j Y hO*���kv�� E�W 
X 	 
eE�O� 8� ��%j Y hO��,E�Oa �%a %E�O� a �%j Y hY hO�m ��K���������� 0 	pickfiles 	PickFiles�� ����� �  ������ 0 instruction Instruction�� 00 defaultfolderpathalias DefaultFolderPathAlias��  � �������������� 0 instruction Instruction�� 00 defaultfolderpathalias DefaultFolderPathAlias��  0 filepathstring FilePathString�� 0 chosenfiles ChosenFiles�� 0 	filealias 	FileAlias�� 0 	posixfile 	PosixFile� X��������y������������������������������� 0 sayingit SayingIt
�� .sysottosnull���     TEXT
�� 
prmp
�� 
ftyp
�� 
dflc
�� 
mlsl�� 
�� .sysostdfalis    ��� null��  � ������
�� 
errn������  �� 0 usercanceled userCanceled
�� 
kocl
�� 
cobj
�� .corecnte****       ****�� 0 debuggingit DebuggingIt
�� .sysodlogaskr        TEXT
�� 
psxp�� ��E�O $� 
�j Y hO*���kv��e� 	E�W 
X 
 eE�O� W =�[��l kh _  a �%j Y hO�a ,E�O�a %�%a %E�[OY��O_  a �%j Y hY hO�n ������������� 0 sendoutputto SendOutputTo�� ����� �  �������� 0 	chosenapp 	ChosenApp�� 0 docbody DocBody�� 0 docname DocName��  � ���������� 0 	chosenapp 	ChosenApp�� 0 docbody DocBody�� 0 docname DocName�� 0 
themessage 
theMessage� "���������������������0����������������������'��*>;������H
�� .JonspClpnull���     ****
�� 
capp�� 0 sayingit SayingIt�� 0 debuggingit DebuggingIt
�� 
bool
�� .sysodelanull��� ��� nmbr
�� .sysottosnull���     TEXT
�� .aevtoappnull  �   � ****
�� .miscactvnull��� ��� null
�� 
kocl
�� 
bcke
�� 
prdt
�� 
pvis
�� 
subj
�� 
ctnt�� �� 
�� .corecrel****      � null
�� 
trcp
�� 
pnam
�� 
radd
�� 
faal
�� eMdsKcmd
�� .prcskprsnull���     ctxt�� ɡj  O*�/ ��	 ��& �j O�j Y hO*j 	O*j 
Okj O��  
lj Y hO��  N� F*��a a ea �a �a a  E�O� "*�a a a a a a a a  OPUUY +a  a a a l  UOa  a !a a l  UOPUo ��W���������� (0 chooseoutputappfor ChooseOutputAppFor�� ����� �  ������ 0 results Results�� 0 title Title��  � ������������ 0 results Results�� 0 title Title�� 0 	outputapp 	OutputApp��  0 outputquestion OutputQuestion�� "0 outputappanswer OutputAppAnswer� do�������������������������������������� 0 sayingit SayingIt
�� .sysottosnull���     TEXT�� 
�� 
okbt
�� 
appr
�� 
inSL
�� 
prmp�� 
�� .gtqpchltns    @   @ ns  
�� 
cobj�� $0 interactwithuser InteractWithUser�� 0 sendoutputto SendOutputTo��  � ������
�� 
errn������  �� 0 usercanceled userCanceled�� e�E�O U�E�O� 
�j Y hO�����v������kv�a  E�O�f  �a k/E�O*a �l+ O*���m+ Y hW X  eE` p �����������
�� .aevtoappnull  �   � ****� k    ���  ��  ��  ��  0��  :��  F��  W��  ^��  m�� ��� �� '�� ��� C�� ��� ��� �� 3�� O����  ��  ��  �  � \������ 7�� A�������� U������ i k�� t����������9@DHK��N���Y�~fq|������}�����|�{�z�y�x�w�
&�v5OZ]ln}����u����t�s���%G�r�qZ�p�� 0 sayingit SayingIt�� 0 debuggingit DebuggingIt�� 0 usercanceled userCanceled�� 0 compiler Compiler�� 0 yourprogname YourProgName
�� 
rtyp
�� 
ctxt
�� .earsffdralis        afdr
�� 
psxp�� 0 
homefolder 
homeFolder�� *0 yourprognameasposix YourProgNameAsPOSIX�� "0 commandlinetext CommandLineText�� 0 audiophrase AudioPhrase�� 0 pickabutton PickAButton�� 0 fionaanswer FionaAnswer
�� .sysottosnull���     TEXT�� �� 0 pickfromlist PickFromList� 0 	userstext 	UsersText�~ 0 order Order�} 0 usestartseq UseStartSeq�| 0 getusertext GetUserText�{ 0 
start_text  
�z 
cwor
�y .corecnte****       ****�x "0 numwordsentered NumWordsEntered
�w .sysodelanull��� ��� nmbr
�v .sysodlogaskr        TEXT�u 0 
timingthis 
TimingThis�t 0 	pickfiles 	PickFiles�s &0 filepathsasstring FilePathsAsString
�r .sysoexecTEXT���     TEXT�q 0 programresult ProgramResult�p (0 chooseoutputappfor ChooseOutputAppFor���fE�OfE�OfE�O�E�O�E�O)��l 	�%�,E�O��%E�O��%�%�%E` Oa E` O*a a a m+ E` O_ a   eE�Oa j Oa E` Y hO�f  �*a a a a a  a !va "m+ #E` $O_ $a %  
kE` &Y ;_ $a '  
lE` &Y )_ $a (  
mE` &Y _ $a )  a !E` &Y hO_ _ $%a *%E` O_ a +%_ &%E` Y hO�f  �*a ,a -a .m+ E` /O_ /a 0  �*a 1_ &%a 2%a 3l+ 4E` 5O_ 5a 6-j 7E` 8Okj 9O_ 5a : E_ 8_ &  (_ a ;%E` O_ a <%a =%_ 5%a >%E` Y a ?j @Okj 9OfY _ a A%E` Y hY hO�f  Fa BE` $O*a Ca Dl+ 4�&E` $O_ a E%_ $%a F%E` O_ a G%_ $%a H%E` Y hO�f  1*a Ia Ja Km+ E` LO_ La M  _ a N%E` Y hY hO�f  H*a O�l+ PE` QO_ &k _ a R%_ &%a S%E` Y _ a T%E` O_ _ Q%E` Y hO�f  _ La U  _ a V%E` Y hY hO�f  4� _ j Y hO� a W_ %j @Y hO_ j XE` YY hO�f  *_ Ya Zl+ [Y h ascr  ��ޭ