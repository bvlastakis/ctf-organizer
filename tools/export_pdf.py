import os
import sys
import cStringIO
import xhtml2pdf.pisa as pisa
import xhtml2pdf

def testSimple(
    data= "table_test.html",
    dest= "test.pdf"):

    """
    Simple test showing how to create a PDF file from
    PML Source String. Also shows errors and tries to start
    the resulting PDF
    """

    pdf = pisa.CreatePDF(
        file(data, "r" ),
        file(dest, "wb")
        )

def testURL(
    url="https://yalesurvey.qualtrics.com/CP/Report.php?SID=SV_79h5Dtghhos9qHr&R=R_896vN1HuugF02cB",
    dest="test-website.pdf"):

    """
    Loading from an URL. We open a file like object for the URL by
    using 'urllib'. If there have to be loaded more data from the web,
    the pisaLinkLoader helper is passed as 'link_callback'. The
    pisaLinkLoader creates temporary files for everything it loads, because
    the Reportlab Toolkit needs real filenames for images and stuff. Then
    we also pass the url as 'path' for relative path calculations.
    """
    import urllib

    pdf = pisa.CreatePDF(
        urllib.urlopen(url),
        file(dest, "wb"),
        log_warn = 1,
        log_err = 1,
        path = url,
        link_callback = pisa.pisaLinkLoader(url).getFileName
        )


if __name__ == '__main__':
    testURL()
