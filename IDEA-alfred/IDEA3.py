# -*- coding: utf-8 -*-

import sys,os
from workflow import Workflow, Workflow3

def main(wf):
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    args = wf.args
    query = ""
    if len(wf.args)==1: 
        query= wf.args[0]
    workspaces = []
    IDEAIndex =[]
    ideaFolder = []
    if query==r'/rebuild':
        os.remove('IDEA.index')
        wf.add_item("Rebuild Search Index","Please don't open on this item", arg='', autocomplete=None, uid = -1)
        wf.send_feedback()

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
            wf.add_item("Workspaces.conf not found","Please open workflow folder and configure your workspaces.conf", arg='', autocomplete=None, uid = -1)
        else:
            wf.add_item("IOError","Please Check Configuration", arg='', autocomplete=None, uid = -1)
    
    if len(ideaFolder) > 0 :
        index = 0
        for item in ideaFolder:
            title = os.path.split(item)[1]
            if query!="" and title.find(query)==-1 :
                continue
            subtitle = item
            wf.add_item(title,subtitle, arg=item, autocomplete=None, uid = index)
            index += 1
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
