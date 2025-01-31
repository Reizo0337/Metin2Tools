createcharacterwindow.py 



				##REFFERAL
				{
					"name" : "character_name",
					"type" : "text",

					"x" : 43,
					"y" : 218+ 29,

					"text" : "Refferal",

					"text_horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "refferal_Slot",
							"type" : "image",

							"x" : 40 - 1,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/parameter_slot_04.sub",
						},
						{
							"name" : "refferal_value",
							"type" : "editline",

							"x" : 40 - 1 + 3,
							"y" : 0,

							"input_limit" : 12,

							"width" : 90,
							"height" : 20,
						},
					),
				},