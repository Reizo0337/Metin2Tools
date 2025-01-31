quest refferal_manage begin
	state start begin
		when letter begin
			send_letter("Manage Refferal")
		end
		
		when button or info begin
			say_title("Refferal Manage")
			say("[ENTER]What do you wanna do?[ENTER]")
			local opt1 = select("Add new refferal", "Remove refferal", "Cancel")
			if opt1 == 1 then
				say_title("Refferal Manage")
				say("Hello "..pc.get_name().."[ENTER]Write below the refferal code that you want to add:")
				local code = input()
				
				add_new_refferal(code)
				
				syschat("I have added succesfully this refferal code "..code..".")
			end
			if opt1 == 2 then
				say_title("Refferal Manage")
				say("Hello "..pc.get_name().."[ENTER]Write below the refferal code that you want to add:")
				local code = input()
				
				remove_refferal(code)
				
				syschat("I have removed succesfully this refferal code "..code..".")
			end
		end
	end
end