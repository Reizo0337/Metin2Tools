packet.h

1. Search:

typedef struct command_player_create


2. Add after the last one:

#ifdef ENABLE_REFFERAL_SYSTEM
	char 	refferal[CHARACTER_NAME_MAX_LEN + 1];
#endif