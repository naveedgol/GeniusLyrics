tell application "iTunes"
	if selection = {} then
		display dialog "No track selected" buttons {"Ok"} with icon caution
		error number -128
	end if
	set songName to name of selection
	set artistName to artist of selection
end tell

set pathwithspaces to "/Users/Naveed/Documents/Side Projects/GeniusLyrics/main.py"

set py to "/usr/local/bin/python3 " & quoted form of pathwithspaces & " \"" & artistName & "\" \"" & songName & "\""
do shell script py

set newLyrics to (read POSIX file "/Users/Naveed/Documents/Side Projects/GeniusLyrics/lyrics.txt")
if newLyrics = "Lyrics not found" then
	display dialog "Lyrics not found" buttons {"Ok"} with icon caution
	error number -128
end if

tell application "iTunes"
	set lyrics of selection to newLyrics as string
end tell