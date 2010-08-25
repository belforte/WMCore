#/usr/bin/env python2.4
"""
_Destroy_

"""

__revision__ = "$Id: Destroy.py,v 1.2 2009/06/10 21:06:04 sryu Exp $"
__version__ = "$Revision: 1.2 $"

from WMCore.WorkQueue.Database.DestroyWorkQueueBase import DestroyWorkQueueBase
from WMCore.WorkQueue.Database.Oracle.Create import Create

class Destroy(DestroyWorkQueueBase):    
    def __init__(self, logger = None, dbi = None):
        """
        _init_

        Call the base class's constructor and add all necessary tables for 
        deletion,
        """
        print "----"        
        DestroyWorkQueueBase.__init__(self, logger, dbi)
    
        for tableName in Create.sequenceTables:
            seqname = '%s_SEQ' % tableName
            self.create["%s%s" % (Create.seqStartNum, seqname)] = \
                           "DROP SEQUENCE %s"  % seqname 
            # triggers have to be deleted first
            triggerName = '%s_TRG' % tableName
            self.create["%s%s" % ('00', triggerName)] = \
                           "DROP TRIGGER %s"  % triggerName 