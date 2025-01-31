1. Search:

ACMD(do_stun);

2. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
ACMD(do_refferal_info);
#endif

3. Search:

	{ "respawn",	do_respawn,		0,			POS_DEAD,	GM_WIZARD	},

4. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
	{ "refferal_info", do_refferal_info, 0,		POS_DEAD, GM_IMPLEMENTOR },
#endif