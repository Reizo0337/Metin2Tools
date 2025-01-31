PythonNetworkStreamPhaseSelect.cpp

1. Search:

bool CPythonNetworkStream::SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byCON, BYTE byINT, BYTE bySTR, BYTE byDEX)

2. Replace with:

#ifdef ENABLE_REFFERAL_SYSTEM
bool CPythonNetworkStream::SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byCON, BYTE byINT, BYTE bySTR, BYTE byDEX, const char *refferal)
#else
bool CPythonNetworkStream::SendCreateCharacterPacket(BYTE index, const char *name, BYTE job, BYTE shape, BYTE byCON, BYTE byINT, BYTE bySTR, BYTE byDEX)
#endif

3. Search:

	createCharacterPacket.DEX = byDEX;

4. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
	strncpy(createCharacterPacket.refferal, refferal, CHARACTER_NAME_MAX_LEN);
#endif
