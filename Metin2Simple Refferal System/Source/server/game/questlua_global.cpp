1. Add:
#ifdef ENABLE_REFFERAL_SYSTEM
#include "db.h"
#endif

2. Search:

	void RegisterGlobalFunctionTable(lua_State* L)
	{

3. Add before:

#ifdef ENABLE_REFFERAL_SYSTEM
	int _add_new_refferal(lua_State* L)
	{
		const char* refferal = lua_tostring(L, 1);
		
		DBManager::instance().DirectQuery("INSERT INTO player.refferal_data(code) VALUES ('%s')", refferal);

		sys_log(0, "QUEST_LOG: refferal_system: ADDED NEW REFFERAL: %s", refferal);

		return 0;
	}

	int _remove_refferal(lua_State* L)
	{
		const char* refferal = lua_tostring(L, 1);
		
		DBManager::instance().DirectQuery("DELETE FROM player.refferal_data WHERE code = '%s'", refferal);

		sys_log(0, "QUEST_LOG: refferal_system: REMOVED REFFERAL: %s", refferal);

		return 0;
	}
#endif

4. Search:
	luaL_reg global_functions[] =
		{

5. Add After:

#ifdef ENABLE_REFFERAL_SYSTEM
			{	"add_new_refferal",			_add_new_refferal		},
			{	"remove_refferal",			_remove_refferal 		},
#endif