# -*- coding: utf-8 -*-

import alfred,sys,os
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

reload(sys) 
sys.setdefaultencoding('UTF-8')
query = ""
if len(sys.argv)==2: 
    query= sys.argv[1]
results = []
workspaces = []
IDEAIndex =[]
ideaFolder = []

if query==r'/rebuild':
    os.remove('IDEA.index')
    aitem = alfred.Item({'uid': -1, 'arg' : ""},"Rebuild Search Index", "please don't click on this item")
    results.append(aitem)
# prepare for Index
try :
    if os._exists('IDEA.index'):
        for ind in open('IDEA.index'):
            IDEAIndex.append(ind.strip('\n'))
    else:
        #read workspaces from workspace.conf
        for line in open('workspaces.conf'):
            workspaces.append(line.strip('\n') )

        indexFile = open('IDEA.index','w')
        for rootdir in workspaces:
            rootdir_levels = rootdir.split('/')
            for root,subFolders,files in os.walk(rootdir):
                nested_levels = root.split('/')
                if '.idea' in subFolders:
                    ideaFolder.append(root)
                    indexFile.write(root+"\n")
                if(len(nested_levels)-len(rootdir_levels)>2):
                    del subFolders[:]
        indexFile.close()
except IOError:
    if os._exists('workspaces.conf')==False:
        aitem = alfred.Item({'uid': -1, 'arg' : ""},"Workspaces.conf not found", "Please open workflow folder and configure your workspaces.conf")
    else:
        aitem = alfred.Item({'uid': -1, 'arg' : ""},"IOError", "Please Check Configuration")
    results.append(aitem)

if len(ideaFolder) > 0 :
    index = 0
    for item in ideaFolder:
        title = os.path.split(item)[1]
        if query!="" and title.find(query)==-1 :
            continue
        subtitle = item
        aitem = alfred.Item({'uid': index, 'arg' : item}, title, subtitle)
        results.append(aitem)
        index += 1

xml = alfred.xml(results)
alfred.write(xml)
