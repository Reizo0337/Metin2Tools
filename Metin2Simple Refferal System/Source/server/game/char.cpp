1. Search:	
	m_iSyncHackCount = 0;

2. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
	m_Refferal = "";
#endif

3. Search:

	m_dwPlayerID = t->id;

4. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
	m_Refferal = t->refferal;
#endif

5. Search in void CHARACTER::PointChange(BYTE type, long long amount, bool bAmount, bool bBroadcast)

case POINT_LEVEL:

6. Add at the end of the case

#ifdef ENABLE_REFFERAL_SYSTEM
			if (strlen(GetPlayerRefferal()) > 0)
			{
				if (GetLevel() == 10 || GetLevel() == 20 || GetLevel() == 30 || GetLevel() == 40 || GetLevel() == 50 || GetLevel() == 60 || GetLevel() == 70 || GetLevel() == 80 || GetLevel() == 90 || GetLevel() == 120)
				{
					ChatPacket(CHAT_TYPE_INFO, "Deoarece ai avansat in nivel si folosesti acest refferal %s, ai primit un bonus!", GetPlayerRefferal());
					AutoGiveItem(REFFERAL_REWARD_VNUM, REFFERAL_REWARD_COUNT);
				}
			}
#endif

7. Add at the end of the file:

#ifdef ENABLE_REFFERAL_SYSTEM
const char* CHARACTER::GetPlayerRefferal() const
{
	return m_Refferal.c_str();
}
#endif