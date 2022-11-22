Doing this research trying to use open-source software when I can, I came across a couple of technical issues. Here are some that I found:

# LibreOffice

1. There seems to be no obvious way to have an axis label in a chart contain text that is subscript or superscript, for example Z<sub>phase</sub> cannot be written in a normal axis label. This seems to be a normal feature in MS Office, WPS Office, and even OnlyOffice, to name a few alternatives. One workaround that I found and implemented is:

* Insert an axis label with a dummy text and colour the font white, so there is an empty space where the axis label should be.
* Create a textbox and write the desired title, as textboxes can contain superscript and subscript text.
* Place the textbox in the place of the dummy axis label. If it's the y-axis label, then you need to rotate the textbox by 90 degrees, otherwise if it's the x-axis label then just drag the textbox to the chart.
* Shift-select the textbox and shift-select the chart (this is how you do multiple selection in LibreOffice).
* Right click the object, and click "Group". This will combine the two objects (textbox that you created, and the chart) into one object.
* You can now drag the chart around and the textbox will become the ad hoc axis label.
* You can also right-click the chart and click "Ungroup" if you wish to edit the chart again in any way. 

Note: This is done in the latest version of LibreOffice as of 2022, which is version 7.4.2.3.

# Qualcoder

1. Qualcoder is an open-source computer-assisted qualitative data analysis software (CAQDAS). I use it for text coding. Now, the way that Qualcoder works is that it converts PDFs (if you use PDFs) into plain text. In theory this seems fine, but it doesn't convert it very well, at least for the PDFs that I use (journal articles). The text gets jumbled up quite badly, as in, the lines and paragraphs get really messy. Here's a way I mitigate the issue:

* Instead of letting the software natively convert the text using its own engine, what I simply do is I open up a PDF reader and simply CTRL+A and CTRL+C to copy the whole *text*.
* Open Qualcoder, and create a new text file in the Manage Files tab.
* CTRL+V to paste the text. Usually, this will turn out better than letting the native PDF conversion engine does its work.
* Usually I just leave it like that, but sometimes I'll do some minor corrections like correct spacings or paragraphings or I'll just add new texts where I feel necessary.