import vcs

# Adapted for numpy/ma/cdms2 by convertcdms.py
"""
# Text Combined (Tc) module
"""
###############################################################################
#                                                                             #
# Module:       textcombined (Tc) module                                      #
#                                                                             #
# Copyright:    2000, Regents of the University of California                 #
#               This software may not be distributed to others without        #
#               permission of the author.                                     #
#                                                                             #
# Author:       PCMDI Software Team                                           #
#               Lawrence Livermore NationalLaboratory:                        #
#               support@pcmdi.llnl.gov                                        #
#                                                                             #
# Description:  Python command wrapper for VCS's text combined secondary      #
#               object. Can be thought of as the combination of text table    #
#               and text orientation secondary objects.			      #
#                                                                             #
# Version:      4.0                                                           #
#                                                                             #
###############################################################################
#
#
#
###############################################################################
#                                                                             #
# Import: Text table (Tt), and  Text orientation  (To)                        #
#                                                                             #
###############################################################################
import texttable
import textorientation

#############################################################################
#                                                                           #
# Text Combined (Tc) Class.                                                 #
#                                                                           #
#############################################################################


class Tc(object):

    """
 Class: Tc                              # Text Combined

 Description of Tc Class:
    The (Tc) Text Combined class will combine a text table class and a text orientation
    class together. From combining the two classess, the user will be able to set
    attributes for both classes (i.e., define the font, spacing, expansion, color
    index, height, angle, path, vertical alignment, and horizontal alignment).

    This class is used to define and list a combined text table and text orientation
    entry used in VCS.

 Other Useful Functions:
             a=vcs.init()               # Constructor
             a.show('texttable')        # Show predefined text table objects
             a.show('textorientation')  # Show predefined text orientation objects
             a.update()                 # Updates the VCS Canvas at user's request
             a.mode=1, or 0             # If 1, then automatic update, else if
                                          0, then use update function to
                                          update the VCS Canvas.
 Example of Use:
    a=vcs.init()
    To Create a new instance of text table use:
     tc=a.createtextcombined('new_tt','std','new_to','7left')  # Copies content of
                                        # 'std' to 'new_tt' and '7left' to 'new_to'

    To Modify an existing texttable use:
     tc=a.gettextcombined('std','7left')

    tc.list()                           # Will list all the textcombined attribute values
                                        # (i.e., texttable and textorientation attributes
    Specify the text font type:
     tc.font=1                          # The font value must be in the range 1 to 9

    Specify the text spacing:
     tc.spacing=2                       # The spacing value must be in the range -50 to 50

    Specify the text expansion:
     tc.expansion=100                   # The expansion value ranges from 50 to 150

    Specify the text color:
     tc.color=241                       # The text color value ranges from 1 to 257

    Specify the graphics text priority on the VCS Canvas:
     tt.priority = 1

    Specify the viewport and world coordinate:
     tt.viewport=[0, 1.0, 0,1.0]        # FloatType [0,1]x[0,1]
     tt.worldcoordinate=[0,1.0,0,1.0]   # FloatType [#,#]x[#,#]

    Specify the location of the text:
     tt.x=[[0,.1,.2], [.3,.4,.5]]        # List of FloatTypes
     tt.y=[[.5,.4,.3], [.2,.1,0]]        # List of FloatTypes

    Specify the text height:
     tc.height=20                       # The height value must be an integer

    Specify the text angle:
     tc.angle=0                         # The angle value ranges from 0 to 360

    Specify the text path:
     tc.path='right'                    # Same as tc.path=0
     tc.path='left'                     # Same as tc.path=1
     tc.path='up'                       # Same as tc.path=2
     tc.path='down'                     # Same as tc.path=3

    Specify the text horizontal alignment:
     tc.halign='right'                  # Same as tc.halign=0
     tc.halign='center'                 # Same as tc.halign=1
     tc.halign='right'                  # Same as tc.halign=2

    Specify the text vertical alignment:
     tc.valign='tcp'                    # Same as tcvalign=0
     tc.valign='cap'                    # Same as tcvalign=1
     tc.valign='half'                   # Same as tcvalign=2
     tc.valign='base'                   # Same as tcvalign=3
     tc.valign='bottom'                 # Same as tcvalign=4
"""

    __slots__ = [
        's_name',
        'name',
        'Tt_name',
        'To_name',
        'To',
        'Tt',
        'color',
        'fillincolor',
        'priority',
        'font',
        'string',
        'spacing',
        'expansion',
        'viewport',
        'worldcoordinate',
        'x',
        'y',
        'projection',
        'height',
        'angle',
        'path',
        'halign',
        'valign',
    ]

    def _getTtname(self):
        return self.Tt.name

    def _setTtname(self, value):
        self.Tt.name = value
    Tt_name = property(_getTtname, _setTtname)

    def _getToname(self):
        return self.To.name

    def _setToname(self, value):
        self.To.name = value
    To_name = property(_getToname, _setToname)

    def _getcolor(self):
        return self.Tt.color

    def _setcolor(self, value):
        self.Tt.color = value
    color = property(_getcolor, _setcolor)

    def _getfcolor(self):
        return self.Tt.fillincolor

    def _setfcolor(self, value):
        self.Tt.fillincolor = value
    fillincolor = property(_getfcolor, _setfcolor)

    def _getpriority(self):
        return self.Tt.priority

    def _setpriority(self, value):
        self.Tt.priority = value
    priority = property(_getpriority, _setpriority)

    def _getfont(self):
        return self.Tt.font

    def _setfont(self, value):
        self.Tt.font = value
    font = property(_getfont, _setfont)

    def _getstring(self):
        return self.Tt.string

    def _setstring(self, value):
        self.Tt.string = value
    string = property(_getstring, _setstring)

    def _getspacing(self):
        return self.Tt.spacing

    def _setspacing(self, value):
        self.Tt.spacing = value
    spacing = property(_getspacing, _setspacing)

    def _getexpansion(self):
        return self.Tt.expansion

    def _setexpansion(self, value):
        self.Tt.expansion = value
    expansion = property(_getexpansion, _setexpansion)

    def _getx(self):
        return self.Tt.x

    def _setx(self, value):
        self.Tt.x = value
    x = property(_getx, _setx)

    def _gety(self):
        return self.Tt.y

    def _sety(self, value):
        self.Tt.y = value
    y = property(_gety, _sety)

    def _getviewport(self):
        return self.Tt.viewport

    def _setviewport(self, value):
        self.Tt.viewport = value
    viewport = property(_getviewport, _setviewport)

    def _getworldcoordinate(self):
        return self.Tt.worldcoordinate

    def _setworldcoordinate(self, value):
        self.Tt.worldcoordinate = value
    worldcoordinate = property(_getworldcoordinate, _setworldcoordinate)

    def _getprojection(self):
        return self.Tt.projection

    def _setprojection(self, value):
        self.Tt.projection = value
    projection = property(_getprojection, _setprojection)

    def _getheight(self):
        return self.To.height

    def _setheight(self, value):
        self.To.height = value
    height = property(_getheight, _setheight)

    def _getangle(self):
        return self.To.angle

    def _setangle(self, value):
        self.To.angle = value
    angle = property(_getangle, _setangle)

    def _getpath(self):
        return self.To.path

    def _setpath(self, value):
        self.To.path = value
    path = property(_getpath, _setpath)

    def _gethalign(self):
        return self.To.halign

    def _sethalign(self, value):
        self.To.halign = value
    halign = property(_gethalign, _sethalign)

    def _getvalign(self):
        return self.To.valign

    def _setvalign(self, value):
        self.To.valign = value
    valign = property(_getvalign, _setvalign)

    ##########################################################################
    #                                                                           #
    # Initialize the text combine attributes.                                   #
    #                                                                           #
    ##########################################################################
    def __init__(self, Tt_name=None, Tt_name_src='default',
                 To_name=None, To_name_src='default'):
        import vcs
        if (Tt_name is None):
            raise ValueError('Must provide a text table name.')
        if (To_name is None):
            To_name = Tt_name  # Uses the same name than Tt

        if Tt_name in vcs.elements["texttable"]:
            raise Exception(
                "Error texttable object: '%s' already exists" %
                Tt_name)
        if To_name in vcs.elements["textorientation"]:
            raise Exception(
                "Error textorientation object: '%s' already exists" %
                To_name)
        #                                                                 #
        ###################################################################
        # Inherits texttable and textorientation secondary sub-classes.   #
        ###################################################################
        #                                                                 #
        self.Tt = texttable.Tt(Tt_name, Tt_name_src)
        self.To = textorientation.To(To_name, To_name_src)
        self.name = "%s:::%s" % (Tt_name, To_name)
        self.s_name = 'Tc'
        vcs.elements["textcombined"][self.name] = self
        #                                                         #
        ###########################################################
        # Save the parent class.                                  #
        ###########################################################
        #                                                         #

    ##########################################################################
    #                                                                           #
    # List out text combined members (attributes).                              #
    #                                                                           #
    ##########################################################################
    def list(self):
        if ((self.Tt_name == '__removed_from_VCS__') or
                (self.To_name == '__removed_from_VCS__')):
            raise ValueError('This instance has been removed from VCS.')
        print "", "----------Text combined (Tc) member (attribute) listings ----------"
        print "secondary method =", self.s_name
        print "", "----------Text Table (Tt) member (attribute) listings ----------"
        print "Tt_name =", self.Tt_name
        print "font =", self.font
        print "spacing =", self.spacing
        print "expansion =", self.expansion
        print "color =", self.color
        print "fillincolor =", self.fillincolor
        print "priority =", self.priority
        print "string =", self.string
        print "viewport =", self.viewport
        print "worldcoordinate =", self.worldcoordinate
        print "x =", self.x
        print "y =", self.y
        print "projection =", self.projection
        print "", "----------Text Orientation (To) member (attribute) listings ----------"
        print "To_name =", self.To_name
        print "height =", self.height
        print "angle =", self.angle
        print "path =", self.path
        print "halign =", self.halign
        print "valign =", self.valign

    ##########################################################################
    #                                                                           #
    # Script out secondary text table and orientation methods in VCS to a file. #
    #                                                                           #
    ##########################################################################
    def script(self, script_filename=None, mode=None):
        '''
 Function:     script                           # Calls _vcs.scripTo

 Description of Function:
       Saves out a text table and text orientation graphics method in Python or
       VCS script form to a designated file.

 Example of Use:
    script(scriptfile_name,mode)
              where: scriptfile_name is the output name of the script file.
                     mode is either "w" for replace or "a" for append.

              Note: If the the filename has a ".py" at the end, it will produce a
                    Python script. If the filename has a ".scr" at the end, it will
                    produce a VCS script. If neither extensions are give, then by
                    default a Python script will be produced.

    a=vcs.init()
    tc=a.createtextcombined('new_tt','std','new_to','7left')
    tc.script('filename.py')	     # Append to a Python file "filename.py"
    tc.script('filename.scr')	     # Append to a VCS file "filename.scr"
    tc.script('filename','w')	     # Create or overwrite to a Python file "filename.py"
'''
        if (script_filename is None):
            raise ValueError(
                'Error - Must provide an output script file name.')

        if (mode is None):
            mode = 'a'
        elif (mode not in ('w', 'a')):
            raise ValueError(
                'Error - Mode can only be "w" for replace or "a" for append.')

        # By default, save file in json
        scr_type = script_filename.split(".")
        if len(scr_type) == 1 or len(scr_type[-1]) > 5:
            scr_type = "json"
            if script_filename != "initial.attributes":
                script_filename += ".json"
        else:
            scr_type = scr_type[-1]
        if scr_type == '.scr':
            raise DeprecationWarning("scr script are no longer generated")
        elif scr_type == "py":
            mode = mode + '+'
            py_type = script_filename[
                len(script_filename) -
                3:len(script_filename)]
            if (py_type != '.py'):
                script_filename = script_filename + '.py'

            # Write to file
            fp = open(script_filename, mode)
            if (fp.tell() == 0):  # Must be a new file, so include below
                fp.write("#####################################\n")
                fp.write("#                                 #\n")
                fp.write("# Import and Initialize VCS     #\n")
                fp.write("#                             #\n")
                fp.write("#############################\n")
                fp.write("import vcs\n")
                fp.write("v=vcs.init()\n\n")

            unique_name = '__Tt__' + self.Tt_name
            fp.write(
                "#----------Text Table (Tt) member (attribute) listings ----------\n")
            fp.write("tt_list=v.listelements('texttable')\n")
            fp.write("if ('%s' in tt_list):\n" % self.Tt_name)
            fp.write(
                "   %s = v.gettexttable('%s')\n" %
                (unique_name, self.Tt_name))
            fp.write("else:\n")
            fp.write(
                "   %s = v.createtexttable('%s')\n" %
                (unique_name, self.Tt_name))
            fp.write("%s.font = %g\n" % (unique_name, self.font))
            fp.write("%s.spacing = %g\n" % (unique_name, self.spacing))
            fp.write("%s.expansion = %g\n" % (unique_name, self.expansion))
            fp.write("%s.color = %g\n\n" % (unique_name, self.color))
            fp.write(
                "%s.fillincolor = %g\n\n" %
                (unique_name, self.fillincolor))
            fp.write("%s.priority = %d\n" % (unique_name, self.priority))
            fp.write("%s.viewport = %s\n" % (unique_name, self.viewport))
            fp.write(
                "%s.worldcoordinate = %s\n" %
                (unique_name, self.worldcoordinate))
            fp.write("%s.x = %s\n" % (unique_name, self.x))
            fp.write("%s.y = %s\n\n" % (unique_name, self.y))
            fp.write("%s.projection = %s\n\n" % (unique_name, self.projection))

            unique_name = '__To__' + self.To_name
            fp.write(
                "#----------Text Orientation (To) member (attribute) listings ----------\n")
            fp.write("to_list=v.listelements('textorientation')\n")
            fp.write("if ('%s' in to_list):\n" % self.To_name)
            fp.write(
                "   %s = v.gettextorientation('%s')\n" %
                (unique_name, self.To_name))
            fp.write("else:\n")
            fp.write(
                "   %s = v.createtextorientation('%s')\n" %
                (unique_name, self.To_name))
            fp.write("%s.height = %g\n" % (unique_name, self.height))
            fp.write("%s.angle = %g\n" % (unique_name, self.angle))
            fp.write("%s.path = '%s'\n" % (unique_name, self.path))
            fp.write("%s.halign = '%s'\n" % (unique_name, self.halign))
            fp.write("%s.valign = '%s'\n\n" % (unique_name, self.valign))
            fp.close()
        else:
            # Json type
            mode += "+"
            f = open(script_filename, mode)
            vcs.utils.dumpToJson(self.To, f)
            f.close()
            f = open(script_filename, 'a+')
            vcs.utils.dumpToJson(self.Tt, f)
            f.close()

##########################################################################
#        END OF FILE                                                            #
##########################################################################
