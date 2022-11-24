Doing this research trying to use open-source software when I can, I came across a couple of technical issues. Here are some that I found:

# LibreOffice

Note: These workarounds are only done in the latest version of LibreOffice as of November 2022, which is version 7.4.2.3. It admittedly is not the stable version of LibreOffice, but rather the latest development version, which **The Document Foundation** recommends only for technology enthusiasts or power users. So all that is listed here may only work for this specific version and may not work for previous or future versions.

## LibreOffice Calc

1. There seems to be no obvious way to have an axis label in a chart contain text that is subscript or superscript, for example Z<sub>phase</sub> cannot be written in a normal axis label. This seems to be a normal feature in MS Office, WPS Office, and even OnlyOffice, to name a few alternatives. One workaround that I found and implemented is:

* Insert an axis label with a dummy text and colour the font white, so there is an empty space where the axis label should be.
* Create a textbox and write the desired title, as textboxes can contain superscript and subscript text.
* Place the textbox in the place of the dummy axis label. If it's the y-axis label, then you need to rotate the textbox by 90 degrees, otherwise if it's the x-axis label then just drag the textbox to the chart.
* Shift-select the textbox and shift-select the chart (this is how you do multiple selection in LibreOffice).
* Right click the object, and click "Group". This will combine the two objects (textbox that you created, and the chart) into one object.
* You can now drag the chart around and the textbox will become the ad hoc axis label.
* You can also right-click the chart and click "Ungroup" if you wish to edit the chart again in any way. 

## LibreOffice Draw

1. This is not technically part of research, but if you find yourself needing to edit PDFs like filling out forms with texts or digital signatures, you may find issues when attempting to export it to a PDF after you finished editing it in LibreOffice Draw. You will find that the PDF that you exported will contain no text, but retain some elements such as table borders or lines. So, it is somewhat irritating if you need to edit PDFs by inserting texts, but I found a way to kinda make it work albeit not as I wanted. This is again a workaround, and so far I have found a fix if you're using Lubuntu as your operating system, as is found [here](https://ask.libreoffice.org/t/export-or-print-to-pdf-no-text/52178/18) and [here](https://ask.libreoffice.org/t/text-not-showing-when-exporting-to-pdf-or-printing-in-6-4-4-2/55075/8), though again both of these are fixes specifically for Lubuntu and also, for previous LibreOffice versions which are of the 6.4.x.x versions. At the moment though I'm using Windows 10 as my OS, and this is the only thing I've been able to do.

* You can drag and drop PDF files into LibreOffice Draw.
* Edit them as you wish by inserting texts or lines/shapes.
* First, try exporting to PDF as normal. If you find that somehow it exported with no issues, then that's great. If you find that the exported PDF is missing its texts (and you can tell since you can highlight the text despite the fact that it's unreadable as is), then go to this next step.
* Right-click the PDF that you dragged and dropped inside the LibreOffice canvas.
* Click "Convert", and then click "Curve".
* Then, export it to PDF. Everything should be fine.

My issue with this workaround is that the final exported PDF does not export any *original* text of the PDF that you dragged and dropped in LibreOffice Draw, since you have converted it to "Curve", which means that it's now become just a graphical object. You cannot highlight any original text in the final PDF except for the text that you've added. This is quite irritating but it's the best I can do. I may experiment with GIMP for document editing and I will add it in this page once I ascertained GIMP's capabilities in editing PDFs.

# Qualcoder

1. Qualcoder is an open-source computer-assisted qualitative data analysis software (CAQDAS). I use it for text coding. Now, the way that Qualcoder works is that it converts PDFs (if you use PDFs) into plain text. In theory this seems fine, but it doesn't convert it very well, at least for the PDFs that I use (journal articles). The text gets jumbled up quite badly, as in, the lines and paragraphs get really messy. Here's a way I mitigate the issue:

* Instead of letting the software natively convert the text using its own engine, what I simply do is I open up a PDF reader and simply CTRL+A and CTRL+C to copy the whole *text*.
* Open Qualcoder, and create a new text file in the Manage Files tab.
* CTRL+V to paste the text. Usually, this will turn out better than letting the native PDF conversion engine does its work.
* Usually I just leave it like that, but sometimes I'll do some minor corrections like correct spacings or paragraphings or I'll just add new texts where I feel necessary.