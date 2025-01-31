input_login.cpp

1. Search:

bool NewPlayerTable2(TPlayerTable * table, const char * name, BYTE race, BYTE shape, BYTE bEmpire)

2. Replace:

#ifdef ENABLE_REFFERAL_SYSTEM
bool NewPlayerTable2(TPlayerTable * table, const char * name, BYTE race, BYTE shape, const char * refferal, BYTE bEmpire)
#else
bool NewPlayerTable2(TPlayerTable * table, const char * name, BYTE race, BYTE shape, BYTE bEmpire)
#endif

3. Search in the same function:

	table->skill_group = 0;

4. Add after:

#ifdef ENABLE_REFFERAL_SYSTEM
	strlcpy(table->refferal, refferal, sizeof(table->refferal));
#endif

5. Search in CharacterCreate:

if (!check_name(pinfo->name) || pinfo->shape > 1)

6. Replace with:

#ifdef ENABLE_REFFERAL_SYSTEM
	if (!check_name(pinfo->name) || pinfo->shape > 1 || !check_name(pinfo->refferal))
#else
	if (!check_name(pinfo->name) || pinfo->shape > 1)
#endif	

7. Search in the same function:

if (!NewPlayerTable2(&player_create_packet.player_table, pinfo->name, pinfo->job, pinfo->shape, d->GetEmpire()))

8. Replace with:

#ifdef ENABLE_REFFERAL_SYSTEM
	if (!NewPlayerTable2(&player_create_packet.player_table, pinfo->name, pinfo->job, pinfo->shape, pinfo->refferal, d->GetEmpire()))
#else
	if (!NewPlayerTable2(&player_create_packet.player_table, pinfo->name, pinfo->job, pinfo->shape, d->GetEmpire()))
#endif	

9. Search:

void CInputLogin::CharacterCreate(LPDESC d, const char * data)

10. Add after:

#ifdef ENABLE_REFFERAL_SYSTEM
int check_refferal(const char* string)
{
	if (strlen(string) ==  0) return 1;
	
	std::unique_ptr<SQLMsg> pMsg (DBManager::instance().DirectQuery("SELECT code FROM player.refferal_data WHERE code='%s'", string));
	if (pMsg->Get()->uiNumRows > 0) 
	{
		return 1;
	}
	
	return 0;
}
#endif

11. Add at the end of void CInputLogin::Entergame(LPDESC d, const char * data)

#ifdef ENABLE_REFFERAL_SYSTEM
	if (ch->GetQuestFlag("refferal.use") == 0 && ch->GetLevel() <= 1) // here you put the start level.
	{
		if (strlen(ch->GetPlayerRefferal()) > 0)
		{
			// give the player bonus.
			ch->ChatPacket(CHAT_TYPE_INFO, "Ai primit un bonus, deoarece ai folosit refferalul: %s", ch->GetPlayerRefferal());
			ch->AutoGiveItem(REFFERAL_REWARD_VNUM, REFFERAL_REWARD_COUNT);
			
			// let's set it to never give more bonuses to the player.
			ch->SetQuestFlag("refferal.use", 1);
		}
	}
#endif