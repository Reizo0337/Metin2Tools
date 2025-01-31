PythonNetworkStreamModule.cpp

1. Search:

PyObject* netSendCreateCharacterPacket(PyObject* poSelf, PyObject* poArgs)

2. Add after the last argument:

#ifdef ENABLE_REFFERAL_SYSTEM
	char* refferal;
	if (!PyTuple_GetString(poArgs, 1, &refferal))
		return Py_BuildException();
#endif

3. Search:

rkNetStream.SendCreateCharacterPacket((BYTE) index, name, (BYTE) job, (BYTE) shape, stat1, stat2, stat3, stat4);

4. Replace with:

#ifdef ENABLE_REFFERAL_SYSTEM
	rkNetStream.SendCreateCharacterPacket((BYTE) index, name, (BYTE) job, (BYTE) shape, stat1, stat2, stat3, stat4, refferal);
#else
	rkNetStream.SendCreateCharacterPacket((BYTE) index, name, (BYTE) job, (BYTE) shape, stat1, stat2, stat3, stat4);
#endif