# Holiday Island Remastered

This is my attempt to build my version of Sunflower's Holiday Island from 1995. I used to play this game as a child and
I loved it! That being said, I know the "mechanics" weren't the most realistic, that's why I am also thinking about
adding my own personal flavour to my version of the game. I still want to keep the original design - thus I have
downloaded the game files (very easy nowadays) and started using the original tile set.

If you want to see what I have achieved so far, I am adding screenshots to the end of this readme to document my progress.

## Todos - short term:

### cut out tiles
- annoying but necessary, the map tiles are in a tile collection, but it is way easier to use them when extracted into
  single files
- if you have a better solution, I am more than open!

### generate a random height map
- my current algorithm is optimizable
- I would like to make it:
  - based on factors e.g. max terrain level, hilliness, water, no water, etc.
  - based on a seed, I don't know much about procedural map generation, but if it makes sense, I want to implement it
- one thing to keep in mind is, that there must not be any jumps > 1 vertically or horizontally, since the original
  tiles do not support that
- I do not know yet if I want the maps to always start on level 0 on the edges, or maybe higher. It looks like a bowl if the map
  starts at 3 on the edges and instantly goes lower, so I got to figure that out

### implement scrolling

- implement the cursor
- in the original game, you had to right click to move the window, I want to make it scrollable by moving the cursor to
  the edge of the window like in every modern building game

### hover effect

- when hovering over the map, I want to see the outlines of the tile I am hovering over, this is going to get more
  important later

### terrain type

- render the correct type of terrain - sand, water, grass - based on the current terrain level
    - 0 = water
    - 1 & 2 = sand
    - above 2 = grass

- add terrain type variation tiles, if existent

### rivers

- there are river tiles, I don't know how or where to use them yet, so this is more of a "think about" todo

## Todos - long term

### add the UI elements

### add the building functionality

### add terrain modifications

### add the news window

### add more terrain types, snow, rock, maybe volcanoes that can cause special events etc

### ...


## Progress
![img_0.png](progress/img_0.png)
![img_1.png](progress/img_1.png)
![img_2.png](progress/img_2.png)
