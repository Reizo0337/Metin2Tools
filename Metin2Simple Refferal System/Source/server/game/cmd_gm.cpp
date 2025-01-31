1. add.

#ifdef ENABLE_REFFERAL_SYSTEM
ACMD(do_refferal_info)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));
	
	if (!*arg1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Usage: refferal_info <code>");
		return;
	}
	
	char szQuery[1024+1];
	
	snprintf(szQuery, sizeof(szQuery), 
		"SELECT COUNT(refferal) FROM player.player WHERE refferal = '%s'", arg1);

	std::unique_ptr<SQLMsg> msg(DBManager::instance().DirectQuery(szQuery));

	if (msg->Get()->uiNumRows == 0)
	{
		return;
	}

	MYSQL_ROW row = mysql_fetch_row(msg->Get()->pSQLResult);
	
	ch->ChatPacket(CHAT_TYPE_TALKING, "In acest moment %s utilizatori folosesc refferalul %s", row[0], arg1);
}
#endif