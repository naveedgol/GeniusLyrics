tell application "iTunes"
	if selection = {} then
		display dialog "No track selected" buttons {"Ok"} with icon caution
		error number -128
	end if
	set songName to name of selection
	set artistName to name of selection
end tell

set py to "python main.py " & songName & " " & artistName
do shell script py
set theFile to "lyrics.txt"
set fileContents to read theFile
display dialog fileContents

tell application "iTunes"
	set lyrics of selection to fileContents
end tell