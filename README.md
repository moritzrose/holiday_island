# Holiday Island Remastered

This is my attempt to build my version of Sunflower's Holiday Island from 1995. I used to play this game as a child and
I loved it! That being said, I know the "mechanics" weren't the most realistic, that's why I am also thinking about
adding my own personal flavour to my version of the game. I still want to keep the original design - thus I have
downloaded the game files (very easy nowadays) and started using the original tile set.

So far, I did quite a bit of research on isometric game design and I am very proud to have build a small map
generator, that renders the tiles based on a height map. If you check out the repo and run the MapGenerator, you can see
the current state.

## Todos - short term:

### generate a random height map

- based on factors e.g. max terrain level, hilliness, water, no water, etc.
- based on a seed, I don't know much about procedural map generation, but if it makes sense, I want to implement it
- one thing to keep in mind is, that there must not be any jumps > 1 vertically or horizontally, since the original
  tiles do not support that

### implement scrolling

- implement the cursor
- in the original game, you had to right click to move the window, I want to make it scrollable by moving the cursor to
  the edge of the window like every modern game building game

### hover effect

- when hovering over the map, I want to see the outlines of the tile I am hovering over, this is going to get more
  important later

### terrain type

- render the correct type of terrain - sand, water, grass - based on the current terrain level

## Todos - long term

### add the UI elements
### add the building functionality
### add terrain modifications
### add the news window
### ...
