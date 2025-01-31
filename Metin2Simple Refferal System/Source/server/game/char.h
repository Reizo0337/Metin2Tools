1. Search:

		BYTE			GetChatCounter() const;

2. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
		const char * 	GetPlayerRefferal() const;
#endif

3. Search:

		BYTE			m_bCharType;

4. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
		std::string 	m_Refferal;
#endif