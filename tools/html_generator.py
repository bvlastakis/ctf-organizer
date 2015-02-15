
def header(title):
	"""Generates the header string file to be written to .html file"""

	header_string = """
	<html>
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>""" + title + """</title>
	<style type="text/css">
body
{
    line-height: 1.6em;
}

#newspaper-a
{
    font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
    font-size: 12px;
    margin: 45px;
    width: 720px;
    text-align: left;
    border-collapse: collapse;
    border: 2px solid #69c;
}
#newspaper-a th
{
    padding: 7px 17px 2px 17px;
    font-weight: normal;
    font-size: 12px;
    color: #039;
    border-top: 1px dashed #69c;
}
#newspaper-a td
{
    padding: 2px 17px 7px 17px;
    color: #669;
}
#newspaper-a tbody tr:hover td
{
    color: #339;
    background: #d0dafd;
    border-bottom: 1px dashed #69c;
}</style>
</head>
<body>"""

	return header_string

def table(question, answer):
	"""Generates the string for a single table to be written to .html file"""

	table_string = """
    <thead>
    	<tr>
        	<th scope="col">""" + question + """</th>
        </tr>
    </thead>
    <tbody>
    	<tr>
        	<td>""" + answer + """</td>
        </tr>

    </tbody>
"""

	return table_string

def table_header(question):
	"""Generates the string for a single table to be written to .html file"""

	table_string = """
	<table id="newspaper-a">
    <thead>
    	<tr>
        	<th scope="col">""" + question + """</th>
        </tr>
    </thead>
"""
	return table_string

def table_close():

	return """</table>"""

def close():

	close_string = """
    <thead>
    <table id = "newspaper-a">
        <tr>
            <th scope="col">Recommendation</th>
        </tr>
    </thead>
    </table>
            <object type="application/pdf" data="recommendation.pdf" width="90%" height="90%"> </object>
</body>

</html>"""
	return close_string

