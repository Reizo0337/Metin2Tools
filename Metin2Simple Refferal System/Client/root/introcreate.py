introcreate.py

1. Search:

			self.editCharacterName = getChild("character_name_value")

2. Add:

			if app.ENABLE_REFFERAL_SYSTEM:
				self.editRefferalName = getChild("refferal_value")

3. Search:

		self.shapeButtonList[0].SetEvent(ui.__mem_func__(self.__SelectShape), SHAPE0)
		self.shapeButtonList[1].SetEvent(ui.__mem_func__(self.__SelectShape), SHAPE1)

4. Replace the editCharacterName with:
		if app.ENABLE_REFFERAL_SYSTEM:
			self.editCharacterName.SetReturnEvent(ui.__mem_func__(self.editCharacterName.SetFocus))
			self.editCharacterName.SetTabEvent(ui.__mem_func__(self.editRefferalName.SetFocus))

			self.editRefferalName.SetReturnEvent(ui.__mem_func__(self.CreateCharacter))
			self.editRefferalName.SetTabEvent(ui.__mem_func__(self.editCharacterName.SetFocus))

5. Search:

self.editCharacterName.SetText("")

6. Add:

		if app.ENABLE_REFFERAL_SYSTEM:
			self.editRefferalName.SetText("")

7. Search:

		self.editCharacterName.Enable()

8. Add:

		if app.ENABLE_REFFERAL_SYSTEM:
			self.editRefferalName.Enable()


9. Search:

		self.editCharacterName = 0

10. Add:

		if app.ENABLE_REFFERAL_SYSTEM:
			self.editRefferalName = 0

11. Search:

		self.editCharacterName.Disable()

12. Add:

		if app.ENABLE_REFFERAL_SYSTEM:
			self.editRefferalName.Disable()

13. Search:

		textName = self.editCharacterName.GetText()

14. Add:

		if app.ENABLE_REFFERAL_SYSTEM:
			refferalName = self.editRefferalName.GetText()

15. Search:

			if FALSE == self.__CheckCreateCharacter(textName):
				return

16. Replace that with:

		if app.ENABLE_REFFERAL_SYSTEM:
			if FALSE == self.__CheckCreateCharacter(textName) or FALSE == self.__CheckRefferal(refferalName):
				return
		else:
			if FALSE == self.__CheckCreateCharacter(textName):
				return

17. Add at the bottom of the file:

	if app.ENABLE_REFFERAL_SYSTEM:
		def __CheckRefferal(self, refferal_name):
			if net.IsInsultIn(refferal_name):
				self.PopupMessage(localeInfo.CREATE_ERROR_INSULT_NAME, self.EnableWindow)
				return FALSE

			return TRUE

18. Search:

				textName = self.editCharacterName.GetText()

19. Add:

				if app.ENABLE_REFFERAL_SYSTEM:
					refferalName = self.editRefferalName.GetText()

20. Search:

					net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, statCon, statInt, statStr, statDex)

21. Replace that with:


				if app.ENABLE_REFFERAL_SYSTEM:
					net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, statCon, statInt, statStr, statDex, refferalName)
				else:
					net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, statCon, statInt, statStr, statDex)

