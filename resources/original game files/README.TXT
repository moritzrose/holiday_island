Contents

1.0   VESA BIOS Extension
1.a     Why VESA BIOS Extension?

2.0   Possible problems and their solution
2.1     Problems with graphics reproduction
2.2     Memory problems
2.3     Virtual memory
2.4     Smartdrive
2.5     Music and Sound reproduction



1.  VESA BIOS Extension

1.1  When you run HOLIDAY ISLAND for the first time with 
     VESA BIOS extensions, you will be asked to select either 
     "Auto-detect" or "Manual Override".

1.2  Auto-detect: This choice causes the installation program to
     attempt to automatically detect your computer´s hardware and 
     specifications and then define the correct settings for your 
     graphics card. All current cards ought to be recognised. 
     If this doesn´t seem to be the case for your card, however, 
     look at item 1.3 "Manual Override".
1.3  Manual Override: This selection asks you to manually enter the 
     technical data for your graphics card. (This information 
     should be available in the graphics card´s documentation.
     If you are still having difficulties, consult the card´s 
     supplier.)
1.4  Your first choice should be "Auto-detect". If you should then 
     have problems with your graphics card being recognised, then 
     you should follow the instructions in item 1.3 above. Usually 
     it is sufficient to manually enter "VGA ID". (More detailed 
     information should be available in the graphics card´s 
     documentation, or if you are still having difficulties, please
     consult the card´s supplier.)
1.5  After pressing "Auto-detect" or OK after "Manual Override", 
     the monitor screen will go black for a moment. 
     Now the program UNIVBE will check through all of its known 
     video modes, when you confirm with OK. This may be accompanied 
     by pronounced screen flicker and noise from your monitor. 
     Now HOLIDAY ISLAND will load. From now on, every time you run 
     HOLIDAY ISLAND, UNIVBE will initialise automatically. If the 
     screen remains black for longer than 20 seconds, press a key.

1.a     Why VESA BIOS Extension?

HOLIDAY ISLAND can place great demands on your graphics card and the 
VESA BIOS extensions accelerate the generation of graphics and screen
scrolling.
We recommend particularly that owners of computers with 486 processors
and 8 MB RAM should run HOLIDAY ISLAND with VESA BIOS extensions.


2.0  Possible problems and their solution

If you're having technical problems with Holiday Island, please read 
the following section.

2.1    Problems with graphics reproduction

Question:
   In Windows 95 the Task Bar is covering part of the screen. 

Answer:
   Click on the START button and select the Settings menu item. 
   Select the Task Bar in the sub-menu and then turn off the switch 
   <Always on top>

Question:
   Why do the graphics jump sometimes?

Answer:
   You're using a 486 DX2/66 or a 486 DX4/100 and you have a 
   network card which is operational. Turn off the network and 
   the animations in Holiday Island's Options menu.

Question:
   The graphics reproduction is faulty.

Answer:
   In order to run, Holiday Island must have a graphics driver 
   which supports a minimum of 256 colours. Check further details 
   in either your graphics card's manual or in the next section.
   Holiday Island runs under Windows in all resolutions with at 
   least 640x480 pixels.
   We recommend that the game is first started at 800x600 
   supporting 256 colours.
   Instructions on changing the 256 colour mode and screen 
   resolutions can be found either in your computer's or your 
   graphic card's documentation.

To change the Windows graphics driver...

1.	Run Windows (if you haven't already done so) and click on the 
	Setup icon. This is usually located in the 'Main' program 
	group window.
2.	Select the menu item 'Change System Settings'.
3.	Click on the arrow next to the current graphics driver. A list 
	of all available drivers now appears.
4.	Look for the corresponding graphics driver with a 640x480 
	(800x600) resolution for YOUR graphics card. If it isn't listed 
	then select 'Other display'. NOTE! You 	will now need the 
	Windows driver disk for your graphics card and possibly the 
	installation disks for Windows itself. Ask your computer dealer 
	for this disk, if it wasn't supplied when you bought the computer. 
5.	When you are asked for the path for the new driver, enter A:\ 
	if you've placed the diskette in drive A:\ . Now click on OK.
	IMPORTANT! If your computer wasn't supplied together with the 
	original Windows disks, ask your dealer for further assistance.
6.	If you have selected a driver which has already been installed 
	on your system (Windows gives this information) then use this 
	one in preference to all others.
7.	In order to initialise the newly selected driver, you will have 
	to restart Windows. Click on the corresponding dialogue box.
8.	To return your computer to its original specification after 
	playing Holiday Island - repeat these instructions, but this 
	time install your original driver. 


2.2    Memory Problems

Question: 
   What's happening when I get an error message concerning memory?

Answer: 
   You must have a minimum of 8 MB RAM to run Holiday Island. 
   (We recommend 16 MB under Windows 95). To find out how much RAM 
   you computer has available, click on Help in Program Manager and 
   select 'About Program Manager' in the menu. At the bottom of the 
   window that now appears, you can read off the amount of RAM 
   against the item - 'memory:'


2.3    Virtual Memory
   You can increase the available memory by creating additional 
   Windows virtual memory. Virtual memory uses a defined space on 
   the hard disk which then behaves like RAM.
   It's not particularly recommended to use virtual memory to reach 
   the required 8 MB of RAM. Holiday Island will run very slowly 
   and won't be too much fun to play. However if you use virtual 
   memory to supplement an existing 8 MB of RAM, then you can increase 
   the speed of play and consequently your enjoyment of the game.
   Refer to your Windows manual for instructions on setting up 
   virtual memory. 


2.4   SMARTdrive
   If there are problems to start HOLIDAY ISLAND under Windows 3.xx, 
   you can solve this by deactivating SMARTDRV in the AUTOEXEC.BAT 
   file.

2.5   Sound and Music Reproduction

Question:
   I can hear the sound effects in Holiday Island, but no background 
   music. How can I fix this?

Answer:
   Holiday Island uses two methods to produce sound. Voice and sound 
   effects are digitally reproduced, while MIDI is used for the music
   reproduction. Therefore the MIDI part of your configuration may 
   not be properly set up. To test this, carry out the following 
   instructions:

1.	Go into Windows Program Manager and open the 'Main' program 
	group.

2.	Double click on 'Control Panel' and then on 'MIDI-Mapper'. 
	NOTE! Some configurations may not have a MIDI-Mapper icon, when 
	this is the case it's probable that your sound card does not 
	have MIDI capability. Ask your dealer or contact the 
	manufacturer of your sound card. 

3. 	In MIDI-Mapper you'll see a list of names of drivers.

	We suggest the following settings:


Your  sound card		Requires the following driver

Ad-Lib Gold 1000		Gold Synth
Aria Sound Synthesiser		Aria Ext
Ensoniq Soundscape		SNDSCAPE Synth
Gravis Ultrasound		Ultrasnd
Gravis Ultrsound max		Ultrasound
Microsoft Sound System		Sound System
ProAudio 16 Basic		Extended FM
ProAudio Spectrum 16		Ext FM
ProAudio Studio 16		Ext FM
Reveal SC400			Sound FX Ext FM
Reveal SC600			Sound FX Synt
Soundblaster			SB Ext FM
Soundblaster Pro 2		SBP2 Extended MIDI
Soundblaster 16			SB 16 Ext FM
Soundblaster AWE 32		SB AWE 32
Sound Canvas (compatible)	All MIDI drivers

If you do make changes, first of all make a note of your original 
configuration, so that you can return to this if you wish.

4.	Close MIDI-Mapper and return to Holiday Island. If the 
	settings are correct, you should now hear music playback.	

5.	If you're still not hearing anything, open the 'Media Player' 
	in the Accessories program group. 
	Select Open in the file menu, while also selecting MIDI 
	sequencer file types (.MID, .RMI). Double click on CANYON.MID 
	and hit the play button. If you still don't hear any music 
	refer back to your dealer, or the manufacturer of your 
	sound card and ask them how to obtain MIDI playback under 
	Windows.







