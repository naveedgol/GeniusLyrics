tell application "iTunes"
	if selection = {} then
		display dialog "No track selected" buttons {"Ok"} with icon caution
		error number -128
	end if
end tell

set theFile to "/Library/iTunes/Scripts/lyrics.txt"
set fileContents to read theFile
display dialog fileContents

tell application "iTunes"
	set lyrics of selection to fileContents
end tell