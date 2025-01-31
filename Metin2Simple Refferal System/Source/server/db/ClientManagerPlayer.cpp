ClientManagerPlayer.cpp

1. Search:

str_to_number(pkTab->horse_skill_point, row[col++]);

2. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
	strlcpy(pkTab->refferal, row[col++], sizeof(pkTab->refferal));
#endif

3. Search in the select of the player data:

"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point FROM player%s WHERE id=%d", 

4. Add after:

,refferal

5. Search:

"hp, mp, random_hp, random_sp, stat_point, stamina, part_base, part_main, part_hair, gold, playtime, 

6. Add after playtime:

refferal,

7. Search:

	CDBManager::instance().EscapeString(text, packet->player_table.skills, sizeof(packet->player_table.skills));
	queryLen += snprintf(queryStr + queryLen, sizeof(queryStr) - queryLen, "'%s', ", text);
	
8. Add below:

#ifdef ENABLE_REFFERAL_SYSTEM
	CDBManager::instance().EscapeString(text, packet->player_table.refferal, sizeof(packet->player_table.refferal));
	queryLen += snprintf(queryStr + queryLen, sizeof(queryStr) - queryLen, "'%s', ", packet->player_table.refferal);
#endif

