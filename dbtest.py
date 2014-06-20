# coding:utf8

import json,os

db = []

def readfile():
    f = open('dbfile', 'rb')
    # print f
    for line in f:
        # print line
        db.append(json.loads(line))
        # print json.loads(line)
    return db

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

PAGE_SIZE = 20

def get_page_link():
    pbtn = ""
    for i in range(0,len(db)/PAGE_SIZE+1):
        pbtn += """<a href="/p/"""+str(i)+"""">"""+str(i)+"""</a>&nbsp;"""
    return pbtn

def get_page(pno, psize = PAGE_SIZE):
    """ page no start from 0 """
    page = ""
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
    page += get_page_link()
    return page

if __name__ == "__main__":
    readfile()
    # print get_crack_pic_code("http://imgsrc.baidu.com/forum/pic/item/b29a5a63f6246b606f4a2fdaeaf81a4c500fa26f.jpg")
    print len(db)
    print get_page(2,20)
    print get_page_link()
