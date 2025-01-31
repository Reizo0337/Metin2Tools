tables.h

1. Search:

} TPlayerTable;

2. Add before:

#ifdef ENABLE_REFFERAL_SYSTEM
	char 	refferal[CHARACTER_NAME_MAX_LEN + 1];
#endif

