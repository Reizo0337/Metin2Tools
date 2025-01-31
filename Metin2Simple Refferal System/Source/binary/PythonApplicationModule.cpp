PythonApplicationModule.cpp

1. Search for:

#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif


2. Add:

#ifdef ENABLE_REFFERAL_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_REFFERAL_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_REFFERAL_SYSTEM",	0);
#endif
