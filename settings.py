# the level of the map is denoted by a list of strings
# X is where it is blocked
level_map = [
'                            ',
'                            ',
'                            ',
'                            ',
' XX    XXX            XX    ',
' XXP                        ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

# setting up the screen dimension according to the map
tile_size = 40
screen_width = len(level_map[0]) * tile_size
screen_height = (len(level_map)) * tile_size
