# coding:utf8

import json,os
from bottle import template

db = []

def readfile():
    f = open('dbfile', 'rb')
    # print f
    for line in f:
        # print line
        db.append(json.loads(line))
        # print json.loads(line)
    return db

def button_style():
    """
    http://codepen.io/jimram/pen/EBmJD
    """
    return u"""
<style>
    /* Base styles */
.btn-instagram {
  font-size: 1.2em;
  font-family: sans-serif;
  color:#333;
	text-shadow:1px 1px #fff;
	text-decoration: none;
	display:inline-block; 
	padding:0.5em 1.75em 0.5em 1em;
	border-radius: 0.25em;
	background: #f8f8f8;
	border:1px solid #ccc;
	border-right:0.25em solid #00558D; /* blue stripe */
	position: relative;
	margin:0 0 1px; 
}

.btn-instagram:before, .btn-instagram:after {
	content:'';
	display:block;
	position: absolute;
}

/* Add Stripes */
.btn-instagram:before {
	width:0.25em;
	height: 100%;
	background:#FBB03B; /* yellow stripe */ 
	border-left:0.25em solid #D4145A; /* red stripe */ 
	border-right:0.25em solid #00A99D; /* green stripe */ 
	top:0;
	right:0;
}

/* Add Hightlights */
.btn-instagram:after {
	width:100%;
	height: 100%;
	top: 0;
	left: 0;
	border-radius: 0.25em;
	padding-left: 0.25em;
	box-shadow: inset 1px 1px 0px rgba(255,255,255,0.5), inset -1px -1px 0 rgba(0,0,0,0.1);

background: -moz-linear-gradient(top,  rgba(255,255,255,0.35) 0%, rgba(255,255,255,0.2) 49%, rgba(255,255,255,0) 50%, rgba(0,0,0,0.1) 100%);
background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(255,255,255,0.35)), color-stop(49%,rgba(255,255,255,0.2)), color-stop(50%,rgba(255,255,255,0)), color-stop(100%,rgba(0,0,0,0.1)));
background: -webkit-linear-gradient(top,  rgba(255,255,255,0.35) 0%,rgba(255,255,255,0.2) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.1) 100%);
background: -o-linear-gradient(top,  rgba(255,255,255,0.35) 0%,rgba(255,255,255,0.2) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.1) 100%);
background: -ms-linear-gradient(top,  rgba(255,255,255,0.35) 0%,rgba(255,255,255,0.2) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.1) 100%);
background: linear-gradient(to bottom,  rgba(255,255,255,0.35) 0%,rgba(255,255,255,0.2) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.1) 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#59ffffff', endColorstr='#1a000000',GradientType=0 );

}


/* Animate - Fade */
.btn-instagram, .btn-instagram:before {
    -webkit-transition-property: background, border;
    -webkit-transition: 0.1s ease-in;
    -moz-transition-property: background, border;
    -moz-transition: 0.1s ease-in;
    -o-transition-property: background, border;
    -o-transition: 0.1s ease-in;
    transition-property: background, border;
    transition: 0.1s ease-in;

}

/* Hover / Focus */
.btn-instagram:hover, .btn-instagram:focus  {
	background: #fff;
}

.btn-instagram:hover {
	border-right:0.25em solid #09c;
}

.btn-instagram:hover:before {
	background:#fc6; /* yellow stripe */ 
	border-left:0.25em solid #f06; /* red stripe */ 
	border-right:0.25em solid #0cc; /* green stripe */ 
}

.btn-instagram:hover:after {
background: -moz-linear-gradient(top,  rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.1) 49%, rgba(255,255,255,0) 50%, rgba(0,0,0,0.05) 100%);
background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(255,255,255,0.25)), color-stop(49%,rgba(255,255,255,0.1)), color-stop(50%,rgba(255,255,255,0)), color-stop(100%,rgba(0,0,0,0.05)));
background: -webkit-linear-gradient(top,  rgba(255,255,255,0.25) 0%,rgba(255,255,255,0.1) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.05) 100%);
background: -o-linear-gradient(top,  rgba(255,255,255,0.25) 0%,rgba(255,255,255,0.1) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.05) 100%);
background: -ms-linear-gradient(top,  rgba(255,255,255,0.25) 0%,rgba(255,255,255,0.1) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.05) 100%);
background: linear-gradient(to bottom,  rgba(255,255,255,0.25) 0%,rgba(255,255,255,0.1) 49%,rgba(255,255,255,0) 50%,rgba(0,0,0,0.05) 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#40ffffff', endColorstr='#0d000000',GradientType=0 );

}

/* Active */
.btn-instagram:active {
	margin:1px 0 0; 
}

</style>
"""

def get_crack_pic_code(url):
    randstr = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16)))
    return u"""

    <script>
var im_"""+ randstr +""" = "<img style='max-height:500px;width:auto;' src="""+url+""">";

</script>
<iframe id=im_""" + randstr +""" style="border:0px;overflow:hidden;" 
scrolling="no" frameborder="0" src="javascript:parent.im_""" + randstr + """;" 
onload="javascript:var x=document.getElementById('im_"""+randstr+"""').contentWindow.document.images[0];
this.width=x.width+10;this.height=x.height+10;"></iframe>

"""

def get_title(title, year=""):
    return u"""

<br>
<h3>""" + year + """ - """ + title + """</h3>

"""

def get_link(link):
    return u"""
<p>""" + link + """</p>
<br>
"""

def get_torrent_download(link):
    return template("torrentdown", magnet=link, hashv=link.split(':')[3])

PAGE_SIZE = 20

def get_page_link():
    pbtn = ""
    for i in range(0,len(db)/PAGE_SIZE+1):
        pbtn += """<a href="/p/"""+str(i)+"""">"""+str(i)+"""</a>&nbsp;"""
    return pbtn

def get_page(pno, psize = PAGE_SIZE):
    """ page no start from 0 """
    page = ""
    page += button_style()
    for i in [j for j in range(pno * psize, (pno + 1) * psize) if j < len(db)]:
        # page += str(i) + ' '
        # print db[i].get('image')  #magnet
        year = db[i].get('year')
        # if( type(year) == int ):
        year = str(year) if type(year)==int else year
        # print year
        name = db[i].get('name')
        if name is not None:
            if year is not None:
                page += get_title(name, year)
            else:
                page += get_title(name)
        pic = db[i].get('image')
        if pic is not None:
            page += get_crack_pic_code(pic) 
        link = db[i].get('magnet')
        if link is not None:
            page += get_link(link) 
            link = link.upper()
            page += get_torrent_download(link)
    page += get_page_link()
    return page

if __name__ == "__main__":
    readfile()
    # print get_crack_pic_code("http://imgsrc.baidu.com/forum/pic/item/b29a5a63f6246b606f4a2fdaeaf81a4c500fa26f.jpg")
    print len(db)
    print get_page(2,20)
    print get_page_link()
